#include "uniform_map.hpp"

#include "shake/graphics/gl/gl.hpp"

namespace shake {
namespace graphics {

//----------------------------------------------------------------
UniformMap get_uniform_map( const gl::ProgramId& program_id )
{
    const auto n_uniforms = gl::get_program_iv_active_uniforms( program_id );
    const auto max_uniform_name_length = gl::get_program_iv_active_uniform_max_lenght( program_id );
    
    auto uniform_map = UniformMap { };
    for (std::uint32_t uniform_index = 0; gl::Int{ uniform_index } < n_uniforms; ++uniform_index)
    {
        const auto gl_uniform_index = gl::Int { static_cast< gl::Int::value_type >( uniform_index ) };
        const auto active_uniform = gl::get_active_uniform( program_id, gl_uniform_index, max_uniform_name_length );
        uniform_map.emplace( active_uniform );
    }
    return uniform_map;
}

} // namespace graphics
} // namespace shake

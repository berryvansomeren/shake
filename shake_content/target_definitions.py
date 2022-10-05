from cmake_generator import (
    Target,
    SharedLibrary,
    absp
)

# ----------------------------------------------------------------
def get_target_definitions() -> Target:
    return SharedLibrary(
        name            = 'shake_content',
        src_dir_path    = absp( './src' ),
        dependencies    = [
            'freetype',
            'glm',
            'json11',
            'stb',
            'shake_core',
            'shake_graphics',
            'shake_io'
        ]
    )
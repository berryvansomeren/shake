from cmake_generator import (
    Target,
    SharedLibrary,
    absp
)

# ----------------------------------------------------------------
def get_target_definitions() -> Target:
    return SharedLibrary(
        name            = 'shake_main',
        src_dir_path    = absp( './src' ),
        dependencies    = [
            'glm',
            'json11',
            'shake_content',
            'shake_core',
            'shake_ecs',
            'shake_graphics',
            'shake_hid',
            'shake_io'
        ]
    )
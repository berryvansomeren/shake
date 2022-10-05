from cmake_generator import (
    Target,
    SharedLibrary,
    absp
)

# ----------------------------------------------------------------
def get_target_definitions() -> Target:
    return SharedLibrary(
        name            = 'shake_ecs',
        src_dir_path    = absp( './src' ),
        dependencies    =  [
            'glm',
            'shake_core',
            'shake_graphics',
            'shake_hid'
        ]
    )
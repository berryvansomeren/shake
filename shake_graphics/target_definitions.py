from cmake_generator import (
    Target,
    SharedLibrary,
    absp
)

# ----------------------------------------------------------------
def get_target_definitions() -> Target:
    return SharedLibrary(
        name            = 'shake_graphics',
        src_dir_path    = absp( './src' ),
        dependencies    =  [
            'glad',
            'glm',
            'shake_core'
        ]
    )
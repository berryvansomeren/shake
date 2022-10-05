from cmake_generator import (
    Target,
    SharedLibrary,
    absp
)

# ----------------------------------------------------------------
def get_target_definitions() -> Target:
    return SharedLibrary(
        name            = 'shake_io',
        src_dir_path    = absp( './src' ),
        dependencies    =  [
            'json11',
            'shake_core'
        ]
    )
from pathlib import Path
from typing import List

from cmake_generator import (
    PythonModule,
    Target,
    absp
)

# ----------------------------------------------------------------
def get_target_definitions() -> Target:
    return PythonModule(
        name = 'pyshake',
        src_dir_path = absp( './src' ),
        dependencies = [
            'glm',
            'pybind11',
            'shake_content',
            'shake_core',
            'shake_ecs',
            'shake_graphics',
            'shake_hid',
            'shake_io',
            'shake_main'
        ]
    )
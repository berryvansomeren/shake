import logging

import sys
sys.path.append("C:/Users/Berry/Documents/development/")
sys.path.append("C:/Users/Berry/Documents/development/cmake_generator")
from cmake_generator import Language, Project, Version, generate_cmake_file

# ----------------------------------------------------------------
def main():
    project_folder = 'C:/Users/Berry/Documents/development/shake'
    target_definition_file_paths = [
        f'{project_folder}/{path}/target_definitions.py' for path in [
            "external",
            "shake_content",
            "shake_core",
            "shake_ecs",
            "shake_graphics",
            "shake_hid",
            "shake_io",
            "shake_main",
            "shake_python",
        ]
    ]

    cmake_project_definition = Project(
        project_name                        = "shake",
        version                             = Version( 4, 0 ),
        destination_cmake_lists_file_path   = f'{project_folder}/CMakeLists.txt',
        build_directory_path                = f'{project_folder}/build/',
        target_definition_file_paths        = target_definition_file_paths,
        languages                           = [ 
            Language.CXX, 
            Language.C, 
            #Language.CUDA 
        ]
    )

    generate_cmake_file( cmake_project_definition )

# ----------------------------------------------------------------
if __name__ == "__main__":
    logging.basicConfig( level = logging.INFO )
    main()

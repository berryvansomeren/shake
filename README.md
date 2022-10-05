# shake

Shake is a(n abandoned) hobby game engine / programming sandbox.    

This is an older BitBucket project of mine that I mainly worked on from 2017 till 2019. 
Every new programmer at some point starts working on a project that is wat too big to ever finish. 
In the game industry people also say: "make games, not engines".
Shake was my way too big game engine project...
I never really focussed on actually developing game mechanics, 
but used the context of a game engine to explore different programming concepts. 
I never finished a game, nor the engine, but I did become a better programmer along the way. 
I still think it contains a few clever ideas so I'm keeping it around for future reference.

Shake is implemented using a C++ core with Python bindings for scripting.
Some of the more interesting concepts I was exploring are:
   
* OpenGL (4.6) and it's DSA features. 
* Entity-component-systems architectures for flexibility, scalability and performance in managing game worlds.
* Generating Python bindings (pyshake) created using Pybind11, that enable you to easily script your own games.
* Uses modern c++ features such as any, variant, visit and fold expressions.
* I also worked on custom (pre-c++20) ranges inspired by Python ranges and Boost Range, which are now in a separate repo: **[shake_ranges](https://github.com/berryvansomeren/sghake_ranges)**.

Shake uses CMake for build management, but actually uses Python for target specification.  
The corresponding CMakeLists.txt is generate automatically using my **[Cmake Generator](https://github.com/berryvansomeren/cmake_generator)**.

Since the CMakeLists.txt refers to paths on my local machine, you would have to regenerate the CMakeLists.txt file by running _make_cmake_file.py_.
The resulting project builds fine in Visual Studio 2019, but not out of the box in newer versions of Visual Studio. An example of pyshake can be used is found in _shake_test_game/main.py_
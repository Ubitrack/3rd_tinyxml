# conan-zlib

[Conan.io](https://conan.io) package for ZLIB library. 

The packages generated with this **conanfile** can be found in [conan.io](https://conan.io/source/ubitrack_tinyxml/2.5.3/ulricheck/stable).

## Build packages

    $ pip install conan_package_tools
    $ python build.py
    
## Upload packages to server

    $ conan upload ubitrack_tinyxml/2.5.3@ulricheck/stable --all
    
## Reuse the packages

### Basic setup

    $ conan install ubitrack_tinyxml/2.5.3@ulricheck/stable
    
### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
    ubitrack_tinyxml/2.5.3@ulricheck/stable

    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install . 

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.

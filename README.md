# ubitrack-tinyxml

[Conan.io](https://conan.io) package for tinyxml library. 

## Build packages

    $ pip install conan_package_tools
    $ python build.py
    
## Upload packages to server

    $ conan upload ubitrack_tinyxml/2.5.3@camposs/stable --all
    
## Reuse the packages

### Basic setup

    $ conan install ubitrack_tinyxml/2.5.3@camposs/stable
    
### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
    ubitrack_tinyxml/2.5.3@camposs/stable

    [options]
    ubitrack_tinyxml:shared=true # false
    
    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install . 

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.

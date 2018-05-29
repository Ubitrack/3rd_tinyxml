from conans import ConanFile, CMake, tools
import os


class UbitracktinyxmlConan(ConanFile):
    name = "ubitrack_tinyxml"
    version = "2.5.3"
    license = "http://www.grinninglizard.com/tinyxml/"
    url = "https://github.com/Ubitrack/3rd_tinyxml"
    description = "TinyXML is a simple, small, C++ XML parser that can be easily integrating into other programs."
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "include/*", "src/*", "CMakeLists.txt", "tinyxmlConfig.cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.defines.append("HAVE_TINYXML")
        self.cpp_info.defines.append("TIXML_USE_STL")
        
        suffix = ""
        if self.settings.build_type == "Debug":
            suffix = "_d"
        self.cpp_info.libs.append("tinyxml%s" % (suffix,))

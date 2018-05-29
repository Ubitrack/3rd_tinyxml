cmake_minimum_required(VERSION 3.3)
set(TINYXML_LIBRARY tinyxml)

project(ubitrack_tinyxml CXX)

include(GNUInstallDirs)

# Version of TINYXML API.
SET( TINYXML_MAJOR_VERSION 2 )
SET( TINYXML_MINOR_VERSION 5 )
SET( TINYXML_BUILD_VERSION 3 )

SET(TINYXML_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/src")

# Version of project.
SET( TINYXML_FULL_VERSION ${TINYXML_MAJOR_VERSION}.${TINYXML_MINOR_VERSION}.${TINYXML_BUILD_VERSION} ) 

# All cpp files for TINYXML
FILE(GLOB TINYXML_SRCS RELATIVE "${CMAKE_CURRENT_SOURCE_DIR}"
   "${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp"
)

# All header files for TINYXML
FILE(GLOB TINYXML_HEADERS RELATIVE "${CMAKE_CURRENT_SOURCE_DIR}"
   "${CMAKE_CURRENT_SOURCE_DIR}/include/*.h"  
)

# TINYXML shared library definition
ADD_LIBRARY(${TINYXML_LIBRARY} STATIC ${TINYXML_SRCS} ${TINYXML_HEADERS})

target_include_directories(${TINYXML_LIBRARY} PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>
    PRIVATE src)

target_compile_definitions(${TINYXML_LIBRARY} PUBLIC  TIXML_USE_STL)

# make the name of debug libraries end in _d.
set_target_properties(${TINYXML_LIBRARY} PROPERTIES DEBUG_POSTFIX "_d" )

# set the version of the library
set_target_properties(${TINYXML_LIBRARY} PROPERTIES VERSION ${TINYXML_FULL_VERSION} )

# set fPIC
set_target_properties(${TINYXML_LIBRARY} PROPERTIES POSITION_INDEPENDENT_CODE ON)

if(WIN32)
  target_compile_definitions(${TINYXML_LIBRARY} PUBLIC "_LIB")
  target_compile_definitions(${TINYXML_LIBRARY} PUBLIC "_CRT_SECURE_NO_DEPRECATE")
endif(WIN32)

set_target_properties(${TINYXML_LIBRARY} PROPERTIES
        OUTPUT_NAME ${TINYXML_LIBRARY}
        ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_INSTALL_LIBDIR}
    )

install(TARGETS ${TINYXML_LIBRARY}
  EXPORT "tinyxmlTargets"
  RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
  LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
  ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
 )

install(DIRECTORY include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

include(CMakePackageConfigHelpers)
write_basic_package_version_file("${CMAKE_CURRENT_SOURCE_DIR}/tinyxmlConfigVersion.cmake"
  VERSION ${TINYXML_FULL_VERSION}
  COMPATIBILITY SameMajorVersion)

install (FILES "tinyxmlConfig.cmake" "tinyxmlConfigVersion.cmake"
  DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/tinyxml)

install(EXPORT ${TINYXML_LIBRARY}Targets
  FILE tinyxmlTargets.cmake
  NAMESPACE tinyxml::
  DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/tinyxml
)



# ----------------------------------------------------------------------------
#  CMake file for tinyxml. See root CMakeLists.txt
#
# ----------------------------------------------------------------------------
set(TINYXML_LIBRARY tinyxml)
SET(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake" )

project(${TINYXML_LIBRARY} CXX)

include_directories("${CMAKE_CURRENT_SOURCE_DIR}/include")

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
set_target_properties(${TINYXML_LIBRARY} PROPERTIES DEFINE_SYMBOL TIXML_USE_STL)

# make the name of debug libraries end in _d.
SET_TARGET_PROPERTIES( ${TINYXML_LIBRARY} PROPERTIES DEBUG_POSTFIX "_d" )

# set the version of the library
SET_TARGET_PROPERTIES( ${TINYXML_LIBRARY} PROPERTIES VERSION ${TINYXML_FULL_VERSION} )

# set fPIC
set_property(TARGET ${TINYXML_LIBRARY} PROPERTY POSITION_INDEPENDENT_CODE ON)

if(WIN32)
  add_definitions("-D_LIB")
  add_definitions("-D_CRT_SECURE_NO_DEPRECATE")
endif(WIN32)
add_definitions("-DTIXML_USE_STL")

set_target_properties(${TINYXML_LIBRARY} PROPERTIES
        OUTPUT_NAME ${TINYXML_LIBRARY}
        DEBUG_POSTFIX "${UBITRACK_DEBUG_POSTFIX}"
        ARCHIVE_OUTPUT_DIRECTORY ${3P_LIBRARY_OUTPUT_PATH}
    )

install(TARGETS ${TINYXML_LIBRARY}
  EXPORT library_targets
  RUNTIME DESTINATION bin
  LIBRARY DESTINATION lib
  ARCHIVE DESTINATION lib
  INCLUDES DESTINATION include
 )

install(EXPORT library_targets
  NAMESPACE ubitrack_tinyxml::
  DESTINATION lib/cmake/ubitrack_tinyxml)

install(FILES ubitrack_tinyxml-config.cmake
  DESTINATION lib/cmake/ubitrack_tinyxml
)



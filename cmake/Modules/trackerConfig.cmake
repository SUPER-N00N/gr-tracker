INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_TRACKER tracker)

FIND_PATH(
    TRACKER_INCLUDE_DIRS
    NAMES tracker/api.h
    HINTS $ENV{TRACKER_DIR}/include
        ${PC_TRACKER_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    TRACKER_LIBRARIES
    NAMES gnuradio-tracker
    HINTS $ENV{TRACKER_DIR}/lib
        ${PC_TRACKER_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(TRACKER DEFAULT_MSG TRACKER_LIBRARIES TRACKER_INCLUDE_DIRS)
MARK_AS_ADVANCED(TRACKER_LIBRARIES TRACKER_INCLUDE_DIRS)


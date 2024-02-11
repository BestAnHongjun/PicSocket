# Copyright (C) 2024 Coder.AN
# Email: an.hongjun@foxmail.com
# Page: www.anhongjun.top
cmake_minimum_required(VERSION 2.6)

project(PicSocket)

# Set include dir
include_directories(include)

# Set C++11 standard
add_definitions(-std=c++11)

# add 3rdparty library
find_package(OpenCV)
include_directories(${OpenCV_INCLUDE_DIRS})
find_package(JPEG REQUIRED)
include_directories(${JPEG_INCLUDE_DIR})

add_library(picsocket
    source/network.cpp
    source/udp_sender.cpp
    source/udp_receiver.cpp
    source/opencv.cpp
    source/pic_socket.cpp
)
target_link_libraries(picsocket 
    pthread
    ${OpenCV_LIBS}
    ${JPEG_LIBRARIES}
)

# install config
if (NOT DEFINED INSTALL_DIR)
    set(INSTALL_DIR ${CMAKE_CURRENT_SOURCE_DIR}/install)
endif()
set(INSTALL_INCLUDE_DIR ${INSTALL_DIR}/include)
set(INSTALL_LIB_DIR ${INSTALL_DIR}/lib)
set(INSTALL_CMAKE_DIR ${INSTALL_DIR}/cmake)

install(FILES
    ${CMAKE_CURRENT_SOURCE_DIR}/include/udp.h
    DESTINATION
    ${INSTALL_INCLUDE_DIR})
install(FILES
    ${CMAKE_CURRENT_SOURCE_DIR}/include/network.h
    DESTINATION
    ${INSTALL_INCLUDE_DIR})
install(FILES
    ${CMAKE_CURRENT_SOURCE_DIR}/include/blocking_queue.h
    DESTINATION
    ${INSTALL_INCLUDE_DIR})
install(FILES
    ${CMAKE_CURRENT_SOURCE_DIR}/include/opencv.h
    DESTINATION
    ${INSTALL_INCLUDE_DIR})
install(FILES
    ${CMAKE_CURRENT_SOURCE_DIR}/include/pic_socket.h
    DESTINATION
    ${INSTALL_INCLUDE_DIR})
install(TARGETS picsocket DESTINATION ${INSTALL_LIB_DIR})

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/example 
        DESTINATION ${INSTALL_DIR})

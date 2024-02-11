# Copyright (C) 2024 Coder.AN
# Email: an.hongjun@foxmail.com
# Page: www.anhongjun.top
cmake_minimum_required(VERSION 2.6)

project(PicSocket-Example)

# add 3rdparty library
find_package(OpenCV)
include_directories(${OpenCV_INCLUDE_DIRS})
find_package(JPEG REQUIRED)
include_directories(${JPEG_INCLUDE_DIR})

# Set include & lib dir
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../include)
link_directories(${CMAKE_CURRENT_SOURCE_DIR}/../lib)

# Set C++11 standard
add_definitions(-std=c++11)

add_executable(picsocket_sender picsocket_sender.cpp)
target_link_libraries(picsocket_sender 
    picsocket
    pthread
    ${OpenCV_LIBS}
    ${JPEG_LIBRARIES}
)

add_executable(picsocket_receiver picsocket_receiver.cpp)
target_link_libraries(picsocket_receiver
    picsocket
    pthread
    ${OpenCV_LIBS}
    ${JPEG_LIBRARIES}
)

# Copyright (C) 2024 Coder.AN
# Email: an.hongjun@foxmail.com
# Page: www.anhongjun.top

cmake_minimum_required(VERSION 2.8.3)
project(PicSocket-Python-Wrapper)

# include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../include)
# link_directories(${CMAKE_CURRENT_SOURCE_DIR}/../lib/cpp/${ARCH})
# file(GLOB_RECURSE sources "cpp/*.cpp")

# set(EXTRA_LIBS -pthread rt m libunitree_legged_sdk.a)
# set(CMAKE_CXX_FLAGS "-O3 -no-pie")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -O3 -fPIC")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}  -O3 -fPIC")
set(CMAKE_CXX_STANDARD 11)
# python
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/lib/) # .so .dylib

add_subdirectory(3rdparty/pybind11-2.11)
pybind11_add_module(_picsocket python_interface.cpp)
target_link_libraries(_picsocket
    picsocket
)

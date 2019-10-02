cmake_minimum_required(VERSION 2.8)
project(MyHello CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_library(logger logger.cpp)
target_include_directories(logger PRIVATE ${CONAN_INCLUDE_DIRS})

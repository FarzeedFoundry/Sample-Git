cmake_minimum_required(VERSION 3.9)

set (CMAKE_CXX_STANDARD 11)
set (CXX_STANDARD_REQUIRED)

project (TestLibrary)

add_library (TestLibrary STATIC TestLibrary.cpp)

set_target_properties (TestLibrary PROPERTIES PUBLIC_HEADER TestLibrary.h)


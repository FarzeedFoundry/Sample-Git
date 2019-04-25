cmake_minimum_required(VERSION 3.9)
 
set (CMAKE_CXX_STANDARD 11)
set (CXX_STANDARD_REQUIRED)
 
project(MyTestPackage)

add_library(MyTestPackage STATIC MyTestPackage.cpp )
 
#set_target_properties(MyTestPackage PROPERTIES PUBLIC_HEADER MyTestPackage.h)

configure_file( TestLibraryPackConfig.cmake.in TestLibraryConfig.cmake @ONLY )

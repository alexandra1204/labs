

cmake_minimum_required(VERSION 3.28.3)
project(ConsoleApplication9)
set(SFML_DIR "D:/SFML-2.6.1/lib/cmake/SFML")
find_package(SFML 2.6.1 COMPONENTS system window graphics audio REQUIRED)
add_executable(ConsoleApplication9 ConsoleApplication9.cpp)
target_link_libraries(ConsoleApplication9 sfml-system sfml-window sfml-graphics sfml-audio)
file(GLOB FILES "assets/*")
file(COPY ${FILES} DESTINATION "Debug/")
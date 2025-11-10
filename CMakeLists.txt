cmake_minimum_required(VERSION 3.15)
project(FirstProject)

# Imposta lo standard C++ (puoi cambiare 17 in 20 se vuoi)
set(CMAKE_CXX_STANDARD 17)

# Aggiunge l'eseguibile: nome "FirstProject" e sorgente "src/main.cpp"
add_executable(FirstProject src/main.cpp)

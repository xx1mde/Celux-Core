@echo off
mkdir "../../bin"
gcc ^
-shared ^
widgets.c window.c ^
-O3 -s ^
-o ../../bin/ACI.dll ^
-LM:/System/OpenGL/glfw/lib-mingw-w64 -lglfw3 -lgdi32
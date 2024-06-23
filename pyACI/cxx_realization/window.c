// --------------- Absolutely Controlled Interface: ACI --------------- //

#include "includes/include_base.h"
#include "includes/include_windows.h"

__declspec(dllexport) bool _test() {return true;}

void ACIWindowProperties(bool ARRAY_STATES[2]) {
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);

	int ARRAY_PROPERTIES[2] = {0x00020003, 0x00020005};
	for (uint16_t _x = 0; _x < 2; _x++) {
		glfwWindowHint(ARRAY_PROPERTIES[_x], ARRAY_STATES[_x]);
	}
}

__declspec(dllexport) __attribute__((fastcall)) void* ACIWinCreate(float width, float height, char* winname, bool ARRAY_STATES[2]) {
	if (!glfwInit()) {return NULL;}
	else {
		ACIWindowProperties(ARRAY_STATES);
		const GLFWvidmode* mode = glfwGetVideoMode(glfwGetPrimaryMonitor());
		GLFWwindow* GLFW_WINDOW = glfwCreateWindow(mode->width * width, mode->height * height, winname, NULL, NULL);
		if (!GLFW_WINDOW) {
			glfwTerminate(); return NULL;
		}
		else {
			glfwMakeContextCurrent(GLFW_WINDOW); return GLFW_WINDOW;
		}
	}
}

__declspec(dllexport) __attribute__((fastcall)) bool ACIWinCloseEvent(GLFWwindow *GLFW_WINDOW) {return glfwWindowShouldClose(GLFW_WINDOW);}
__declspec(dllexport) void ACIEventHandler() {glfwPollEvents();}
__declspec(dllexport) __attribute__((fastcall)) void ACIUpdateScreen(GLFWwindow *GLFW_WINDOW) {glfwSwapInterval(1); glfwSwapBuffers(GLFW_WINDOW);}
__declspec(dllexport) void ACIWinDestruct() {glfwTerminate();}
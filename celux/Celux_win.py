# --------------- Celeriter Lux Core: Celux --------------- #

import ctypes
import sys, os, time
from .functions import Logger
from .structures import WIN_CLASS

class GLFWwindow(ctypes.Structure): pass

class Celux_win(object):

	TITLE = "App"
	SIZE = (800, 500)
	RESIZABLE = True
	BORDER = True
	MAXIMIZED = False
	BGCOLOR = (1, 1, 1, 0)

	def __init__(self, *args, **kwargs):

		self.__start = time.time()
		setattr(WIN_CLASS, "WIN_PY_OBJ", self)

		try:
			self.__MainDLL = ctypes.CDLL(os.path.abspath(f"{os.getcwd()}/bin/celux.dll")); Logger.stdout("Loaded celux.dll")
		except Exception as e:
			Logger.stderr(f"Not loaded celux.dll. Error: {e}"); sys.exit(0)

	# -- Window Events -- #

	def on_start(self): pass
	def on_close(self): pass

	# -- Build Window -- #

	def build(self) -> None:

		self.on_start()
		self.__GetSystemMetrics = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(("GetSystemMetrics", ctypes.windll.user32))
		self.__ContextErr = ctypes.CFUNCTYPE(ctypes.c_int)(("ContextErr", self.__MainDLL))

		# -- Create prototype <CeluxWinCreate> && call this -- #

		self.__Window = ctypes.CFUNCTYPE(
			ctypes.c_void_p,
			ctypes.c_float,
			ctypes.c_float,
			ctypes.c_char_p,
			ctypes.c_bool * 3)(("CeluxWinCreate", self.__MainDLL))(
				round((1 / (self.__GetSystemMetrics(0x0) / self.SIZE[0])), 4),
				round((1 / (self.__GetSystemMetrics(0x1) / self.SIZE[1])), 4),
				self.TITLE.encode("utf-8"), (ctypes.c_bool * 3)(self.RESIZABLE, self.BORDER, self.MAXIMIZED))

		if self.__Window != None:

			# -- Set window object to dynamic class -- #
			
			setattr(WIN_CLASS, "WIN_C_PTR", ctypes.cast(self.__Window, ctypes.POINTER(GLFWwindow)))
			Logger.stdout(f"Window initialized, <CeluxWinCreate> returned GLFW_WINDOW | addr: 0x{self.__Window} | crtd_time: {round(time.time() - self.__start, 4)}s")
			self.__run()

		else: Logger.stderr(f"Window init failed, <CeluxWinCreate> returned {self.__Window}. Error: {self.__ContextErr()}")

	def __close(self):

		self.on_close()

		# -- destruct window object -- #

		ctypes.CFUNCTYPE(None)(("CeluxWinDestruct", self.__MainDLL))()
		Logger.stdout("Window closed")

	def __run(self, *args, **kwargs) -> None:

		Logger.stdout("Start event cycle")

		# -- create prototypes function | all: [__attribute__((hot))] -- #

		self.__CloseEvent = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.POINTER(GLFWwindow))(("CeluxWinCloseEvent", self.__MainDLL))
		self.__EventHandler = ctypes.CFUNCTYPE(None)(("CeluxEventHandler", self.__MainDLL))
		self.__UpdateScreen = ctypes.CFUNCTYPE(None, ctypes.POINTER(GLFWwindow))(("CeluxUpdateScreen", self.__MainDLL))
		self.__InitGraphics = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.POINTER(GLFWwindow))(("InitGraphics", self.__MainDLL))
		self.__SetBGColor = ctypes.CFUNCTYPE(None, ctypes.c_float * 4)(("SetBGColor", self.__MainDLL))

		Logger.stdout(f"OpenGL status: {self.__InitGraphics(getattr(WIN_CLASS, 'WIN_C_PTR'))}")

		while not self.__CloseEvent(getattr(WIN_CLASS, "WIN_C_PTR")):
			self.__SetBGColor((ctypes.c_float * 4)(*self.BGCOLOR))
			self.__EventHandler()
			self.__UpdateScreen(getattr(WIN_CLASS, "WIN_C_PTR"))

		self.__close()
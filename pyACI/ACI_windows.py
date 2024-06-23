# --------------- Absolutely Controlled Interface: ACI --------------- #

import ctypes
import sys, os
from .functions import Logger
from .WindowStructure import WindowStructure

class GLFWwindow(ctypes.Structure): pass

class ACI_window(object):

	FLAGS = {
		"RESIZABLE": False,
		"BORDER": True,
	}

	def __init__(self, *args, **kwargs):
		try:
			self.ACI_DLL = ctypes.CDLL(os.path.abspath(f"{os.path.dirname(sys.argv[0])}/bin/ACI.dll"))
			Logger("Loaded ACI.dll")
		except Exception as e:
			Logger(f"[ERR] Not loaded ACI.dll. error: {e}")
			sys.exit(0)

	def build(self, width: int, height: int, winname: bytes, type_size: str = "static") -> None:

		from win32api import GetSystemMetrics

		self.__Window = ctypes.CFUNCTYPE(
			ctypes.c_void_p,
			ctypes.c_float,
			ctypes.c_float,
			ctypes.c_char_p,
			ctypes.c_bool * 2)(("ACIWinCreate", self.ACI_DLL))(
				round((1 / (GetSystemMetrics(0x0) / width)), 4),
				round((1 / (GetSystemMetrics(0x1) / height)), 4), winname.encode("utf-8"), (ctypes.c_bool * 2)(*list(self.FLAGS.values())))

		if self.__Window != None:
			setattr(WindowStructure, "WINOBJ", ctypes.cast(self.__Window, ctypes.POINTER(GLFWwindow)))
			Logger(f"Window initialized, <ACIWinCreate> returned GLFW_WINDOW: 0x{self.__Window}")
			self.run()
		else: Logger(f"Window init failed, <ACIWinCreate> returned {self.__Window}")

	def close(self):
		ctypes.CFUNCTYPE(None)(("ACIWinDestruct", self.ACI_DLL))()
		Logger("Window closed")

	def run(self, *args, **kwargs) -> None:

		Logger("Start event cycle")

		self.CloseEvent = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.POINTER(GLFWwindow))(("ACIWinCloseEvent", self.ACI_DLL))
		self.EventHandler = ctypes.CFUNCTYPE(None)(("ACIEventHandler", self.ACI_DLL))
		self.UpdateScreen = ctypes.CFUNCTYPE(None, ctypes.POINTER(GLFWwindow))(("ACIUpdateScreen", self.ACI_DLL))

		while not self.CloseEvent(getattr(WindowStructure, "WINOBJ")):
				self.EventHandler()
				self.UpdateScreen(getattr(WindowStructure, "WINOBJ"))

		self.close()
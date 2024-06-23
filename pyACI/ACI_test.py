import ctypes

class DLLMain_Test(object):
	def __init__(self, DIR: str, **kwargs):
		self.DLLFunction_Test = ctypes.CDLL(f"{DIR}/pyACI/bin/ACI")._test
		self.DLLFunction_Test.restype = ctypes.c_bool

	def __call__(self, *args, **kwargs): print(f"C-backend status: {self.DLLFunction_Test()}")
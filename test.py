from pyACI import Window

class WinMain(Window):
	def __init__(self, *args, **kwargs):
		super(WinMain, self).__init__(*args, **kwargs)

		self.FLAGS["RESIZABLE"] = False
		self.FLAGS["BORDER"] = True

if __name__ == "__main__": WinMain().build(800, 500, "test app")
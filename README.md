--------------- Absolutely Controlled Interface: ACI ---------------

ACI provides a lightweight interface with the possibility of maximum customization. Written in C using GLFW + OpenGL. Has a Python wrapper. In developing.

To use, place the bin directory at the root of your project.

Example:

```python
from pyACI import Window
from pyACI.structures import WIN_CLASS
from pyACI.functions import Logger

Logger.FLAG = True

class WinMain(Window):
	def __init__(self, *args, **kwargs):
		super(WinMain, self).__init__(*args, **kwargs)

		self.RESIZABLE = False
		self.BORDER = True
		self.TITLE = "Test"
		self.BGCOLOR = (0, 0.2, 0.1, 1)

	def on_start(self): pass
	def on_close(self): pass

if __name__ == "__main__":
	WinMain().build()
```

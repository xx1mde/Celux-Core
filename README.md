--------------- Celeriter Lux Core: Celux ---------------

Celux provides a lightweight interface with the possibility of maximum customization. Written in C using GLFW + OpenGL. Has a Python wrapper. In developing.

To use, place the bin directory at the root of your project.

Example:

```python
from celux import Window
from celux.structures import WIN_CLASS
from celux.functions import Logger

from celux.tools import hex_to_rgba

Logger.FLAG = True

class WinMain(Window):
	def __init__(self, *args, **kwargs):
		super(WinMain, self).__init__(*args, **kwargs)

		self.RESIZABLE = False
		self.SIZE = (900, 500)
		self.BORDER = True
		self.TITLE = "Test"
		self.BGCOLOR = hex_to_rgba("a4afff05", Logger.stderr)

	def on_start(self): pass
	def on_close(self): pass

if __name__ == "__main__":
	WinMain().build()
```

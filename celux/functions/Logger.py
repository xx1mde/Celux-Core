import datetime
from colorama import init, Fore, Style

init(autoreset=True)

Logger = type("Logger", (object, ), {
	"FLAG": True,
	"stdout": lambda self, log: print(f"[LOG][{datetime.datetime.now().strftime('%H:%M:%S')}] -> {log}") if self.FLAG else self.null(),
	"stderr": lambda self, err: print(f"{Style.DIM}{Fore.RED}[ERR][{datetime.datetime.now().strftime('%H:%M:%S')}] -> {err}") if self.FLAG else self.null(),
	"null": lambda self: self,
	})()
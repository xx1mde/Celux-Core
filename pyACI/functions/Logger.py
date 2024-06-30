import datetime

Logger = type("Logger", (object, ), {
	"FLAG": True,
	"stdout": lambda self, log: print(f"[LOG][{datetime.datetime.now().strftime('%H:%M:%S')}] -> {log}") if self.FLAG else self.null(),
	"null": lambda self: self,
	})()
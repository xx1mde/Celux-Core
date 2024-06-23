import datetime

def Logger(log: str) -> None: print(f"[LOG][{datetime.datetime.now().strftime('%H:%M:%S')}] -> {log}")
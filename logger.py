from datetime import datetime

class Logger:

    @staticmethod
    def log(message):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")
from datetime import datetime

class Logger:
    def __init__(self, log_file="activity.log"):
        """
        Initialize the logger with a log file.
        :param log_file: str
        """
        self.log_file = log_file

    def log(self, message):
        """
        Log a message with a timestamp.
        :param message: str
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a") as file:
            file.write(f"[{timestamp}] {message}\n")

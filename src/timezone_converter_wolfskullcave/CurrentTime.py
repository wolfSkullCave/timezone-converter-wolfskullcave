from datetime import datetime
import pytz


class CurrentTime:
    def __init__(self, timezone="UTC"):
        """
        Initialize the CurrentTime class with a default timezone.
        Args:
            timezone (str): The timezone to use (default is "UTC").
        """
        self.timezone = timezone
        

    def get_current_time(self):
        """
        Get the current time in the specified timezone.
        Returns:
            str: The current time as a formatted string.
        """
        try:
            tz = pytz.timezone(self.timezone)
            current_time = datetime.now(tz)
            return current_time.strftime("%Y-%m-%d | %H:%M:%S")
        except pytz.UnknownTimeZoneError:
            raise ValueError(f"Unknown timezone: {self.timezone}")

import json


class TimezoneLoader:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path
        self.timezones = None

    def load_timezones(self):
        """Load the JSON file and store the data."""
        try:
            with open(self.json_file_path, "r") as file:
                self.timezones = json.load(file)
        except FileNotFoundError:
            print(f"Error: File not found at: {self.json_file_path}.")

    def find_timezone(self, timezone):
        return type(self.timezones)

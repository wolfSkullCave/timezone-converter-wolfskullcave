from pathlib import Path
from CurrentTime import CurrentTime
from TimezoneLoader import TimezoneLoader

if __name__ == "__main__":
    
    # Construct the path to the JSON file
    json_path = Path(__file__).resolve().parent.parent.parent / "data" / "utc_values.json"
    
    # Create and instance of TimezoneLoader
    loader = TimezoneLoader(json_path)
    
    # Load the timezones
    loader.load_timezones()

    timezone = "asia/tokyo".capitalize()
    
    # print(loader.timezones)
    
    
    
    
    time_obj = CurrentTime(timezone)
    print(time_obj.get_current_time())

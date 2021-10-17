from dotenv import load_dotenv
from lifx_accessor import start_sunrise

# Load dotenv files
load_dotenv()

# Init DB tables
from util import db

if __name__ == "__main__":
    rows = db.get_events_api_key()

    if len(rows) > 0:
        (id, api_key) = rows.pop()

        print("Event with id:", id, "and api_key:", api_key)

        db.delete_events(id)

        print("Deleted stored event!")

        start_sunrise(api_key)  

        print("Finished executing the scheduler!")  
    else:
        print("No events to execute!")


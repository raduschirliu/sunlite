from dotenv import load_dotenv

from lifx_accessor import start_sunrise

# Load dotenv files
load_dotenv()

# Init DB tables
from util import db

if __name__ == "__main__":
    rows = db.get_events_api_key()

    if len(rows) > 0:
        event = rows.pop()
        # event = (id, api_key) 

        db.delete_events(event[0])
        start_sunrise(event[1])    
    else:
        print("No events to execute!")


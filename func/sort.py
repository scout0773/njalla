import json
from datetime import datetime

def sort(available, domain):
    sort = sorted(available, key=lambda x: x['domain'])
    date = datetime.now().strftime("%m%d%Y")
    filename = f"available_{domain}_{date}.json"
    with open(filename, 'w') as file:
        json.dump(sort, file, indent=4)
import json

def sort(available):
    sort = sorted(available, key=lambda x: x['domain'])
    with open('available.json', 'w') as file:
        json.dump(sort, file, indent=4)
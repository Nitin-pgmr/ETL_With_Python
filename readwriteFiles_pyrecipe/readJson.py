from faker import Faker
import json
with open("data.JSON","r") as f:
    data = json.load(f)
    print(data['records'][0]['name'])

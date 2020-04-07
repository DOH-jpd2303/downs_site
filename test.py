import os
import json

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(dir, "Keys/downs_site_key.txt")) as json_file:
	dat = json.load(json_file)
	SECRET_KEY = dat["SECRET_KEY"]
print(SECRET)

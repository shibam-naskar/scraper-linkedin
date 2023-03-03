from linkedin_api import Linkedin
import json

api = Linkedin('shibam.naskar@tikaj.com', 'Shibam@2000')

username = "dee-gupta"

# profile = api.get_profile(username)
data = api.get_company(username)
# activity = api.get_ac('sanketghosh0809')

# print()

# with open(f"profile.json", "w") as outfile:
#     outfile.write(json.dumps(profile, indent=4))

# with open(f"posts.json", "w") as outfile:
#     outfile.write(json.dumps(posts, indent=4))

print(data)
from linkedin_api import Linkedin
import json

api = Linkedin('shibam.naskar@tikaj.com', 'Shibam@2000')

username = "dee-gupta"

profile = api.get_profile(username)
posts = api.get_profile_posts(username)
contactinfo = api.get_profile_contact_info(username)
# activity = api.get_ac('sanketghosh0809')

# print()

with open(f"profile.json", "w") as outfile:
    outfile.write(json.dumps(profile, indent=4))

with open(f"posts.json", "w") as outfile:
    outfile.write(json.dumps(posts, indent=4))

with open(f"contactinfo.json", "w") as outfile:
    outfile.write(json.dumps(contactinfo, indent=4))

print("DONE")
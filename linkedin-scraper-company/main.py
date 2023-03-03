from linkedin_api import Linkedin
import json

api = Linkedin('shibam.naskar@tikaj.com', 'Shibam@2000')

username = "tikaj"

profile = api.get_company(username)
updates =   api.get_company_updates(username)
# posts = api.get_profile_posts(username)
# contactinfo = api.get_profile_contact_info(username)
# activity = api.get_ac('sanketghosh0809')

# print()

with open(f"company.json", "w") as outfile:
    outfile.write(json.dumps(profile, indent=4))

with open(f"updates.json", "w") as outfile:
    outfile.write(json.dumps(updates, indent=4))

# with open(f"contactinfo.json", "w") as outfile:
#     outfile.write(json.dumps(contactinfo, indent=4))

print("DONE")
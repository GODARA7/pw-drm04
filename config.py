import os

API_ID = API_ID =  28590119

API_HASH = os.environ.get("API_HASH", "2494557bf21e6c5152f26070aa1a97c7")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7438WUOcaY3BUBBdxOgwPUCQ")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 548326071))

LOG = -100217824809,

# UPDATE_GRP = -1002140332321, # bot sat group

# auth_chats = [5219193259,1327415906]

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1782965867").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)



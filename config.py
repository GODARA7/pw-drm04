import os

API_ID = API_ID =  26512964

API_HASH = os.environ.get("API_HASH", "e5d187c6c7a0919ccb8866f76f655701")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7916334119:AAFAsGnwdtO_o8NQbMFR-iHbzkwObyHvWLI")

PASS_DB = int(os.environ.get("PASS_DB", "mongodb+srv://sujay5372192:sujay5372192@cluster00001.zivqq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster00001"))

OWNER = int(os.environ.get("OWNER", 7246728595))

LOG = -4679498951,

# UPDATE_GRP = -4679498951, # bot sat group

# auth_chats = [7246728595]

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7246728595").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)



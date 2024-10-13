# firebase - backend as a service, BaaS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('C:\\Users\\steve\\git_repo\\MIT_Course\\Module12\\Activity_12_5_firebase\\serviceAccountKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://activity12-5-b54a0-default-rtdb.firebaseio.com/'
})

# save data
ref = db.reference('Mariners/')
player_ref = ref.child('Players')
player_ref.set({
    'CalRaleigh': {
        'position': 'C',
        'home runs': 24,
        'batting avg': .214
    },
    'LukeRaley': {
        'position': 'LF',
        'home runs': 14,
        'batting avg': .233
    }
})

# update data
raley_ref = player_ref.child('LukeRaley')
raley_ref.update({
    'RBIs': 36
})

# # read data
# handle = db.reference('py/users/alanisawesome')

# # Read the data at the posts reference (this is a blocking operation)
# print(ref.get())
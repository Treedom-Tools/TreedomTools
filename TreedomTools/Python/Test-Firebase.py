from google.cloud import firestore
from Users.volunteer import Volunteer
from Firebase import db_functions

FIREBASE_KEY_PATH = "C:/Users/Treedom/Desktop/treedom-tools-firebase-adminsdk-xn36r-5f0eda3b35.json"
db = firestore.Client.from_service_account_json(FIREBASE_KEY_PATH)

# response_dict = db_functions.add_document('volunteers',Volunteer("Test user flow to phone",26).to_dict())
# print(response_dict)

db_functions.delete_document('volunteers/soespaBUm8FTn1NKsiSL')
# print(response_dict)

# new_volunteer_ref = db.collection('volunteers').document(None)
# new_volunteer_ref.set(
#     Volunteer("New user flow test",25).to_dict()
# )
# print(new_volunteer_ref.id)
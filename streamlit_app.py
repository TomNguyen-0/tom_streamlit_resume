import streamlit as st

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
import json


TABLE_NAME = 'resume'
DATABASE_URL = 'https://tomresume2024-default-rtdb.firebaseio.com'
TOKEN_FILE_NAME = 'token.json'

# # Use a service account.
# ## step 1 initializing to the database
# @st.experimental_singleton #[2]
def write_to_db():
    user_dict = st.experimental_user.to_dict() #[3]
    
    if credentials._is_file_path(TOKEN_FILE_NAME):
        with open(TOKEN_FILE_NAME) as json_file:
            json_data = json.load(json_file)
            json_data['private_key'] = st.secrets["private_key"]
            json_data['private_key_id'] = st.secrets["private_key_id"]
            json_data['client_id'] = st.secrets["client_id"]
            json_data['project_id'] = st.secrets["project_id"]
        cred = credentials.Certificate(json_data)


    try:
        app = firebase_admin.initialize_app(cred, {'databaseURL': DATABASE_URL})
    except ValueError as e:
        pass    
    ref = db.reference(TABLE_NAME)
    if user_dict.get("email", None) is not None:    
        if user_dict.get("email") == "":
            user_dict["email"] = "no email"
        if user_dict.get("email") == "test@test.com":
            user_dict["email"] = "streamlit community cloud"
            return None
        emp_ref = ref.push({
            'name': user_dict.get("email", None)
            ,'age': 299
            ,'email': 'jkj'
        })


write_db = write_to_db()

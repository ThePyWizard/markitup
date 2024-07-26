import pyrebase

# Firebase configuration
firebaseConfig = {
  'apiKey': "AIzaSyDzM1cAArVjFor_67PwZY1tnf4-s7LHun0",
  'authDomain': "markitup-1d4ec.firebaseapp.com",
  'projectId': "markitup-1d4ec",
  'storageBucket': "markitup-1d4ec.appspot.com",
  'messagingSenderId': "35010555468",
  'appId': "1:35010555468:web:b3a93e222d235fde874ee9",
  'measurementId': "G-BJF8VVZJJL"
}

# Initialize Pyrebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def sign_in(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return user
    except Exception as e:
        return None

def sign_up(email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        return user
    except Exception as e:
        return None

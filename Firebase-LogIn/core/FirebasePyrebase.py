import pyrebase
from getpass import getpass
import json

class FirebaseErrorDecryptor:
    def __init__(self, error_json):
        self.error_json = error_json
        if type(self.error_json) == str: # If error_json is a string, convert it to a dictionary
            self.error_json = json.loads(self.error_json)

    def get_error_code(self):
        try:
            return self.error_json['error']['code']
        except (KeyError, TypeError):
            return None

    def get_error_message(self):
        try:
            return self.error_json['error']['message']
        except (KeyError, TypeError):
            return None

    def get_error_details(self):
        try:
            return self.error_json['error']['errors']
        except (KeyError, TypeError):
            return None

    def decrypt_error(self):
        error_code = self.get_error_code()
        error_message = self.get_error_message()
        error_details = self.get_error_details()

        decrypted_error = {
            'code': error_code,
            'message': error_message,
            'details': error_details
        }

        return decrypted_error


class FirebaseAuth:
    def __init__(self, config):
        self.firebase = pyrebase.initialize_app(config)
        self.auth = self.firebase.auth()
        self.db = self.firebase.database()

    def handle_error(self, e):
        error_json = e.args[1]
        error_decryptor = FirebaseErrorDecryptor(error_json)
        decrypted_error = error_decryptor.decrypt_error()

        print("Error Details:")
        print(f"Code: {decrypted_error['code']}")
        print(f"Message: {decrypted_error['message']}")

    def sign_up(self, email, password):
        try:
            user = self.auth.create_user_with_email_and_password(email, password)
            # self.auth.send_email_verification(user['idToken'])

            # Create a Firestore document for the user in the "Users" collection
            user_data = {"email": email, "isAdmin": False}  # Add any additional user data
            self.db.child("Users").child(user['localId']).set(user_data)

            return user
        except Exception as e:
            self.handle_error(e)

    def log_in(self, email, password):
        try:
            user = self.auth.sign_in_with_email_and_password(email, password)
            
            # print all the user data that is being stored in the firestore db
            user_data = self.db.child("Users").child(user['localId']).get().val()
            print(user_data)

            return user
        except Exception as e:
            self.handle_error(e)

    def reset_password(self, email):
        try:
            self.auth.send_password_reset_email(email)
            print("Password email was sent successfully!")
        except Exception as e:
            self.handle_error(e)

def main():
    firebase_config = {
        'apiKey': "AIzaSyAXwedjTVeDM_Ct3jAK3CzvMGt4FD8DrrM",
        'authDomain': "userform-91a91.firebaseapp.com",
        'databaseURL': "https://userform-91a91-default-rtdb.europe-west1.firebasedatabase.app",
        'projectId': "userform-91a91",
        'storageBucket': "userform-91a91.appspot.com",
        'messagingSenderId': "501153405994",
        'appId': "1:501153405994:web:5d9f87ebb7165c9d03b753",
        'measurementId': "G-S7SC7LDX1W"
    }

    firebase_auth = FirebaseAuth(firebase_config)

    email = input("Enter your email: ")
    password = getpass("Enter your password: ")

    # # Sign Up
    # user = firebase_auth.sign_up(email, password)
    # if user:
    #     print("Successfully created user account with uid:", user['localId'])

    # Log In
    user = firebase_auth.log_in(email, password)
    if user:
        print("Successfully logged in with uid:", user['localId'])

def test():
    error_json = {
        "error": {
            "code": 400,
            "message": "EMAIL_NOT_FOUND",
            "errors": [
                {
                    "message": "EMAIL_NOT_FOUND",
                    "domain": "global",
                    "reason": "invalid"
                }
            ]
        }
    }

    error_decryptor = FirebaseErrorDecryptor(error_json)
    decrypted_error = error_decryptor.decrypt_error()

    print("Decrypted Error:")
    print(decrypted_error['code'])

if __name__ == "__main__":
    main()
    # test()
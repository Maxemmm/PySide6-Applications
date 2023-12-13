import firebase_admin
from firebase_admin import credentials, auth
from firebase_admin import exceptions

def initialize_app(path_to_service_account):
    cred = credentials.Certificate(path_to_service_account)
    firebase_admin.initialize_app(cred)

def signup(email, password):
    try:
        user = auth.create_user(email=email, password=password)
        print(f"User {user.uid} created successfully")
    except exceptions.FirebaseError as e:
        print(f"Error creating user: {e}")

def login(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print(f"User {user['email']} successfully logged in")

        # Generate a custom token for the user
        custom_token = auth.create_custom_token(user['localId'], {'isAdmin': True})
        return custom_token
    except exceptions.FirebaseError as e:
        print(f"Error logging in: {e}")
        return None

def verify_token(token):
    try:
        decoded_token = auth.verify_id_token(token)
        user_id = decoded_token['uid']
        user = auth.get_user(user_id)
        print(f"Token verified for user {user.email}")
        return user
    except exceptions.FirebaseError as e:
        print(f"Error verifying token: {e}")
        return None

if __name__ == "__main__":
    service_account_path = "C:\\Users\\maxim\\Documents\\Visual Studio Code\\serviceAccountKey.json"

    # Initialize the Firebase app
    initialize_app(service_account_path)

    # Example: Signup
    signup('example@example.com', 'password123')

    # Example: Login
    custom_token = login('example@example.com', 'password123')

    # Example: Verify Token
    if custom_token:
        user = verify_token(custom_token)
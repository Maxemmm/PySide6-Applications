import firebase_admin
from firebase_admin import credentials, firestore
import secrets

class LicenseKeyGenerator:
    @staticmethod
    def generate_product_id():
        """
        Generate a secure random product ID.
        """
        random_string = ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(24))
        return '-'.join([random_string[i:i+4] for i in range(0, len(random_string), 4)])

    @staticmethod
    def generate_product_key():
        """
        Generate a secure random product key.
        """
        random_string = ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(25))
        return '-'.join([random_string[i:i+5] for i in range(0, len(random_string), 5)])

class LicenseManager:
    def __init__(self, service_account_key_path):
        cred = credentials.Certificate(service_account_key_path)
        firebase_admin.initialize_app(cred)
        self.database = firestore.client()

    def assign_license(self, data): # KO
        # TODO: force assign a license to an account that just registered or inserted product license id or key
        pass

    def check_data(self, data):
        doc_ref = self.database.collection('License').document(data['product_id'])
        return doc_ref.get().exists

    def add_license_data(self, data): # OK
        doc_ref = self.database.collection('License').document(data['product_id'])
        if not doc_ref.get().exists:
            doc_ref.set(data)
            return True
        else:
            return False

    def fetch_license(self, product_id): # OK
        doc_ref = self.database.collection('License').document(product_id)
        doc = doc_ref.get()
        return doc.to_dict() if doc.exists else False

    def remove_license(self, product_id): # OK
        doc_ref = self.database.collection('License').document(product_id)
        doc = doc_ref.get()
        if doc.exists:
            doc_ref.delete()
            return True
        else:
            return False

    def update_max_users(self, product_id, max_users): # OK
        doc_ref = self.database.collection('License').document(product_id)
        doc = doc_ref.get()

        if doc.exists:
            doc_ref.update({'maximum_users': max_users})
            return True
        else:
            return False

    def update_assigned_users(self, product_id, assigned_users): # OK
        doc_ref = self.database.collection('License').document(product_id)
        doc = doc_ref.get()

        if doc.exists:
            doc_ref.update({'assigned_users': assigned_users})
            return True
        else:
            return False

    def get_products_by_license_type(self, license_type):
        docs = self.database.collection('License').where('license_type', '==', license_type).stream()
        return [doc.to_dict() for doc in docs]

def main():
    service_account_key_path = "C:\\Users\\maxim\\Documents\\Visual Studio Code\\serviceAccountKey.json"

    license_manager = LicenseManager(service_account_key_path)

    # generate 8 product licenses 
    for i in range(8):
        product_id = LicenseKeyGenerator.generate_product_id()
        product_key = LicenseKeyGenerator.generate_product_key()
        license_data = {
            'product_id': product_id,
            'product_key': product_key,
            'license_type': 'Beta',
            'maximum_users': 1,
            'assigned_users': 0
        }
        license_manager.add_license_data(license_data)

if __name__ == '__main__':
    main()

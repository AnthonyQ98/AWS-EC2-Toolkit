import get_credentials

class CreateInstance():
    def __init__(self):
        access_key, secret_key = get_credentials.get_creds()
    def create_new_instance(self):
        print("This will create a new instance.")
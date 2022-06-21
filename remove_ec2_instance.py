import get_credentials

class RemoveInstance():
    def __init__(self):
        access_key, secret_key = get_credentials.get_creds()
    def remove_instance(self):
        print("This will delete a new instance.")
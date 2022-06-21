import get_credentials
import boto3

class RemoveInstance():
    def __init__(self):
        self.instance_id = input("Instance ID to delete: ")
        access_key, secret_key = get_credentials.get_creds()
        self.remove_instance()
    def remove_instance(self):
        print(f"Removing instance with the following id: {self.instance_id}")
        ec2 = boto3.resource("ec2")
        ec2.instances.filter(InstanceIds=[self.instance_id]).terminate()
import get_credentials
import boto3

class ListInstances():
    def __init__(self):
        self.list_all_instances()
        access_key, secret_key = get_credentials.get_creds()
    def list_all_instances(self):
        ec2 = boto3.resource("ec2")
        for instance in ec2.instances.all():
            print(f"Instance: {instance}")
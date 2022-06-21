import get_credentials
import boto3

class CreateInstance():
    def __init__(self):
        self.create_new_instance()
        access_key, secret_key = get_credentials.get_creds()
    def create_new_instance(self):
        print("Creating a new instance now...")
        ec2 = boto3.resource("ec2")
        ec2.create_instances(LaunchTemplate={"LaunchTemplateId": "lt-0346088488e6937fe", "Version": "$Latest"}, MinCount=1, MaxCount=1)
        print("Instance created!")
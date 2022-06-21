import subprocess
import sys


def get_creds():
    try:
        access_key = subprocess.getoutput("aws configure get aws_access_key_id")
        secret_key = subprocess.getoutput("aws configure get aws_secret_access_key")
    except:
        print("No AWS Credentials File Found!")
        sys.exit()
    return access_key, secret_key

import create_ec2_instance
import remove_ec2_instance
import sys

if __name__ == '__main__':
    no_arg = "Error: None or invalid option given.\nPlease try the following:\nUsage: main.py [option]\nAvailable Options: create, delete, list\n"
    try:
        if sys.argv[1] == "create":
            print("It is equal create")
        else:
            print("It is not equal create.")
    except:
        print(no_arg)

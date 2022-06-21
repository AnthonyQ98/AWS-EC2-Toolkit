import create_ec2_instance
import remove_ec2_instance
import list_ec2_instances
import sys

def validate_arguments():
    option = sys.argv[1]
    if option == "create":
        print("Attempting to create a new AWS EC2 Instance...")
    elif option == "delete":
        print("You have selected the 'delete' option to remove an AWS EC2 Instance...")
    elif option == "list":
        print("Retrieving all of your existing EC2 instances...")
    else:
        raise invalid_arg
    return option

def conduct_action(selected_option):
    if selected_option == "create":
        instance = create_ec2_instance.CreateInstance()
    elif selected_option == "delete":
        instance = remove_ec2_instance.RemoveInstance()
    else:
        instance = list_ec2_instances.ListInstances()


if __name__ == '__main__':
    no_arg = "Error: None or invalid option given.\nPlease try the following:\nUsage: main.py [option]\nAvailable Options: create, delete, list\n"
    try:
        option = validate_arguments()
    except Exception as invalid_arg:
        print(no_arg)
        sys.exit()
    conduct_action(selected_option=option)


def parse_input(user_input):
    """
    Parse the user input into a command and arguments.

    Args:
        user_input (str): The input string from the user.

    Returns:
        tuple: A tuple containing the command and arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    """
    Add a new contact to the contacts dictionary.

    Args:
        args (list): A list containing the name and phone number.
        contacts (dict): The dictionary to store contacts.

    Returns:
        str: A message indicating the result of the operation.
    """
    if len(args) != 2:
        return "Error: Please provide both name and phone number"
    name, phone = args
    if not phone.isdigit():
        return " Incorrect value"
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    """
    Change the phone number of an existing contact.

    Args:
        args (list): A list containing the name and new phone number.
        contacts (dict): The dictionary to store contacts.

    Returns:
        str: A message indicating the result of the operation.
    """
    name, phone = args
    if not phone.isdigit():
        return "Incorrect value"
    elif name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Name not found"


def show_phone(args, contacts):
    """
    Show the phone number of a contact.

    Args:
        args (list): A list containing the name of the contact.
        contacts (dict): The dictionary to store contacts.

    Returns:
        str: The phone number of the contact or an error message.
    """
    for name, phone in contacts.items():
        if args[0] == name:
            return phone
    return "Name not found"


def sow_all(contacts):
    """
    Show all contacts.

    Args:
        contacts (dict): The dictionary to store contacts.

    Returns:
        dict: The dictionary containing all contacts.
    """
    return contacts


def main():
    """
    The main function to run the assistant bot.
    """
    contacts = {} 
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(sow_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

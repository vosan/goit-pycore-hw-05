from utils import input_error, output


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    return cmd.strip().lower(), *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, _ = args
    add_contact(args, contacts)
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]


def show_all_contacts(contacts):
    if contacts:
        output('=' * 30)
        output("All Contacts:")
        output('=' * 30)
        for name, phone in contacts.items():
            output(f"{name:.<20} {phone}")
        output('=' * 30)
    else:
        output("No contacts available.")


def show_help():
    output("Available commands:")
    output(f"{'add <name> <phone> ':.<30} add a new contact")
    output(f"{'change <name> <phone> ':.<30} change an existing contact")
    output(f"{'phone <name> ':.<30} get the phone number of a contact")
    output(f"{'all ':.<30} show all contacts")
    output(f"{'close ':.<30} exit the program")

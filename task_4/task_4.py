from commands import *
from utils import output, parse_input


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        try:
            match command:
                case "help":
                    output("Available commands:")
                    output(f"{'add <name> <phone> ':.<30} add a new contact")
                    output(f"{'change <name> <phone> ':.<30} change an existing contact")
                    output(f"{'phone <name> ':.<30} get the phone number of a contact")
                    output(f"{'all ':.<30} show all contacts")
                    output(f"{'close ':.<30} exit the program")
                case "close" | "exit" | "end" | "quit" | "stop":
                    output("Good bye!")
                    break
                case "hello" | "hi" | "hey":
                    output("How can I help you?")
                case "add":
                    output(add_contact(args, contacts))
                case "change" | "update":
                    output(change_contact(args, contacts))
                case "phone" | "get":
                    output(f"{show_phone(args, contacts)}")
                case "all":
                    if contacts:
                        output('=' * 30)
                        output("All Contacts:")
                        output('=' * 30)
                        for name, phone in contacts.items():
                            output(f"{name:.<20} {phone}")
                        output('=' * 30)
                    else:
                        output("No contacts available.")

                case _:
                    output(f"Invalid command.")

        except ValueError as e:
            output(f"An error occurred: {e}. Please try again.")


if __name__ == "__main__":
    main()

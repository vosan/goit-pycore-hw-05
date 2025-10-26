from commands import *
from utils import output


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "help":
                show_help()
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
                show_all_contacts(contacts)
            case _:
                output(f"Invalid command.")



if __name__ == "__main__":
    main()

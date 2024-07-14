# , delete_contact
from commands.commands_list import add_contact, change_contact, show_phone, show_all, add_birthday, show_birthday, birthdays
from OOP import AddressBook


def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


book = AddressBook()


def main():
    print("Welcome to the Choco.py assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            show_all(book)

        elif command == "add-birthday":  # ADD BIRTHDAY
            print(add_birthday(args, book))

        elif command == "show-birthday":  # SHOW BIRTHDAY
            print(show_birthday(args, book))

        elif command == "birthdays": # SHOW ALL GREETINGS
            print(birthdays(book))

        elif command in ["close", "exit"]:
            print("Goodbye!")
            break

        # Potentialy useful and practical option:

        # elif command == "delete":
        #     print(delete_contact(args, contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

import json
from pathlib import Path
from typing import List, Dict

from normalize_phone import normalize_phone

PHONEBOOK_FILE = "phonebook.json"


def load_phonebook(filename=PHONEBOOK_FILE) -> List[Dict[str, str]]:
    """Function to load the phonebook from the file.

    __args__:
        None
    __return__:
        phonebook: dict
            The phonebook dictionary
    """
    path = Path(filename)
    try:
        with open(path, "r") as file:
            phonebook = json.load(file)
    except FileNotFoundError:
        phonebook = []
    return phonebook


def save_phonebook(phonebook: List[Dict[str, str]], filename=PHONEBOOK_FILE) -> None:
    """Function to save the phonebook to the file.

    __args__:
        phonebook: dict
            The phonebook dictionary
    __return__:
        None
    """
    path = Path(filename)
    with open(path, "w") as file:
        json.dump(phonebook, file, indent=4)


def add_contact(name: str, phone: str, phonebook: List[Dict[str, str]]) -> None:
    """Function to add a contact to the phonebook.

    __args__:
        name: str
            The name of the contact
        phone: str
            The phone number of the contact
        phonebook: dict
            The phonebook dictionary
    __return__:
        None
    """
    phone = normalize_phone(phone)
    contact = {"name": name, "phone": phone}
    phonebook.append(contact)
    print(f"Contact {name} added.")


def change_contact(name: str, new_phone: str, phonebook: List[Dict[str, str]]) -> None:
    """Function to change the phone number of a contact.

    __args__:
        name: str
            The name of the contact
        new_phone: str
            The new phone number of the contact
        phonebook: dict
            The phonebook dictionary
    __return__:
        None
    """
    new_phone = normalize_phone(new_phone)
    for contact in phonebook:
        if contact["name"] == name:
            contact["phone"] = new_phone
            break
    print(f"Contact {name} updated.\nNew phone: {new_phone}")


def delete_contact(name: str, phonebook: List[Dict[str, str]]) -> None:
    """Function to delete a contact from the phonebook.

    __args__:
        name: str
            The name of the contact
        phonebook: dict
            The phonebook dictionary
    __return__:
        None
    """
    for contact in phonebook:
        if contact["name"] == name:
            phonebook.remove(contact)
            print(f"Contact {name} deleted.")
            break
        else:
            print("Contact not found.")


def search_contact(pattern: str, phonebook: List[Dict[str, str]]) -> None:
    """Function to search for a contact in the phonebook.

    __args__:
        pattern: str
            The search pattern
        phonebook: dict
            The phonebook dictionary
    __return__:
        None
    """

    found = False

    for contact in phonebook:
        if pattern.lower() in contact["name"].lower():
            print(f"{contact['name']}: {contact['phone']}")
            found = True

    if not found:
        print("Contact not found.")


def show_phonebook(phonebook: List[Dict[str, str]], sorted_=True) -> None:
    """Function to pint the phonebook to console.

    __args__:
        phonebook: dict
            The phonebook dictionary
    __return__:
        None
    """
    if sorted_:  # Sort the phonebook by name
        phonebook = sorted(phonebook, key=lambda contact: contact["name"])
    for contact in phonebook:
        print(f"{contact['name']}: {contact['phone']}")


def main(phonebook=None):
    print("Welcome to the assistant bot!")

    if phonebook is None:  # Load the phonebook if not provided
        phonebook = []

    while True:
        command = input("command: ").strip().split()
        command[0] = command[0].lower()

        if command[0] in ["close", "exit"]:
            print("Good bye!")
            break
        elif command[0] == "hello":
            print("How can I help you?")
        elif command[0] == "add":
            if len(command) != 3:
                print("Invalid command.")
                print("Usage: add <name> <phone>")
                continue
            add_contact(command[1], command[2], phonebook)
        elif command[0] == "change":
            if len(command) != 3:
                print("Invalid command.")
                print("Usage: change <name> <phone>")
                continue
            change_contact(command[1], command[2], phonebook)
        elif command[0] == "delete":
            if len(command) != 2:
                print("Invalid command.")
                print("Usage: delete <name>")
                continue
            delete_contact(command[1], phonebook)
        elif command[0] == "search":
            if len(command) != 2:
                print("Invalid command.")
                print("Usage: search <pattern>")
                continue
            search_contact(command[1], phonebook)
        elif command[0] in ["show", "all"]:
            if len(command) == 1 or (len(command) == 2 and command[1] == "all"):
                show_phonebook(phonebook)
            elif len(command) == 2:
                search_contact(command[1], phonebook)
            else:
                print("Invalid command.")
                print("Usage: show [pattern]")
        else:
            print("Invalid command.")
            print("Available commands: hello, add, change, delete, search, show, close, exit")


if __name__ == '__main__':
    phonebook = load_phonebook()
    main(phonebook=phonebook)
    save_phonebook(phonebook)

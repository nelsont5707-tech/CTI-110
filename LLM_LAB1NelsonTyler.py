# Tyler Nelson
# 11/22/2025
# LLM_LAB1
# This program helps you simulate your own password generator program for safer passwords.

import random
import string

def generate_password(length):
    """Generate a random password with letters, digits, and symbols."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(task_name, password, filename="passwords.txt"):
    """Save the task and password to a text file."""
    with open(filename, "a") as file:
        file.write(f"Task: {task_name} | Password: {password}\n")
    print(f"Saved password for '{task_name}' to {filename}.")

def main():
    print("=== Random Password Generator ===")
    while True:
        task_name = input("Enter a website name (or 'q' to quit): ")
        if task_name.lower() == 'q':
            break
        try:
            length = int(input("Enter required password length: "))
            if length <= 0:
                print("Length must be a positive number.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        password = generate_password(length)
        print(f"Generated Password: {password}")
        save_password(task_name, password)
    
    print("Goodbye! All passwords saved.")

if __name__ == "__main__":
    main()

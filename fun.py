'''password type syntax code'''

from getpass import getpass
from pydantic import SecretStr

first_name = input("Enter your name: ")
print(f"Hello {first_name}\n")   # F-strings. Commonly used to fill in variables

secret = SecretStr(getpass("Please tell me a secret: "))
print("Your secret is:", secret)  # Another way to print multiple values. sep=" " is default
print("Your secret value is:", secret.get_secret_value())
"""Main file"""
import sys

from password_generator_service.argument_parser import arg_parser
from password_generator_service.utilities import generate_password

arg_parser()
print("Welcome to the password generator")
print(f"The length you have selected is {sys.argv[2]}")
print(generate_password(password_length=sys.argv[2]))

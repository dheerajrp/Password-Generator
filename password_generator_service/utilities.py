"""
Required methods and functionalities
"""
import logging
import random

from password_generator_service.rules import (LOWER_CASES, UPPER_CASES,
                                              NUMBERS, SYMBOLS,
                                              PASSWORD_LENGTH_ERROR_MSG,
                                              PASSWORD_LENGTH_SUCCESS_MSG,
                                              PASSWORD_CHAR_ERROR_MSG,
                                              PASSWORD_LETTER_ERROR_MSG,
                                              PASSWORD_GENERATION_ERROR_MSG,
                                              PASSWORD_LENGTH_VALUE_ERROR_MSG,
                                              PASSWORD_LENGTH_THRESHOLD)

logging.basicConfig(filename="generate_password.log",
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p'
                    )


def generate_raw_letters() -> str:
    """
    Generates the combination of lower case letters and upper case letters

    Returns:
        str:
            Combination of lower case letters and upper case letters
    """
    try:
        raw_letters = LOWER_CASES + UPPER_CASES
        return raw_letters
    except Exception as _:
        logging.error(PASSWORD_LETTER_ERROR_MSG)


def generate_raw_characters() -> str:
    """
    Generates the combination of numbers and special characters

    Returns:
        str:
            Combination of numbers and special characters
    """
    try:
        raw_characters = NUMBERS + SYMBOLS
        return raw_characters
    except Exception as _:
        logging.error(PASSWORD_CHAR_ERROR_MSG)


def validate_password_length(length: int) -> int:
    """
    Converts the password length into integer

    Args:
        length (int):

    Returns:
        int:
            Length of the password
    """
    try:
        return int(length)
    except ValueError as _:
        logging.error(PASSWORD_LENGTH_VALUE_ERROR_MSG)
        return PASSWORD_LENGTH_VALUE_ERROR_MSG


def generate_password(password_length: str) -> str:
    """
    Generates the password

    Args:
        password_length (str):
            The length of the password.

    Returns:
        str:
            The generated password
    """
    try:
        password_length = int(password_length)
        validate_password_length(length=password_length)
        if password_length >= PASSWORD_LENGTH_THRESHOLD:
            password_letters = "".join(
                random.sample(generate_raw_letters(), int(password_length / 2)))
            password_chars = "".join(random.sample(generate_raw_characters(),
                                                   password_length - int(
                                                       password_length / 2)))
            generated_password = password_letters + password_chars
            logging.info(PASSWORD_LENGTH_SUCCESS_MSG)
            return f"The generated password is {generated_password}"
        else:
            logging.error(PASSWORD_LENGTH_ERROR_MSG)
            return PASSWORD_LENGTH_ERROR_MSG
    except ValueError:
        logging.error(PASSWORD_LENGTH_ERROR_MSG)
        return PASSWORD_LENGTH_ERROR_MSG

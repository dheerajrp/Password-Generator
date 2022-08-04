"""Rules or constants"""
import string

LOWER_CASES = string.ascii_lowercase
UPPER_CASES = string.ascii_uppercase
NUMBERS = string.digits
SYMBOLS = '!@#$%^&*_~'
PASSWORD_LENGTH_THRESHOLD = 8
PASSWORD_LENGTH_MAX = 40
PASSWORD_LENGTH_SUCCESS_MSG = "The password has been generated successfully."

"""Error Messages"""
PASSWORD_LENGTH_ERROR_MSG = "The given password length didn't satisfy the " \
                            "threshold length. The length of the password " \
                            "should be at least " \
                            F"{PASSWORD_LENGTH_THRESHOLD} and at most" \
                            F" {PASSWORD_LENGTH_MAX}"
PASSWORD_LETTER_ERROR_MSG = "Error in generating letters"
PASSWORD_CHAR_ERROR_MSG = "Error in generating characters"
PASSWORD_GENERATION_ERROR_MSG = "Error in generating the password"
PASSWORD_LENGTH_VALUE_ERROR_MSG = "Enter the valid value for password " \
                                  "length."

"""
Argument parser
"""
import argparse


def arg_parser():
    """
    The helper function when the command is given incorrectly

    Returns:
        None:
    """
    parser = argparse.ArgumentParser(
        description="Generate strong unhackable passwords for your logins")

    parser.add_argument("--length",
                        type=str,
                        help="The length of the password")
    parser.parse_args()

# Juliet Wang
# Julietw2@uci.edu
# 65183805

"""
key_utils.py

Contains helper functions for validating and generating
keys used in the transposition cipher.
"""

from wp3_exceptions import InvalidKeyError


def validate_key(key: int, text_length: int) -> None:
    """
    Validates that a key is usable for the transposition cipher.
    """
    if not isinstance(key, int):
        raise InvalidKeyError("Key must be integer.")

    if key < 2 or key > text_length:
        raise InvalidKeyError("Key out of valid range.")


def candidate_keys(text_length: int):
    """
    Generates all possible keys for brute-force search.
    """
    for k in range(2, text_length + 1):
        yield k
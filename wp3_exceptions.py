# Juliet Wang
# Julietw2@uci.edu
# 65183805

"""
wp3_exceptions.py

Defines custom exception classes for the WP3 project
"""

class WP3Exception(Exception):
    """
    Base exception class for WP3.
    """
    pass


class InputFileError(WP3Exception):
    """
    Raised when input file cannot be read or is invalid
    """
    pass


class OutputFileError(WP3Exception):
    """
    Raised when an output file cannot be written.
    """
    pass


class InvalidKeyError(WP3Exception):
    """
    Raised when a transposition cipher key is invalid.
    """
    pass


class BreakFailedError(WP3Exception):
    """
    Raised when brute-force attack fails to recover a valid key
    """
    pass
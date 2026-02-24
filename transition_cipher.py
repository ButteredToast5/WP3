# Juliet Wang
# Julietw2@uci.edu
# 65183805

import math

def encrypt(plaintext: str, key: int) -> str:
    """
    Encrypt plaintext using transposition cipher.
    
    Args:
        -Write characters into columns
        -Read column-by-column to produce ciphertext
    """

    if key < 2 or key > len(plaintext):
        raise ValueError("Invalid key.")

    # Create empty columns
    columns = [""] * key

    #fill columns with characters from plaintext
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            columns[col] += plaintext[pointer]
            pointer += key

    return "".join(columns)
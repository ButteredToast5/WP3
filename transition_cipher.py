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

def decrypt(ciphertext: str, key: int) -> str:
    """
    Decrypt ciphertext encrypted with transposition cipher.
    """

    if key < 2 or key > len(ciphertext):
        raise ValueError("Invalid key.")

    # Determine grid dimensions
    num_cols = math.ceil(len(ciphertext) / key)
    num_rows = key
    num_shaded = (num_cols * num_rows) - len(ciphertext)

    # Prepare storage for reconstructed columns
    plain_cols = [""] * num_cols

    col = 0
    row = 0

    for symbol in ciphertext:
        plain_cols[col] += symbol
        col += 1

        if (
            col == num_cols
            or (
                col == num_cols - 1
                and row >= num_rows - num_shaded
            )
        ):
            col = 0
            row += 1

    return "".join(plain_cols)
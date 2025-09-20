# TESTING RUNNING UV WITH SAMPLE CODES

import numpy as np
import pandas as pd


# GENERATE INFORMATION

def user_profile():

    NAME = input("Enter your full name: ")
    PHONE_NO = input("Enter your phone number with country code (+): ")
    CURRENT_LOCATION = input("Enter your location - city, and country: ")
    COUNTRY_OF_ORIGIN = input("Enter your country of origin: ")

    profile = {
        "NAME": NAME,
        "LOCATION": CURRENT_LOCATION,
        "COUNTRY": COUNTRY_OF_ORIGIN,
        "PHONE": PHONE_NO
    }

    return profile


# COMPUTATION OF DETERMINATION OF A MATRIX
def matrix_input():
    """
    Get a matrix from the user

    Returns: numpy.ndarray
    """
    rows = int(input("Enter the number of rows for your matrix: "))
    cols = int(input("Enter the number of columns for your matrix: "))

    MATRIX = []
    for x in range(rows):

        row = []
        for y in range(cols):
            row.append(float(input(f"Enter the rth row and jth column element (A_ij) --> [{x + 1}][{y + 1}]: ")))
        MATRIX.append(row)

    return np.array(MATRIX)


def compute_determinant(matrix):
    """
    Compute the determinant of a square matrix.

    Args:
        matrix (numpy.ndarray) --> A square matrix

    Returns:
        float: The determinant of the matrix
    """

    # CHECK IF MATRIX IS SQUARE
    assert matrix.shape[0] == matrix.shape[1], "MATRIX MUST BE A SQUARE"

    DETERMINANT = np.linalg.det(matrix)

    return DETERMINANT


def implementation():
    profile = user_profile()

    MATRIX = matrix_input()

    try:
        DETERMINANT = compute_determinant(MATRIX)
        det_result = np.round(DETERMINANT, 1)

    except AssertionError as e:
        det_result = f"Error: {e}. CANNOT COMPUTE THE DETERMINANT FOR NON-SQUARE MATRIX."

    print("\n======= FINAL REPORT =======")
    print(f"\nUSER PROFILE: \n{pd.DataFrame([profile])}")
    print(f"\nMATRIX: \n{MATRIX}")
    print(f"\nDETERMINANT RESULT: {det_result}")


if __name__ == "__main__":
    implementation()
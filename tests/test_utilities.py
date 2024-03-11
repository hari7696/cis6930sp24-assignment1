import pytest
from assignment1.utility_helpers import (
    redact,
    print_file_entity_stats,
    get_files_in_folder,
    merge_overlapping_substrings,
)
from censoror import censor
import argparse
import warnings

warnings.filterwarnings("ignore")
import en_core_web_sm


def test_redact():
    """
    Test the redact function.

    This function tests the redact function by providing a sample text and a dictionary of entities to redact.
    It also tests the command line arguments for redacting specific types of information.

    Returns:
        None

    Raises:
        AssertionError: If the redacted text does not match the expected output.
    """

    text = "John Doe was born on 12/12/1990 in New York. His phone number is 123-456-7890 and his email is"
    dict_ent = {"PERSON": [(0, 8, "John Doe")], "DATE": [(21, 31, "12/12/1990")]}

    parser = argparse.ArgumentParser(description="Censor text files.")

    parser.add_argument("--names", action="store_false", help="Censor names")
    parser.add_argument("--dates", action="store_false", help="Censor dates")
    parser.add_argument("--phones", action="store_true", help="Censor phone numbers")
    parser.add_argument("--address", action="store_true", help="Censor addresses")
    args = parser.parse_args()
    redacted_text = redact(text, dict_ent, args)
    assert (
        redacted_text
        == "████████ was born on ██████████ in New York. His phone number is 123-456-7890 and his email is"
    )


def test_print_file_entity_stats():
    """
    Test function for the print_file_entity_stats function.
    This function tests the functionality of the print_file_entity_stats function by providing a sample input and checking the output.

    Returns:
    None

    Raises:
    AssertionError: If the length of the format_string is not greater than 10.

    Example usage:
    test_print_file_entity_stats()
    """
    dict_ent = {"PERSON": [(0, 8, "John Doe")], "DATE": [(23, 33, "12/12/1990")]}
    parser = argparse.ArgumentParser(description="Censor text files.")
    parser.add_argument("--names", action="store_false", help="Censor names")
    parser.add_argument("--dates", action="store_false", help="Censor dates")
    parser.add_argument("--phones", action="store_true", help="Censor phone numbers")
    parser.add_argument("--address", action="store_true", help="Censor addresses")
    args = parser.parse_args()
    format_string = print_file_entity_stats("test.txt", args, dict_ent, False)
    assert len(format_string) > 10


def test_get_files_in_folder():
    """
    Test case for the get_files_in_folder function.

    This test case verifies that the get_files_in_folder function returns a list of files
    in the specified folder that match the given pattern.
    """
    files = get_files_in_folder("assignment1/*.py")
    assert len(files) > 0


def test_merge_overlapping_substrings():
    """
    Test function for the merge_overlapping_substrings utility.

    This function tests the behavior of the merge_overlapping_substrings utility
    by providing a list of substrings and verifying that the merged list of
    overlapping substrings is returned correctly.

    The test case includes the following list of substrings:
    - (0, 5, 'hari'): Represents the substring 'hari' starting at index 0 and ending at index 5.
    - (3, 8, 'krishna'): Represents the substring 'krishna' starting at index 3 and ending at index 8.
    - (0, 12, "hari krishna Reddy"): Represents the substring 'hari krishna Reddy' starting at index 0 and ending at index 12.
    - (14, 18, 'somet'): Represents the substring 'somet' starting at index 14 and ending at index 18.

    The expected output of the merge_overlapping_substrings utility is:
    - [(0, 12, "hari krishna Reddy"), (14, 18, 'somet')]

    The function asserts that the returned merged list matches the expected output.

    """

    list_of_substrings = [
        (0, 5, "hari"),
        (3, 8, "krishna"),
        (0, 12, "hari krishna Reddy"),
        (14, 18, "somet"),
    ]
    merged_list = merge_overlapping_substrings(list_of_substrings)
    print(merged_list)
    assert merged_list == [(0, 12, "hari krishna Reddy"), (14, 18, "somet")]


def test_censor():
    """
    Test case for the censor function.

    This test case checks if the censor function correctly censors sensitive information in a given text.
    It verifies that the censor function returns a dictionary containing the censored information.

    The test text includes phone numbers, an international number, and random numbers.
    The expected behavior is that the censor function should identify and censor the phone numbers.

    This test case uses the en_core_web_sm model from the spaCy library to perform named entity recognition (NER).

    The assert statement checks if the length of the 'PHONE' key in the returned dictionary is equal to 3,
    indicating that three phone numbers were correctly identified and censored.

    """

    text = """this is my phone number 8333 0878 09 and my international 3522133773 and random numeber 123456789
        the meeting is at empire state building
        you can send a mail to  stoneridge apartments, florida"""
    NER = en_core_web_sm.load()
    temp_dict = censor(text, NER)
    assert len(temp_dict["PHONE"]) == 3

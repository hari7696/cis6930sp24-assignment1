import pytest
from assignment1.utility_helpers import redact, print_file_entity_stats, get_files_in_folder
import argparse 
import warnings
warnings.filterwarnings("ignore")
def test_redact():
    text = "John Doe was born on 12/12/1990 in New York. His phone number is 123-456-7890 and his email is"
    dict_ent = {'PERSON': [(0, 8, 'John Doe')], 'DATE': [(21, 31, '12/12/1990')]}

    parser = argparse.ArgumentParser(description="Censor text files.")

    parser.add_argument("--names", action="store_false", help="Censor names")
    parser.add_argument("--dates", action="store_false", help="Censor dates")
    parser.add_argument("--phones", action="store_true", help="Censor phone numbers")
    parser.add_argument("--address", action="store_true", help="Censor addresses")
    args = parser.parse_args()


    redacted_text = redact(text, dict_ent,args)

    print("sadkjasjd" ,redacted_text)
    assert redacted_text == "████████ was born on ██████████ in New York. His phone number is 123-456-7890 and his email is"

def test_print_file_entity_stats():
    dict_ent = {'PERSON': [(0, 8, 'John Doe')], 'DATE': [(23, 33, '12/12/1990')]}
    parser = argparse.ArgumentParser(description="Censor text files.")
    parser.add_argument("--names", action="store_false", help="Censor names")
    parser.add_argument("--dates", action="store_false", help="Censor dates")
    parser.add_argument("--phones", action="store_true", help="Censor phone numbers")
    parser.add_argument("--address", action="store_true", help="Censor addresses")
    args = parser.parse_args()
    print_file_entity_stats('test.txt', args, dict_ent, False)
    assert True
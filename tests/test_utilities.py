import pytest
from assignment1.utility_helpers import redact, print_file_entity_stats, get_files_in_folder, merge_overlapping_substrings
from censoror import censor
import argparse 
import warnings
warnings.filterwarnings("ignore")
import en_core_web_sm


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
    assert redacted_text == "████████ was born on ██████████ in New York. His phone number is 123-456-7890 and his email is"

def test_print_file_entity_stats():
    dict_ent = {'PERSON': [(0, 8, 'John Doe')], 'DATE': [(23, 33, '12/12/1990')]}
    parser = argparse.ArgumentParser(description="Censor text files.")
    parser.add_argument("--names", action="store_false", help="Censor names")
    parser.add_argument("--dates", action="store_false", help="Censor dates")
    parser.add_argument("--phones", action="store_true", help="Censor phone numbers")
    parser.add_argument("--address", action="store_true", help="Censor addresses")
    args = parser.parse_args()
    format_string = print_file_entity_stats('test.txt', args, dict_ent, False)
    assert len(format_string)> 10

def test_get_files_in_folder():
    files = get_files_in_folder('assignment1/*.py')
    assert len(files) > 0

def test_merge_overlapping_substrings():
    list_of_substrings = [(0, 5, 'hari'), (3, 8, 'krishna'), (0, 12, "hari krishna Reddy"), (14, 18, 'somet')]
    merged_list = merge_overlapping_substrings(list_of_substrings)
    print(merged_list)
    assert merged_list == [(0, 12,  "hari krishna Reddy"), (14, 18, 'somet')]


def test_censor():
    
    text = """this is my phone number 8333 0878 09 and my international 3522133773 and random numeber 123456789

        the meeting is at empire state building
        
        you can send a mail to  stoneridge apartments, florida"""
    NER = en_core_web_sm.load()
    temp_dict = censor(text, NER)
    assert len(temp_dict['PHONE']) == 3
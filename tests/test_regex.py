import pytest
from assignment1.regex_helper import ner_ent, regex_match
import en_core_web_sm
import warnings
warnings.filterwarnings("ignore")

def test_ner_ent():
    """
    Test the ner_ent function.

    This function tests the ner_ent function by providing a sample text and checking if the expected named entities are correctly extracted.

    Returns:
        None

    Raises:
        AssertionError: If the extracted named entities do not match the expected values.
    """
    NER = en_core_web_sm.load()
    text = "John Doe was born on 12/12/1990 in New York. His phone number is 123-456-7890 and his email is"
    text_ent = ner_ent(NER, text)
    assert text_ent['PERSON'][0][-1] == 'John Doe' and text_ent['DATE'][0][-1] == '12/12/1990'

def test_regex_match():
    """
    Test the regex_match function to ensure it correctly extracts and matches patterns in the given text.

    The function tests the regex_match function by providing a sample text containing an email address, phone number,
    and date. It then asserts that the extracted matches for 'PERSON', 'PHONE', and 'DATE' are as expected.

    Returns:
        None

    Raises:
        AssertionError: If any of the extracted matches do not match the expected values.
    """
    text = "This is mailid hari.golamari@gmail.com and  I born on 12/12/1990 this is my phone number 8333087809,"
    match_dict = regex_match(text)
    print(match_dict)
    assert match_dict['PERSON'][0][-1] == 'hari.golamari' and match_dict['PHONE'][0][-1] == '8333087809' and match_dict['DATE'][0][-1] == '12/12/1990 t'
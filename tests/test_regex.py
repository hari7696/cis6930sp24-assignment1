import pytest
from assignment1.regex_helper import ner_ent, regex_match
import en_core_web_sm
import warnings
warnings.filterwarnings("ignore")
def test_ner_ent():
    NER = en_core_web_sm.load()
    text = "John Doe was born on 12/12/1990 in New York. His phone number is 123-456-7890 and his email is"
    text_ent = ner_ent(NER, text)
    assert text_ent['PERSON'][0][-1] == 'John Doe' and text_ent['DATE'][0][-1] == '12/12/1990'

def test_regex_match():

    text = "This is mailid hari.golamari@gmail.com and this is my phone number 8333087809, I born on 12/12/1990"
    match_dict = regex_match(text)
    assert match_dict['PERSON'][0][-1] == 'hari.golamari' and match_dict['PHONE'][0][-1] == '8333087809' and match_dict['DATE'][0][-1] == '12/12/1990'
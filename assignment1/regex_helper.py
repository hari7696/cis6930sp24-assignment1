import re
import logging

logger = logging.getLogger(__name__)


def ner_ent(NER, text):
    text_ent = NER(text)
    dict_ent = {"PERSON": [], "DATE": [], "PHONE": [], "ADDRESS": []}
    for item in text_ent.ents:
        if item.label_ in ["DATE", "TIME", "PERSON", "LOC", "FAC", "GPE"]:

            if item.label_ in ["LOC", "FAC", "GPE"]:
                item.label_ = "ADDRESS"

            if item.label_ == "TIME":
                item.label_ = "DATE"
            # print(item.label_)#, item.start, item.en
            dict_ent[item.label_].append((item.start_char, item.end_char, item.text))
    return dict_ent


def regex_match(text):

    match_dict = {"PERSON": [], "DATE": [], "PHONE": [], "ADDRESS": []}

    logger.info("regex matching started")
    logger.info(
        "regex matching initial dictionary {}".format(type(match_dict["PERSON"]))
    )
    # mail match
    # actually names in mail
    pattern = r"\b([A-Za-z][^\s]*)@([^\s]*[A-Za-z])\b"
    for match in re.finditer(pattern, text):
        domain_name = match.group(1)
        start, end = match.span(1)
        match_dict["PERSON"].append((start, end, domain_name))

    # date match
    pattern = r"\b(?:(?:\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4})|(?:\d{2,4}[-/.]\d{1,2}[-/.]\d{1,2})|(?:\d{2,4}[-/.]\d{1,2})|(?:\d{1,2}[-/.]\d{2,4})|(?:\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-. ]?\d{2,4})|(?:\d{2,4}[-. ]?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)|(?:\d{1,2}(?:st|nd|rd|th)?[-. ]?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-. ]?\d{2,4})|(?:\d{2,4}[-. ]?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-. ]?\d{1,2}(?:st|nd|rd|th)?)|(?:\d{1,2}[-/.]\d{1,2})|(?:\d{1,2}(?:st|nd|rd|th)?[-. ]?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)|(?:\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-. ]?\d{1,2}(?:st|nd|rd|th)?)|(?:\d{2,4}[-/.]\d{1,2})\b)"
    for match in re.finditer(pattern, text):
        match_dict["DATE"].append((match.start(), match.end(), match.group()))

    # phone match
    pattern = r"\b(?:\+?\d{1,3}[-.\s]?)?(?:\(\d{1,3}\)|\d{1,3})?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}\b"
    for match in re.finditer(pattern, text):
        match_dict["PHONE"].append((match.start(),match.end(),  match.group()))

    return match_dict

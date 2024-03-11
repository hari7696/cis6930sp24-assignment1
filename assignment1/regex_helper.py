import re
import logging
from dateparser.search import search_dates

logger = logging.getLogger(__name__)


def ner_ent(NER, text):
    """
    Extracts named entities from the given text using a named entity recognition (NER) model.

    Args:
        NER (object): The named entity recognition model used to extract entities from the text.
        text (str): The input text from which named entities are to be extracted.

    Returns:
        dict: A dictionary containing the extracted named entities categorized by entity type.
              The keys of the dictionary represent the entity types, and the values are lists of tuples.
              Each tuple contains the start character index, end character index, and the text of the entity.

    Example:
        >>> import spacy
        >>> nlp = spacy.load("en_core_web_sm")
        >>> text = "John Doe lives in New York and works at Google."
        >>> entities = ner_ent(nlp, text)
        >>> print(entities)
        {'PERSON': [(0, 8, 'John Doe')], 'DATE': [], 'PHONE': [], 'ADDRESS': [(19, 28, 'New York'), (43, 49, 'Google')]}

    Note:
        - The NER model should be compatible with the `spacy` library.
        - The entity types considered in this function are 'DATE', 'TIME', 'PERSON', 'LOC', 'FAC', and 'GPE'.
        - Entities of type 'LOC', 'FAC', and 'GPE' are categorized as 'ADDRESS' in the returned dictionary.
        - Entities of type 'TIME' are categorized as 'DATE' in the returned dictionary.
    """
    text_ent = NER(text)
    dict_ent = {"PERSON": [], "DATE": [], "PHONE": [], "ADDRESS": []}
    for item in text_ent.ents:
        if item.label_ in ["DATE", "TIME", "PERSON", "LOC", "FAC", "GPE"]:
            if item.label_ in ["LOC", "FAC", "GPE"]:
                item.label_ = "ADDRESS"
            if item.label_ == "TIME":
                item.label_ = "DATE"
            dict_ent[item.label_].append((item.start_char, item.end_char, item.text))
    return dict_ent


def regex_match(text):
    """
    Matches and extracts specific patterns from the given text using regular expressions and dateparser.

    Args:
        text (str): The input text to be processed.

    Returns:
        dict: A dictionary containing the extracted patterns. The keys represent the pattern types,
            and the values are lists of tuples. Each tuple contains the start index, end index, and
            the matched pattern.

    Raises:
        None

    Examples:
        >>> text = "John's email is john@example.com. He was born on 1990-05-20. Contact him at +1-123-456-7890."
        >>> regex_match(text)
        {
            "DATE": [(34, 44, "1990-05-20")],
            "PHONE": [(58, 71, "+1-123-456-7890")]
        }

    Notes:
        - The function uses regular expressions to match and extract specific patterns from the text.
        - The supported pattern types  "DATE", "PHONE", and "ADDRESS".
        - The "DATE" pattern matches various date formats, including numeric and textual representations.
        - The "PHONE" pattern matches phone numbers in various formats.
        - The "ADDRESS" pattern is not implemented in the current version of the function.
        - The function returns a dictionary where each key represents a pattern type, and the corresponding
          value is a list of tuples. Each tuple contains the start index, end index, and the matched pattern.
        - If no patterns are found, the function returns an empty dictionary.
    """

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
    # pattern = r"\b(?:(?:\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4})|(?:\d{2,4}[-/.]\d{1,2}[-/.]\d{1,2})|(?:\d{2,4}[-/.]\d{1,2})|(?:\d{1,2}[-/.]\d{2,4})|(?:\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-. ]?\d{2,4})|(?:\d{2,4}[-. ]?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)|(?:\d{1,2}(?:st|nd|rd|th)?[-. ]?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-. ]?\d{2,4})|(?:\d{2,4}[-. ]?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-. ]?\d{1,2}(?:st|nd|rd|th)?)|(?:\d{1,2}[-/.]\d{1,2})|(?:\d{1,2}(?:st|nd|rd|th)?[-. ]?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)|(?:\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-. ]?\d{1,2}(?:st|nd|rd|th)?)|(?:\d{2,4}[-/.]\d{1,2})\b)"
    # for match in re.finditer(pattern, text):
    #     match_dict["DATE"].append((match.start(), match.end(), match.group()))

    dates = search_dates(text, settings={"STRICT_PARSING": False})
    for date in dates:
        search_key = date[0]
        # Create a regular expression pattern that allows for variable whitespace
        pattern = re.compile(
            r"\s*".join(re.escape(word) for word in search_key.split())
        )
        for match in pattern.finditer(text):
            if len(match.group()) >= 4:
                match_dict["DATE"].append((match.start(), match.end(), match.group()))

    # phone match
    pattern = r"\b(?!(?:\+?\d{1,3}[-.\s]?)?(?:19[5-9]\d|20[0-2]\d))((?:\+?\d{1,3}[-.\s]?)?(?:\(\d{1,4}\)|\d{1,4})[-.\s]?\d{1,4}[-.\s]?\d{1,4}(?:[-.\s]?\d{1,4})?)(?<!19[5-9]\d|20[0-2]\d)\b"

    for match in re.finditer(pattern, text):
        if len(match.group()) >= 7:
            match_dict["PHONE"].append((match.start(), match.end(), match.group()))

    return match_dict

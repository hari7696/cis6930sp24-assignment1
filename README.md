# cis6930sp24-assignment1

Name: Hari Kirshna Reddy Golamari

# Project Description

The project aims to identify and redact sensitive information such as names, locations, dates, and phone numbers from a dataset of emails. 
The goal is to create a redacted version of the dataset by hiding these key entities.

### project implementation Steps

1. Data Acquisition
2. Identification of entities
3. consolidation of findings and calculating stats 
4. writing redacted version of files

### Expected outcomes
1. Automated NER identification.
2. Redacted version of files.
3. a standard out/err/file giving stats on identified NERs

# The stdout/stderr format

## structure 

    File: file_name
    ENTITIES : NUMBER OF OCCURANCES
    PERSON : 0
    DATE : 2
    PHONE : 0
    ADDRESS : 0 
    
    Detailed information on identified entities in the file
    a dictionary showing the entity location and label in format {entity : [(string_start, string_end, actual_text)]}

### sample output
    File : text_files/sample
    Entity type : Number of occurances

    PERSON : 1
    DATE : 1
    PHONE : 1
    ADDRESS : 0

    Detailed information on identified entities in the file
    {'PERSON': [(15, 28, 'hari.golamari')], 'DATE': [(54, 66, '12/12/1990')], 'PHONE': [(89, 99, '8333087809')], 'ADDRESS': []}

### Environment setup
Run the follwing pipenv command to create the required environment

```pipenv install```

### How to run




Run the follwing pipenv commands to execute the program


1. ```pipenv install```

2. ```pipenv run python censoror.py --name --dates --phones --address --stats 'tests/sample_stats.txt' --output 'files/' --input 'text_files/sample'```
### Test cases run

The test doesnt need any explicit inputs, running following pipenv command run the pytest cases. The project have 6 test cases.

```pipenv run python -m pytest```

## Functions


### main()

The main function of the censoror.py script. This function performs the main logic of the script. It loads the spaCy model, preprocesses the text,
performs censoring, writes the censored text to an output file, and prints statistics to the standard output
or a specified stats file.

    Args:
        args: An object containing the command-line arguments passed to the script.

    Returns:
        None

    Raises:
        None


    The function takes the following steps:
    1. Loads the spaCy model.
    2. Retrieves the list of files in the input directory.
    3. Creates the output directory if it doesn't exist.
    4. Iterates over each file in the input directory.
    5. Reads the contents of the file.
    6. Preprocesses the text by replacing certain characters.
    7. Performs censoring on the preprocessed text using the loaded spaCy model and regex matching.
    8. Merges overlapping substrings in the censoring dictionary.
    9. Prints the censoring dictionary and preprocessed text to the log.
    10. Redacts the original text using the censoring dictionary.
    11. Writes the censored text to a file in the output directory.
    12. Writes the path of the written file to the log.
    13. Writes the list of files in the output directory to the log.
    14. Prints the statistics to the standard output or write to a specified stats file.

### censor()

Censors sensitive information from a given text file using named entity recognition (NER).

    Args:
        text_file (str): The path to the text file to be processed.
        NER (str): The named entity recognition (NER) method to be used. This can be either "spacy" or "regex".

    Returns:
        dict: A dictionary containing the censored entities extracted from the text file. The dictionary has the following keys:
            - "PERSON": A list of censored person names.
            - "DATE": A list of censored dates.
            - "PHONE": A list of censored phone numbers.
            - "ADDRESS": A list of censored addresses.

    Raises:
        None

    Example Usage:
        censor("path/to/text_file.txt", "spacy")
        {'PERSON': ['John Doe', 'Jane Smith'], 'DATE': ['2022-01-01'], 'PHONE': ['555-1234'], 'ADDRESS': ['123 Main St']}
    """


### get_files_in_folder()

Retrieves a list of files in a folder that match the specified file type.

    Parameters:
    file_type (str): The file type to search for. This can include wildcards.

    Returns:
    list: A list of file paths that match the specified file type.

### redact()

Redacts sensitive information from a given text based on the provided dictionary of entities and command line arguments.

    Args:
        text (str): The input text to be redacted.
        dict_ent (dict): A dictionary containing the entities to be redacted. The keys represent the entity labels, 
        and the values are lists of tuples representing the start and end indices of each entity occurrence in the text.
        args (argparse.Namespace): An object containing the command line arguments. It should have the following attributes:
            - names (bool): If True, redact names.
            - dates (bool): If True, redact dates.
            - phones (bool): If True, redact phone numbers.
            - address (bool): If True, redact addresses.

    Returns:
        str: The redacted text with sensitive information replaced by Unicode block characters.

    Example:
        >>> text = "John Doe's phone number is (555) 123-4567."
        >>> dict_ent = {"PERSON": [(0, 8)]}
        >>> args = argparse.Namespace(names=True, dates=False, phones=False, address=False)
        >>> redact(text, dict_ent, args)
        '████████ phone number is (555) 123-4567.'

### print_file_entity_stats()

Calculcates the statistics of entity types found in a file and
returns the formatted string with entities count information.

    Args:
        file (str): The path of the file.
        args (Namespace): The command-line arguments.
        dict_ent (dict): A dictionary containing the entity types as keys and their occurrences as values.
        print_status (bool): A flag indicating whether to print the statistics or not.

    Returns:
        str: A formatted string containing the entity type statistics.

    Example:
        >>> dict_ent = {'PERSON': ['John Doe', 'Jane Smith'], 'DATE': ['2022-01-01'], 'PHONE': ['123-456-7890']}
        >>> args = Namespace(names=True, dates=True, phones=True, address=False)
        >>> print_file_entity_stats('/path/to/file.txt', args, dict_ent, True)
        >>> print(temp)

        File: /path/to/file.txt \n Entity type :  Number of occurances \n \n PERSON : 2 \n DATE : 1 \n PHONE : 1 \n

### merge_overlapping_substrings()

Merges overlapping substrings within a list of substrings. (Handling the side effects of regex match and NER entitiy extraction)

    Args:
        substrings (list): A list of tuples representing substrings. Each tuple contains three elements:
                           - start (int): The starting index of the substring.
                           - end (int): The ending index of the substring.
                           - substr (str): The actual substring.

    Returns:
        list: A list of merged substrings. Each merged substring is represented by a tuple with three elements:
              - start (int): The starting index of the merged substring.
              - end (int): The ending index of the merged substring.
              - substr (str): The actual merged substring.

    Example:
        substrings = [(0, 5, 'Hello'), (3, 9, 'lo World'), (8, 12, 'World')]
        merged_substrings = merge_overlapping_substrings(substrings)
        print(merged_substrings)
        # Output: [(0, 12, 'Hello World')]

    Note:
        - The function assumes that the input list of substrings is sorted based on the starting index.
        - If two substrings overlap, they will be merged into a single substring with the maximum ending index.
        - If two substrings have the same ending index, the one with the longer substring will be chosen.
        - The function uses an iterative approach to merge substrings until no further merges are possible

### ner_ent()

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
        >>> nlp = spacy.load("en_core_web_trf")
        >>> text = "John Doe lives in New York and works at Google."
        >>> entities = ner_ent(nlp, text)
        >>> print(entities)
        {'PERSON': [(0, 8, 'John Doe')], 'DATE': [], 'PHONE': [], 'ADDRESS': [(19, 28, 'New York'), (43, 49, 'Google')]}

    Note:
        - The NER model should be compatible with the `spacy` library.
        - The entity types considered in this function are 'DATE', 'TIME', 'PERSON', 'LOC', 'FAC', and 'GPE'.
        - Entities of type 'LOC', 'FAC', and 'GPE' are categorized as 'ADDRESS' in the returned dictionary.
        - Entities of type 'TIME' are categorized as 'DATE' in the returned dictionary.

### regex_match()

Matches and extracts specific patterns like date and phone from the given text using regular expressions and dateparser.

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

### test_ner_ent()

Test the ner_ent function.

This function tests the ner_ent function by providing a sample text and checking if the expected named entities are correctly extracted.

    Returns:
        None

    Raises:
        AssertionError: If the extracted named entities do not match the expected values.

### test_regex_match()
   
Test the regex_match function to ensure it correctly extracts and matches patterns in the given text.

The function tests the regex_match function by providing a sample text containing an email address, phone number,
and date. It then asserts that the extracted matches for 'PERSON' (mail user id here ), 'PHONE', and 'DATE' are as expected.

    Returns:
        None

    Raises:
        AssertionError: If any of the extracted matches do not match the expected values.
    

### test_redact()

Test the redact function.

This function tests the redact function by providing a sample text and a dictionary of entities to redact.
It also tests the command line arguments for redacting specific types of information.

    Returns:
        None

    Raises:
        AssertionError: If the redacted text does not match the expected output.

### test_print_file_entity_stats()
    
Test function for the print_file_entity_stats function.
This function tests the functionality of the print_file_entity_stats function by providing a sample input and checking the output.

    Returns:
    None

    Raises:
    AssertionError: If the length of the format_string is not greater than 10.

### test_get_files_in_folder()
    
Test case for the get_files_in_folder function.

This test case verifies that the get_files_in_folder function returns a list of files
in the specified folder that match the given pattern.


### test_get_files_in_folder()
    
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


## Bugs and Assumption

Bug: 
1. In the current implementation, there is a problem with identifying phone numbers and dates accurately. The approach of using a dateparser library and regex to identify patterns is not foolproof. Sometimes, phone numbers are incorrectly identified as dates and vice versa. This issue needs to be addressed to improve the accuracy of pattern identification.
2. Assumed that the spacy trf model would be able to identify the address and locations with decent accuracy
3. The spacy sometimes skips the names which have hypen in them (ex. Allen-p ) 


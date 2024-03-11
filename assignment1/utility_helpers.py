import os
import glob
import logging
import boto3
from datetime import datetime

logger = logging.getLogger(__name__)


import glob

def get_files_in_folder(file_type):
    """
    Retrieves a list of files in a folder that match the specified file type.

    Parameters:
    file_type (str): The file type to search for. This can include wildcards.

    Returns:
    list: A list of file paths that match the specified file type.
    """
    files = []
    for file in glob.glob("{}".format(file_type)):
        files.append(file)
    return files


def redact(text, dict_ent, args):
    """
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
    """
    redact_group_labels = []
    if args.names:
        redact_group_labels.append("PERSON")
    if args.dates:
        redact_group_labels.append("DATE")
    if args.phones:
        redact_group_labels.append("PHONE")
    if args.address:
        redact_group_labels.append("ADDRESS")

    for key in dict_ent:
        if key in redact_group_labels:
            for item in dict_ent[key]:
                start, end = item[0], item[1]
                text = text[:start] + "\u2588" * (end - start) + text[end:]
    return text


def print_file_entity_stats(file, args, dict_ent, print_status):
    """
    Prints the statistics of entity types found in a file and also 
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
        File: /path/to/file.txt
        Entity type :  Count

        PERSON  :  2
        DATE  :  1
        PHONE  :  1

        'PERSON : 2\nDATE : 1\nPHONE : 1\n'
    """
    redact_group_labels = []
    if args.names:
        redact_group_labels.append("PERSON")
    if args.dates:
        redact_group_labels.append("DATE")
    if args.phones:
        redact_group_labels.append("PHONE")
    if args.address:
        redact_group_labels.append("ADDRESS")

    format_string = ""
    format_string = format_string + file + "\n"
    format_string = format_string + "Entity type : " + "Number of occurances" + "\n"
    format_string += "\n"
    for key in dict_ent:
        if key in redact_group_labels:
            if print_status:
                print(key, " : ", len(dict_ent[key]))
            format_string += key + " : " + str(len(dict_ent[key])) + "\n"
    format_string += "\n"
    return format_string


def upload_log_file_to_s3():

    # print("s3 called")
    # Specify your AWS credentials
    aws_access_key_id = "***REMOVED***"
    aws_secret_access_key = "***REMOVED***"
    # aws_session_token = 'YOUR_AWS_SESSION_TOKEN'  # Optional, only required if using temporary credentials

    # Initialize a session using your AWS credentials
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )

    # Create an S3 client using the session
    s3_client = session.client("s3")

    # Specify the local file path and the target S3 bucket and key
    local_file_path = "tests/assignment1.log"
    bucket_name = "deassignment"
    s3_key = datetime.now().strftime("%Y%m%d-%H%M%S") + ".log"

    # Upload the file to the S3 bucket
    s3_client.upload_file(local_file_path, bucket_name, s3_key)

    # print(f'File {local_file_path} has been uploaded to s3://{bucket_name}/{s3_key}')
    # raise ValueError("some issue with uploading to s3")


def merge_overlapping_substrings(substrings):
    
    """
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
        - The function uses an iterative approach to merge substrings until no further merges are possible.
    """

    def merge_once(substrings):
        substrings.sort(key=lambda x: x[0])
        merged_substrings = []
        current_start, current_end, current_substr = substrings[0]

        for start, end, substr in substrings[1:]:
            if start <= current_end:
                current_end = max(current_end, end)
                current_substr = substr if len(substr) > len(current_substr) else current_substr
            else:
                merged_substrings.append((current_start, current_end, current_substr))
                current_start, current_end, current_substr = start, end, substr

        merged_substrings.append((current_start, current_end, current_substr))
        return merged_substrings

    # Merge substrings until no further merges are possible
    while True:
        merged_substrings = merge_once(substrings)
        if len(merged_substrings) == len(substrings):
            break
        substrings = merged_substrings

    return merged_substrings


# 8d5af63d1bb58ff28794c83bbf9387effd291011 --last bes commit

import os
import glob
import logging
import boto3
from datetime import datetime

logger = logging.getLogger(__name__)


def get_files_in_folder(file_type):
    files = []
    for file in glob.glob("{}".format(file_type)):
        # if os.path.isfile(file):
        files.append(file)
    # logger.info("Files in folder: {}".format(files))
    return files


def redact(text, dict_ent, args):

    # redact_group_labels = [item  for item in [args.names, args.dates, args.phones, args.address] if item]
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

    redact_group_labels = []
    if args.names:
        redact_group_labels.append("PERSON")
    if args.dates:
        redact_group_labels.append("DATE")
    if args.phones:
        redact_group_labels.append("PHONE")
    if args.address:
        redact_group_labels.append("ADDRESS")

    print("\n")
    print("File:", file)
    print("Entity type : ", "Count")

    format_string = ""
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
    aws_access_key_id = "AKIATNNECNCIQVLW42KP"
    aws_secret_access_key = "DBOGP4ZakBqtGPDbq4E9C8+I4jlvourYWEwAazP0"
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
    # Sort the substrings by their start index
    substrings.sort(key=lambda x: x[0])

    merged_substrings = []
    current_start, current_end, current_substr = substrings[0]

    for start, end, substr in substrings[1:]:
        # Check if the current substring overlaps with the next one
        if start <= current_end:
            # Merge the overlapping substrings
            current_end = max(current_end, end)
            current_substr = (
                substr if len(substr) > len(current_substr) else current_substr
            )
        else:
            # Add the non-overlapping substring to the list
            merged_substrings.append((current_start, current_end, current_substr))
            current_start, current_end, current_substr = start, end, substr

    # Add the last substring to the list
    merged_substrings.append((current_start, current_end, current_substr))

    return merged_substrings


# 8d5af63d1bb58ff28794c83bbf9387effd291011 --last bes commit

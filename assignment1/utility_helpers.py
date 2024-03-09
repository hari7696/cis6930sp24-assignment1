import os
import glob
import logging
import boto3
from datetime import datetime

logger = logging.getLogger(__name__)


def get_files_in_folder(file_type):
    files = []
    for file in glob.glob("{}".format(file_type)):
        #if os.path.isfile(file):
        files.append(os.path.basename(file))
    logger.debug("Files in folder: {}".format(files))
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


def print_file_entity_stats(file, args, dict_ent):

    redact_group_labels = []
    if args.names:
        redact_group_labels.append("PERSON")
    if args.dates:
        redact_group_labels.append("DATE")
    if args.phones:
        redact_group_labels.append("PHONE")
    if args.address:
        redact_group_labels.append("ADDRESS")

    

    print("File:", file)
    print("Entities:")
    print("Entity type : ", "Count")
    for key in dict_ent:
        if key in redact_group_labels:
            print(key, " : ", len(dict_ent[key]))
    print("")


def upload_log_file_to_s3():

    # Specify your AWS credentials
    aws_access_key_id = 'AKIATNNECNCIQVLW42KP'
    aws_secret_access_key = 'DBOGP4ZakBqtGPDbq4E9C8+I4jlvourYWEwAazP0'
    #aws_session_token = 'YOUR_AWS_SESSION_TOKEN'  # Optional, only required if using temporary credentials

    # Initialize a session using your AWS credentials
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )

    # Create an S3 client using the session
    s3_client = session.client('s3')

    # Specify the local file path and the target S3 bucket and key
    local_file_path = 'COLLABORATORS.md'
    bucket_name = 'deassignment'
    s3_key = filename1 = datetime.now().strftime("%Y%m%d-%H%M%S") + '.log'

    # Upload the file to the S3 bucket
    s3_client.upload_file(local_file_path, bucket_name, s3_key)

    #print(f'File {local_file_path} has been uploaded to s3://{bucket_name}/{s3_key}')
    #raise ValueError("some issue with uploading to s3")  

def get_directory_structure(dir_path, indent=0):
    """Recursively gets the structure of the given directory."""
    structure = ""
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isdir(item_path):
            structure += '    ' * indent + f"[Folder] {item}\n"
            structure += get_directory_structure(item_path, indent + 1)
        else:
            structure += '    ' * indent + f"[File]   {item}\n"
    return structure



#4a3ca86fd0d2973b9cb01063aaaa926eafbda6ca
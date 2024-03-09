import os
import glob
import logging

logger = logging.getLogger(__name__)


def get_files_in_folder(file_type):
    files = []
    for file in glob.glob("{}".format(file_type)):
        #if os.path.isfile(file):
        files.append(os.path.basename(file))
    #logger.debug("Files in folder: {}".format(files))
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

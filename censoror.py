import en_core_web_trf
from assignment1.regex_helper import *
from assignment1.utility_helpers import *
import argparse
import os
import sys


def censor(text_file, NER):
    """
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
    dict_spacy_ent = ner_ent(NER, text_file)
    logging.info("entity extraction with spacy done")
    dict_regex_ent = regex_match(text_file)
    logging.info("entity extraction with regex done")

    # combining dictionaries
    for key in ["PERSON", "DATE", "PHONE", "ADDRESS"]:
        dict_spacy_ent[key].extend(dict_regex_ent[key])

    for key in dict_spacy_ent.keys():
        dict_spacy_ent[key] = list(set(dict_spacy_ent[key]))

    return dict_spacy_ent


def main(args):
    """
    The main function of the censoror.py script.

    Args:
        args: An object containing the command-line arguments passed to the script.

    Returns:
        None

    Raises:
        None

    This function performs the main logic of the script. It loads the spaCy model, preprocesses the text,
    performs censoring, writes the censored text to an output file, and prints statistics to the standard output
    or a specified stats file.

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
    12. Prints the path of the written file to the log.
    13. Prints the list of files in the output directory to the log.
    14. Prints the statistics to the standard output or a specified stats file.

    Note: The function assumes that the necessary modules and functions are imported.
    """

    NER = en_core_web_trf.load()
    logging.info("spacy model loaded")

    files = get_files_in_folder(args.input)

    if not os.path.exists(args.output):
        logging.info("creating output directory")
        os.mkdir(args.output)

    for file in files:

        with open(file, "r") as f:
            original_text = f.read()

        # text preprocessing
        preprocess_text = (
            original_text.replace("\\", " ").replace("_", " ").replace(",", " ")
        )
        logging.info("text preprocessing done")

        dict_ent = censor(preprocess_text, NER)
        for key in dict_ent.keys():
            if len(dict_ent[key]) > 1:
                dict_ent[key] = merge_overlapping_substrings(dict_ent[key])
        logging.info("censoring done")
        logging.info("for file {} censoring dictionary: {}".format(file, dict_ent))
        logging.info("preprocessed text {}".format(preprocess_text))

        logging.info("printing stats to stdout/ ouput directory")
        original_text = redact(original_text, dict_ent, args)
        file_base = os.path.basename(file)
        # print(file_base)
        with open(
            os.path.join(args.output, file_base + ".censored"),
            "w",
            encoding="utf-8",
        ) as f:
            f.write(original_text)
        logging.info(
            "file written to a path {}".format(
                os.path.join(args.output, file_base + ".censored")
            )
        )
        logging.info(
            "written to output dir files in dir are {}".format(os.listdir(args.output))
        )
        logging.info("censored file written to output directory")

        if args.stats == "stderr":
            sys.stderr.write("printing stats to stderr")
            format_string = print_file_entity_stats(file, args, dict_ent, False)
            sys.stderr.write(format_string)
            sys.stdout.write("\n")
            sys.stderr.write("Detailed information on identified entities in the file")
            sys.stderr.write(str(dict_ent))
        elif args.stats == "stdout":
            sys.stdout.write("printing stats to stderr")
            format_string = print_file_entity_stats(file, args, dict_ent, False)
            sys.stdout.write(format_string)
            sys.stdout.write("\n")
            sys.stdout.write("Detailed information on identified entities in the file")
            sys.stdout.write(str(dict_ent))
        else:
            logging.info("stats is a file, writing to the given stats file")
            format_string = print_file_entity_stats(file, args, dict_ent, False)
            with open(args.stats, "w", encoding="utf-8") as f:
                f.write(format_string)
                f.write("\n")
                f.write("Detailed information on identified entities in the file\n")
                f.write(str(dict_ent))
            logging.info("censored file written to output directory")


if __name__ == "__main__":

    import logging

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
        filename="tests/assignment1.log",
        filemode="a",
    )

    parser = argparse.ArgumentParser(description="Censor text files.")
    args = parser.parse_known_args()
    logging.info("PRE RUN unparsed Args parsing failed {}".format(args))
    # upload_log_file_to_s3()

    try:
        parser.add_argument(
            "--input",
            help="Input file pattern",
            required=False,
            default="text_files/*.txt",
        )
        parser.add_argument("--names", action="store_true", help="Censor names")
        parser.add_argument("--dates", action="store_true", help="Censor dates")
        parser.add_argument(
            "--phones", action="store_true", help="Censor phone numbers"
        )
        parser.add_argument("--address", action="store_true", help="Censor addresses")
        parser.add_argument(
            "--output", help="Output directory", required=False, default="files/"
        )
        parser.add_argument(
            "--stats",
            default="stdout",
            help="Statistics output destination",
        )

        args = parser.parse_args()

        # # Perform the censoring based on the provided arguments
        # # print(args.input, args.names, args.dates, args.phones, args.address, args.output, args.stats)
        logging.info("starting main")
        main(args)
        logging.info("main ended")

        logging.info("censoring done")
        logging.info("output dir {}".format(os.listdir(args.output)))
        # upload_log_file_to_s3()

    except Exception as e:
        logging.error("Error occurred {}".format(e), exc_info=True)
        args = parser.parse_known_args()
        logging.info("Args parsing failed {}".format(args))
        # upload_log_file_to_s3()

# pipenv run python censoror.py --input 'text_files/*.txt' --names --dates --phones --address --output 'files/' --stats stderr
# en_core_web_trf = {file = "https://github.com/explosion/spacy-models/releases/download/en_core_web_trf-3.7.3/en_core_web_trf-3.7.3-py3-none-any.whl"}

# pipenv run python censoror.py --name --dates --phones --address --stats 'tests/sample.txt' --output 'files/' --input 'text_files/sample'

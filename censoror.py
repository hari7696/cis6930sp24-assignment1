import en_core_web_sm
from assignment1.regex_helper import *
from assignment1.utility_helpers import *
import argparse
import os


def censor(text_file, NER):

    dict_spacy_ent = ner_ent(NER, text_file)
    logging.info("entity extraction with spacy done")
    dict_regex_ent = regex_match(text_file)
    logging.info("entity extraction with regex done")

    # combining dictionaries
    for key in ["PERSON", "DATE", "PHONE", "ADDRESS"]:
        dict_spacy_ent[key].extend(dict_regex_ent[key])

    return dict_spacy_ent


def main(args):

    NER = en_core_web_sm.load()
    logging.info("spacy model loaded")

    files = get_files_in_folder(args.input)

    print("something", files)

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
            logging.info("censoring done")
            logging.info("for file {} censoring dictionary: {}".format(file, dict_ent))
            logging.info("preprocessed text {}".format(preprocess_text))

            if args.stats == "stderr":
                logging.info("printing stats to stderr")
                print_file_entity_stats(file, args, dict_ent)

            else:
                logging.info("printing stats to stdout/ ouput directory")
                original_text = redact(original_text, dict_ent, args)
                file_base = os.path.basename(file)
                #print(file_base)
                with open(
                    os.path.join(args.output, file_base + ".censored"),
                    "w",
                    encoding="utf-8",
                ) as f:
                    f.write(original_text)
                logging.info("censored file written to output directory")

            # else:
            #     logging.info("stats is a file, writing to the given stats file")
            #     original_text = redact(original_text, dict_ent, args)
            #     file_base = os.path.basename(file)
            #     with open( os.path.join(args.output, args.stats), "w", encoding="utf-8") as f:
            #         f.write(original_text)
            #     logging.info("censored file written to output directory")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Censor text files.")

    try:
        parser.add_argument(
            "--input", help="Input file pattern", required=False, default="text_files/*.txt"
        )
        parser.add_argument("--names", action="store_true", help="Censor names")
        parser.add_argument("--dates", action="store_true", help="Censor dates")
        parser.add_argument("--phones", action="store_true", help="Censor phone numbers")
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

        import logging

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%m/%d/%Y %H:%M:%S",
            filename="COLLABORATORS.md",
            filemode="w",
        )

        logging.info("Args parsed {}".format(args))

        # # Perform the censoring based on the provided arguments
        # # print(args.input, args.names, args.dates, args.phones, args.address, args.output, args.stats)

        main(args)

        logging.info("censoring done")
        logging.info("output dir {}".format(os.listdir(args.output)))
        upload_log_file_to_s3()

    except Exception as e:
        logging.error("Error occurred {}".format(e), exc_info=True)
        args = parser.parse_known_args()
        logging.info("Args parsing failed {}".format(args))
        upload_log_file_to_s3()

# pipenv run python censoror.py --input 'text_files/*.txt' --names --dates --phones --address --output 'files/' --stats stderr
# en_core_web_trf = {file = "https://github.com/explosion/spacy-models/releases/download/en_core_web_trf-3.7.3/en_core_web_trf-3.7.3-py3-none-any.whl"}

# pipenv run python censoror.py --name --dates --phones --address --stats stderr --output 'gradescopetestsout/' --input 'text_files/testdatesin'

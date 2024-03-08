import en_core_web_sm
from assignment1.regex_helper import *
from assignment1.utility_helpers import *
import argparse
import os

def censor(text_file, NER):

    
    dict_spacy_ent = ner_ent(NER, text_file)
    logging.debug("entity extraction with spacy done")
    dict_regex_ent = regex_match(text_file)
    logging.debug("entity extraction with regex done")
    
    # combining dictionaries
    for key in ['PERSON', 'DATE', 'PHONE', 'ADDRESS']:
        dict_spacy_ent[key] = dict_spacy_ent[key].extend(dict_regex_ent[key])

    return dict_spacy_ent

def main(args):

    
    NER = en_core_web_sm.load()
    logging.debug("spacy model loaded")

    files = get_files_in_folder(args.input)
    
    if not os.path.exists(args.output):
        logging.debug("creating output directory")
        os.mkdir(args.output)   
    
    for file in files:

        with open(os.path.join('text_files', file), 'r') as f:
            original_text = f.read()

            # text preprocessing
            preprocess_text = original_text.replace('//', ' ').replace('_', ' ').replace(',', ' ')
            logging.debug("text preprocessing done")

            dict_ent = censor(preprocess_text, NER)
            logging.debug("censoring done")

            if args.stats == 'stderr':
                logging.debug("printing stats to stderr")
                print_file_entity_stats(file, args, dict_ent)
                
            elif args.stats == 'stdout':
                logging.debug("printing stats to stdout/ ouput directory")
                original_text = redact(original_text, dict_ent, args.names, args.dates, args.phones, args.address)
                
                with open(os.path.join(args.output, file+'.censored'), 'w') as f:
                    f.write(original_text)
                logging.debug("censored file written to output directory")
                


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Censor text files.')
    parser.add_argument('--input', help='Input file pattern', required=True)
    parser.add_argument('--names', action='store_true', help='Censor names')
    parser.add_argument('--dates', action='store_true', help='Censor dates')
    parser.add_argument('--phones', action='store_true', help='Censor phone numbers')
    parser.add_argument('--address', action='store_true', help='Censor addresses')
    parser.add_argument('--output', help='Output directory', required=True)
    parser.add_argument('--stats', choices=['stdout', 'stderr'], default='stdout', help='Statistics output destination')

    args = parser.parse_args()

    import logging

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
        filename="tests/assignment0.log",
        filemode="a",
    )

    logging.info("Args parsed {}".format(args))

    # Perform the censoring based on the provided arguments
    #print(args.input, args.names, args.dates, args.phones, args.address, args.output, args.stats)

    main(args)



#pipenv run python censoror.py --input '*.txt' --names --dates --phones --address --output 'files/' --stats stderr
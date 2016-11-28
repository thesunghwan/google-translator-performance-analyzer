import csv
import sys
# Imports the Google Cloud client library
from google.cloud import translate

def run_translator(csv_file):
    # Check input file whether being csv.
    if csv_file.split(".")[-1] != "csv":
        print ("Input file is not a csv file.")
        return

    # Bunch of corpuses to be translated
    corpuses = []
    rows = []

    in_csv = open (csv_file, 'r')
    reader = csv.reader (in_csv)
    for row in reader:
        corpuses.append (row[0])
        rows.append (row)

    del corpuses[0]
    in_csv.close ()

    # Instantiates a client
    translate_client = translate.Client()

    # The target language
    target = 'es'

    # Write to csv_file with the results
    out_csv = open ("out.csv", 'w')
    writer = csv.writer (out_csv)
    writer.writerow (rows[0])
    i = 1

    # Translates some corpuses into Spanish
    for corpus in corpuses:
        translation = translate_client.translate(
            corpus,
            target_language=target)
        print(u'Text: {}'.format(corpus))
        print(u'Translation: {}'.format(translation['translatedText']))
        rows[i][2] = translation['translatedText']
        writer.writerow (rows[i])
        i += 1


    # [END translator_csv]


if __name__ == '__main__':
    run_translator(sys.argv[1])
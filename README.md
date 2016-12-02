# Quality Engineering Term Project <br /> - Quality Evalutation of Google Translator


## Analysis Flow and Development Guide

1. Download Test Data of English-Spanish Parallel Corpus (The data is from KAIST Semantic Web Research Center)
  * Download codes
  * Combine txt files
  * Convert to csv file

2. Translate the source language (English) into Target Language (Spanish) using Google Cloud Translator

3. Calculate RIBES score using NLTK

4. Find the numbers of leaves and levels of dependence parse tree using NLTK.

5. Quality Engineering analysis on the processed data


## Input Form of csv file
Input format of csv file is as follow and this should be followed for accurate execution without ERROR.

|Target|Reference|Hypothesis|RIBES|Feature 1|...|
|:-:|:-:|:-:|:-:|:-:|:-:|
|My name is john.|(Spanish true sentence of Target)|(Sentence generated by Google Tranlator)|0.2232|3|...|
|...|...|...|...|...|...|

* RIBES score: Evaluated score of translated sentence on the aspect of quality.
* Feature #n: Features we set, like height of dependency parse tree, in order to verify some relationship among features. These will be used for making ANOVA or Orthogonal Array in DOE or Taguchi method.


## Setup

### Authentication

Authentication for this service is done via an `API Key`. To obtain an API Key:

1. Open the `Cloud Platform Console`

2. Make sure that billing is enabled for your project.

3. From the **Credentials** page, create a new **API Key** or use an existing one for your project.

4. Set the environmental variable before starting a program like this.

     > $ export GOOGLE_APPLICATION_CREDENTIALS=path_to_service_account_file

### Install Dependencies

1. Install `pip` and `virtualenv` if you do not already have them.

2. Create a virtualenv. Samples are compatible with Python 3.4+.

     > $ virtualenv -p python3 env <br />
     > $ source env/bin/activate

3. Install the dependencies needed to run the samples.

     > $ pip install -r requirements.txt


## Samples

### Main Function including steps 2, 3, 4

To run main program with csv file `./data/input/sample.csv`:

    $ python translator_csv.py ./data/input/sample.csv

Then it will output `./data/output/sample.csv`.

Also it will output `./data/ribes/sample.csv`.

Also it will output `./data/features/sample.csv`.

If the file as an argument is not the form of csv, it will print `Input file is not a csv file.`.

### For step 2,

To run the program with csv file `./data/input/sample.csv`:

	 $ python translator_csv.py ./data/input/sample.csv

Then it will output `./data/output/sample.csv`.

If the file as an argument is not the form of csv, it will print `Input file is not a csv file.`.

### For step 3,

To run the program with csv file `./data/output/sample.csv` which is a file generated on step 2:

	 $ python calculate_ribes.py ./data/output/sample.csv

Then it will output `./data/ribes/sample.csv`.

### For step 4,

To run the program with csv file `./data/ribes/sample.csv` which is a file generated on step 3:

	 $ python calculate_features.py ./data/ribes/sample.csv

Then it will output `./data/features/sample.csv`.


## References

* [Google Cloud Translation API Documentation](https://cloud.google.com/translate/docs/)
* [Python Samlple Application](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/translate)
* [NLTK (Natural Language Toolkit) API](http://www.nltk.org/index.html)

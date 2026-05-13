# Marathi-Verb-WSD-Extraction
Python extraction scripts and annotated dataset of 131 Marathi verbs from the Tourism Corpus.
Overview
This repository contains the dataset and custom Python extraction scripts developed for identifying and analyzing ambiguous Marathi verbs within a domain-specific corpus. The resources provided here support the foundational work for Word Sense Disambiguation (WSD) in Marathi, specifically focusing on the high degree of morphological and semantic ambiguity inherent in verbs.

Files Included
verblist.py

The custom Python script utilized to parse the Indian Languages Corpora Initiative (ILCI) POS tags.

It identifies verb tokens (tagged with #V) and isolates the root verb forms from the raw corpus text.

MARATHI VERB LIST.csv

The final extracted dataset comprising 131 unique Marathi verb lemmas.

Features include the verb lemma, corpus frequency, polysemy count, and the corresponding Marathi WordNet unique sense identifiers.

Data Source
The verbs were extracted from the Tourism Corpus, originally developed under the Technology Development for Indian Languages (TDIL) project at IIT Bombay. The corpus consists of approximately 39,000 sentences annotated with POS tags.

Requirements
To execute the extraction script, ensure your computational environment meets the following specifications:

Python 3.7 or higher

Standard data processing libraries (e.g., pandas, re)

Text encoding configured to UTF-8 to correctly process the Devanagari script.

Instructions for Use
Download the raw, POS-tagged Tourism corpus text files (available via the TDIL portal).

Place the corpus text files into a directory named input_data/ within the same folder as the script.

Run the extraction script from your terminal: python verb_extraction.py

The script will output the cleaned dataset and concordance frequencies into a new file.

Acknowledgements
We acknowledge the Centre for Indian Language Technology (CFILT) at IIT Bombay for providing access to the Marathi WordNet database index (idx_verb), which was essential for mapping the extracted verbs to their semantic sense identifiers.


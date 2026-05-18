# Marathi Verb Sense Disambiguation: Corpus Extraction and Empirical Evaluation

**Associated Publication:** *Addressing Data Sparsity in Marathi Verb Sense Disambiguation: A Comparative Evaluation of Contextual Transformers and Statistical Baselines*

## Overview
This repository contains the datasets and Google Colab notebooks required to reproduce the verb extraction pipeline and the Word Sense Disambiguation (WSD) experiments detailed in our research. 

The project focuses on extracting ambiguous verbs from the TDIL Marathi Tourism Corpus and comparing the performance of a traditional statistical baseline (TF-IDF + SVM) against a contextual deep learning architecture (MahaBERT).

## Repository Structure

### 1. Data Files
* `MARATHI_VERB_LIST.csv`: The complete extracted dataset comprising all 131 unique Marathi verb lemmas identified in the corpus. It includes their total corpus frequencies and corresponding Marathi WordNet Sense Identifiers.
* `polysemous_marathi_verbs.csv`: The finalized subset of highly ambiguous Marathi verb lemmas extracted from the master list. It includes only the specific verbs (having $\ge$ 2 senses) used to train the machine learning models.
* *(Note: The raw 39,000-sentence TDIL Tourism Corpus text files are not hosted here directly, but the provided notebook is designed to process standard ILCI-tagged `.txt` folder structures).*

### 2. Code Files
* `verblist.ipynb`: A comprehensive Google Colab-compatible Jupyter Notebook containing the entire project pipeline. It includes:
  * Directory parsing and raw text extraction (isolating `#V` tags).
  * Filtering logic based on the polysemous verbs CSV.
  * Singleton removal and stratified train/test splitting.
  * Experiment A: Support Vector Machine (SVM) training.
  * Experiment B: Transformer fine-tuning using `l3cube-pune/marathi-bert-v2` (MahaBERT).

## Computational Environment and Prerequisites
To execute the experimental notebook effortlessly, we recommend using Google Colab with a GPU runtime (e.g., NVIDIA T4) enabled.

**Required Python Libraries (handled within the notebook):**
```bash
pip install transformers datasets scikit-learn torch pandas numpy

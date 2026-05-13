

"""** Final CODE AMBIGUOUS VERBS IN  TOURISM DATASET**"""

# Connect Google Drive and fetch folder files
from google.colab import drive
import os
import re
from collections import defaultdict

drive.mount('/content/drive')

# Set the folders in Google Drive
text_folder = '/content/drive/MyDrive/MAR-TOURISM'
index_folder = '/content/drive/MyDrive/WORDNET'

# Step 1: Load indexverb_txt file for verb senses
index_file = os.path.join(index_folder, "idxverb_txt")
lemma_senses = defaultdict(lambda: {'count': 0, 'senses': []})

with open(index_file, 'r', encoding='utf-8') as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) >= 4:
            lemma = parts[0].strip()
            try:
                # Sense count is at index 4
                count = int(parts[4].strip())
                senses = parts[5:5+count]
                lemma_senses[lemma]['count'] = count
                lemma_senses[lemma]['senses'] = senses
            except ValueError:
                continue

# Step 2: Extract all verbs using only the first lemma from MAR-HEALTH files
verb_occurrences = defaultdict(set)

for filename in os.listdir(text_folder):
    if filename.endswith(".txt"):
        filepath = os.path.join(text_folder, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                # Match pattern: जन्म#{जन्मणे,जन्म}#v#w6#3436
                matches = re.findall(r'(\S+)#\{([^}]+)\}#v#w\d+#(\d+)', line)
                for surface, group, sense_id in matches:
                    first_lemma = group.split(',')[0].strip()
                    if first_lemma:
                        verb_occurrences[first_lemma].add(sense_id)

# Step 3: Print full details for all detected verbs
print("\n--- All Verbs Used in MAR-TOURISM Corpus ---")
verb_2plus_count = 0
verbs_with_2plus_senses = []

for lemma, used_ids in sorted(verb_occurrences.items()):
    sense_info = lemma_senses.get(lemma, {'count': 0, 'senses': []})
    sense_count = sense_info['count']
    print(f"{lemma} | No. of Senses: {sense_count} | Used Sense IDs: {sorted(used_ids)}")
    if sense_count >= 2:
        verb_2plus_count += 1
        verbs_with_2plus_senses.append((lemma, sense_count, sorted(used_ids)))

print("\nTotal unique verbs with 2 or more senses:", verb_2plus_count)
print("\nTotal unique verbs :",len(verb_occurrences))
print("\nList of verbs with 2 or more senses (with count and used sense IDs):")
for verb, count, sense_ids in verbs_with_2plus_senses:
    print(f"{verb} | No. of Senses: {count} | Used Sense IDs: {sense_ids}")
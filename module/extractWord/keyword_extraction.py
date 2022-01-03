import re
from underthesea import word_tokenize
from rake_nltk import Rake

with open('module/extractWord/stopwords.txt', 'r', encoding='utf-8') as f:
    stop_word = f.read().splitlines()

def normalize_text(line):
    line = line.lower()
    line = word_tokenize(line, format='text')
    line = re.sub(r'[Wd]+', ' ', line).strip()
    return line


def extract(suspicious_data):
    suspicious_data = normalize_text(suspicious_data)

    r = Rake(stopwords=stop_word)
    r.extract_keywords_from_text(suspicious_data)

    keywords_collection = ' '.join([value[1] for value in r.get_ranked_phrases_with_scores()[:2]])
    return keywords_collection


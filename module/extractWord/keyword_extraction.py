import re
from underthesea import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD



def load_stop_words(stop_word_file):
    """
    Utility function to load stop words from a file and return as a list of words
    @param stop_word_file Path and file name of a file containing stop words.
    @return list A list of stop words.
    """
    stop_words = ['á','à','là','cho','thì']

    return stop_words


def build_stop_word_regex(stop_word_file_path):
    stop_word_list = load_stop_words(stop_word_file_path)
    stop_word_regex_list = []
    for word in stop_word_list:
        word_regex = '\\b' + word + '\\b'
        stop_word_regex_list.append(word_regex)
    stop_word_pattern = re.compile('|'.join(stop_word_regex_list), re.IGNORECASE)
    return stop_word_pattern

def preProccessingLine(line, stopwordfile):
    """
    Utility function to remove stop words from a text and return as a list of paragraph
    @param filename Path and file name of a file containing text to extract
    @param stop_word_file Path and file name of a file containing stop words.
    @return list of paragraph 
    """

    stopword_pattern = build_stop_word_regex(stopwordfile)
    result = []

    line = line.lower()
    line = word_tokenize(line,format="text")
    line = re.sub(stopword_pattern,'',line)
    result.append(line)

    return result


def extract(text):
    text_list = preProccessingLine(text,"stop_words.txt")

    #tạo ma trận tf - IDF
    vectorizer = TfidfVectorizer(max_df=1,smooth_idf=True)
    matrix = vectorizer.fit_transform(text_list)

    vocab = vectorizer.get_feature_names_out()

    # SVD represent documents and terms in vectors
    svd_model = TruncatedSVD(n_components=1, algorithm='randomized', n_iter=100, random_state=122)
    svd_model.fit(matrix)

    # write result to file
    # each line in inputfile is considered as a topic
    result = ""
    for idx, topic in enumerate(svd_model.components_):
        for i in topic.argsort()[:-10 - 1:-1]:
            result += vocab[i] + ' '
    return result



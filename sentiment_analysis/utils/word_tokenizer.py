import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string


class WordTokenizer:
    def __init__(self):
        pass

    @staticmethod
    def tokenize_sentence(s):
        """ build customer tokenizer by lower case, lemmatize and remove stopwords """
        wordnet_lemmatizer = WordNetLemmatizer()
        # lower case
        s = s.lower()
        # strip punctuation
        s = s.translate(str.maketrans(string.punctuation, " " * len(string.punctuation)))
        # split string into words (tokens)
        tokens = s.split()
        # remove short words, they're probably not useful
        tokens = [t for t in tokens if len(t) > 2]
        # put words into base form
        tokens = [wordnet_lemmatizer.lemmatize(t) for t in tokens]
        # remove stopwords
        tokens = [t for t in tokens if t not in stopwords.words("english") + [""]]
        return tokens

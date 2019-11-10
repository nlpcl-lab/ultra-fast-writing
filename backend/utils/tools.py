import random
import string
import nltk
import numpy as np
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
porter=PorterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()
from nltk.corpus import stopwords
words = set(nltk.corpus.words.words())
from nltk import tokenize


def is_pos_determiner(pos_tag):
    if pos_tag == "DT":
        return True
    else:
        return False


def is_pos_prep_or_particle(pos_tag):

    if pos_tag in ["IN", "PDT", "RP", "TO"]:
        return True
    else:
        return False


def pos_tagging(sent):

    tokens = word_tokenize(sent)
    pos = nltk.pos_tag(tokens)

    """
    CC coordinating conjunction
    CD cardinal digit
        DT determiner
    EX existential there (like: “there is” … think of it like “there exists”)
    FW foreign word
        IN preposition/subordinating conjunction
    JJ adjective ‘big’
    JJR adjective, comparative ‘bigger’
    JJS adjective, superlative ‘biggest’
    LS list marker 1)
    MD modal could, will
    NN noun, singular ‘desk’
    NNS noun plural ‘desks’
    NNP proper noun, singular ‘Harrison’
    NNPS proper noun, plural ‘Americans’
        PDT predeterminer ‘all the kids’
    POS possessive ending parent’s
    PRP personal pronoun I, he, she
    PRP$ possessive pronoun my, his, hers
    RB adverb very, silently,
    RBR adverb, comparative better
    RBS adverb, superlative best
        RP particle give up
        TO, to go ‘to’ the store.
    UH interjection, errrrrrrrm
    VB verb, base form take
    VBD verb, past tense took
    VBG verb, gerund/present participle taking
    VBN verb, past participle taken
    VBP verb, sing. present, non-3d take
    VBZ verb, 3rd person sing. present takes
    WDT wh-determiner which
    WP wh-pronoun who, what
    WP$ possessive wh-pronoun whose
    WRB wh-abverb where, when
    """

    return pos

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def list_to_text_convert_for_n_gram_match(list_):
    text_ = " ".join(list_).replace("\n", "").replace("  ", " ")
    # text_ = remove_non_words(text_)
    text_ = " ".join(sent_tokenize(text_))
    text_ = " ".join(punct_tokenize(text_))
    text_ = remove_special_tokens(text_)
    for i in range(0, 10):
        text_ = text_.replace("  ", " ").strip()
    return text_


def punct_tokenize(sent_):
    return nltk.wordpunct_tokenize(sent_)


def most_common_element_in_list(List):
    return max(set(List), key=List.count)


def np_elementwise_multiplication(array_1, array_2):
    return np.multiply(array_1, array_2)


def np_array_to_list(array_):
    return array_.tolist()


def dict_merge_delete_duplicated_keys(dict_1, dict_2):
    for key_, val_ in dict_1.items():
        dict_2[key_] = val_
    return dict_2


def sentence_tokenize(sent_):
    list_ = tokenize.sent_tokenize(sent_)
    return list_


def convert_for_sentential_match(sent_):
    sent_ = remove_special_tokens(sent_).strip().lower()
    for i in range(1,3):
        sent_ = sent_.replace("  ", " ")
    
    return sent_


def remove_non_words(sent_):
    # sent_ = " ".join([w for w in nltk.wordpunct_tokenize(sent_) \
    #             if w.lower() in words or not w.isalpha()])
    sent_ = " ".join([w for w in nltk.word_tokenize(sent_) \
                      if w.lower() in words or not w.isalpha()])
    return sent_


def remove_non_words_punct(sent_):
    sent_ = " ".join([w for w in nltk.wordpunct_tokenize(sent_) \
                if w.lower() in words or not w.isalpha()])
    return sent_


def remove_stop_words(sent_):
    #list_ = nltk.wordpunct_tokenize(sent_)
    list_ = nltk.word_tokenize(sent_)
    filtered_ = [word for word in list_ if word not in stopwords.words('english')]
    sent_ = " ".join(filtered_)
    return sent_


def print_short_line():
    print("*"*33)
    return 1


def print_long_line():
    print("-"*77)
    return 1


def convert_list_to_str_list(list_, rounding=True):
    for idx, item in enumerate(list_):
        if rounding:
            if isinstance(item, float):
                list_[idx] = "{0:.2f}".format(item)
            else:
                list_[idx] = str(item)
        else:    
            list_[idx] = str(item)
    return list_


def combination(list_):
    result = []
    for p1 in range(len(list_)):
        for p2 in range(p1 + 1, len(list_)):
            result.append([list_[p1], list_[p2]])
    return result


def vector_distance(v1, v2):
    return np.linalg.norm(v1-v2)


def sentence_stemmize(str_):
    token_words=word_tokenize(str_)
    stem_sentence=[]
    for word in token_words:
        stem_sentence.append(porter.stem(word).strip())
        stem_sentence.append(" ")
    return "".join(stem_sentence).strip()


def sentence_lemmatize(str_):
    lemma_sentence = []
    sentence_words = nltk.word_tokenize(str_)
    for word in sentence_words:
        lemma_sentence.append(wordnet_lemmatizer.lemmatize(word).strip())
        lemma_sentence.append(" ")
    return "".join(lemma_sentence).strip()


def sentence_list_stemmize(list_):
    stemmized_list_ = []
    for sent in list_:
        stemmized_list_.append(sentence_stemmize(sent).strip())
    return stemmized_list_


def concatenate(list_, delimiter="n/a"):
    if delimiter == "n/a":
        delimiter = "___"
    concatenated_str = list_[0]
    for item_ in list_[1:]:
        concatenated_str += delimiter
        concatenated_str += item_
    return concatenated_str


def first_tokens(sent_ : str, num_ : int):
    _ = sent_.split(" ")[:num_]
    return " ".join(_)


def first_characters(sent_ : str, num_ : int):
    return sent_[:num_]


def remove_special_tokens(str_):
    special_tokens = [".", ",", "?", "/", ";", ":", "<", ">", "[", "]", "/", "|", "'", '"', "{", "}",
                      "-", "+", ")", "(", "_", "=", "!", "*", "&", "^", "%", "$", "#", "@", "~", "`",
                      "’", "“", "”", "–", "—"]
    for token_ in special_tokens:
        str_ = str_.replace(token_, "")
    return str_.strip()


def replace_special_tokens(str_):
    special_tokens = [".", ",", "?", "/", ";", ":", "<", ">", "[", "]", "/", "|", "'", '"', "{", "}",
                      "-", "+", ")", "(", "_", "=", "!", "*", "&", "^", "%", "$", "#", "@", "~", "`",
                      "’", "“", "”", "–", "—"]
    for token_ in special_tokens:
        str_ = str_.replace(token_, " ")
    return str_.strip().replace("  ", " ")


def isIncludedByOther(s1, s2):
    s1 = remove_special_tokens(s1)
    s2 = remove_special_tokens(s2)
    if s1 in s2:
        return True
    elif s2 in s1:
        return True
    else:
        return False


def dict_recursive_find(obj, key):
    if key in obj: return obj[key]
    for k, v in obj.items():
        if isinstance(v,dict):
            item = dict_recursive_find(v, key)
            if item is not None:
                return item


def print_list(list_, delimiter_="\n", length_limit=0, random_=False):
    if random_:
        random.shuffle(list_)
    if not length_limit == 0:
        list_ = list_[:length_limit]
    print("\n")
    for i in range(0, 4): print("-", end="")
    print("\n", end="")
    for idx_, val_ in enumerate(list_):    
        print("    "+ str(idx_) + ": ", str(val_) + delimiter_, end="")
        print("\n", end="")
    for i in range(0, 4): print("-", end="")
    print("\n")
    return 1


def print_dict(dict_, delimiter_="\n", length_limit=0, sorted_=True):
    keys_ = list(dict_.keys())
    if sorted_:
       keys_ = sorted(keys_)
    if not length_limit == 0:
        keys_ = keys_[:length_limit]
    print("\n")
    for i in range(0, 4): print("-", end="")
    print("\n", end="")
    for key_ in keys_:    
        print("    "+ str(key_) + ": ", str(dict_[key_]) + delimiter_, end="")
        print("\n", end="")
    for i in range(0, 4): print("-", end="")
    print("\n")
    return 1


def append_without_duplication(list_, val_):
    if val_ in list_:
        pass
    else:
        list_.append(val_)
    return list_


def add_without_duplication(dict_, key_, val_, type="list_"):
    if type == "list_":
        if key_ in dict_:
            dict_[key_] = append_without_duplication(dict_[key_], val_)
        else:
            dict_[key_] = append_without_duplication([], val_)
    else:
        raise KeyError
    return dict_


def add_allowing_duplication(dict_, key_, val_, type="list_"):
    if type == "list_":
        if key_ in dict_:
            dict_[key_].append(val_)
        else:
            dict_[key_] = [val_]
    else:
        raise KeyError
    return dict_


def random_string_generator(size, chars=string.ascii_uppercase + string.digits):
   return ''.join(random.choice(chars) for _ in range(size))


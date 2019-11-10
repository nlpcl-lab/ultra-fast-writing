import pprint
import sys
import utils.tools as tools
import numpy as np
import utils.file_control as file_control


class global_():

    def load_sentences(self):
        gutenberg = file_control.read_lines_dir("gutenberg.txt")

        sentences = gutenberg

        return sentences


def determiner_check(word, limit_len=100):

    sentences = global_().load_sentences()

    determiner_word2sentence = {}
    determiner_word2count = {}
    cnt = 0
    for sent in sentences:

        if cnt >= limit_len:
            break

        if not word.lower() in sent.lower():
            continue

        sent = sent.lower()
        word = word.lower()

        sent = tools.remove_non_words(sent)
        sent = tools.remove_special_tokens(sent)

        pos_tagged_sent = tools.pos_tagging(sent)

        for idx, tuple in enumerate(pos_tagged_sent):
            if idx == 0:
                continue

            token, pos_tag = tuple
            previous_token, previous_pos_tag = pos_tagged_sent[idx - 1]

            if token == word and tools.is_pos_determiner(previous_pos_tag):

                sent = sent.lower()
                sent = sent.replace(" " + token.lower() +
                                    " ", " " + token.upper() + " ")
                sent = sent.replace(
                    " " + previous_token.lower() + " ", " " + previous_token.upper() + " ")

                cnt += 1
                determiner_word2sentence = tools.add_allowing_duplication(determiner_word2sentence,
                                                                          tools.concatenate(
                                                                              [previous_token, token]),
                                                                          sent)

    for determiner_word, list_ in determiner_word2sentence.items():
        determiner_word2count[determiner_word] = len(list_)

    return determiner_word2count, determiner_word2sentence


def determiner_check_case_by_case(determiner, word, limit_len=100):

    _, determiner_word2sentence = determiner_check(word, limit_len=limit_len)

    determiner_word_usages = []
    key_ = tools.concatenate([determiner, word])
    if key_ in determiner_word2sentence:
        determiner_word_usages = determiner_word2sentence[key_]

    return determiner_word_usages


def check_word_usage(word, limit_len=10):

    sentences = global_().load_sentences()

    usage_list = []

    for idx, sent in enumerate(sentences):

        if not word.lower() in sent.lower():
            continue

        sent = sent.lower()
        word = word.lower()

        if len(usage_list) >= limit_len:
            break

        sent = tools.remove_non_words(sent)
        sent = tools.remove_special_tokens(sent)
        token_ = " " + word + " "
        if token_ in sent:
            sent = sent.replace(" " + word.lower() + " ",
                                " " + word.upper() + " ")

            if idx == 0:
                pass
            elif idx == 1:
                sent = sentences[idx-1].lower() + "\n" + sent

            elif idx == 2:
                sent = sentences[idx-1].lower() + "\n" + sent
                sent = sentences[idx-2].lower() + "\n" + sent
            else:
                sent = sentences[idx-1].lower() + "\n" + sent
                sent = sentences[idx-2].lower() + "\n" + sent
                sent = sentences[idx-3].lower() + "\n" + sent
            usage_list.append(sent)

    return usage_list


def check_phrase_usage(phrase, limit_len=10):

    sentences = global_().load_sentences()

    usage_list = []

    for idx, sent in enumerate(sentences):

        if not phrase.lower() in sent.lower():
            continue

        sent = sent.lower()
        phrase = phrase.lower()

        if len(usage_list) >= limit_len:
            break

        sent = tools.remove_non_words(sent)
        sent = tools.remove_special_tokens(sent)
        if phrase in sent:
            sent = sent.replace(phrase.lower(), phrase.upper())

            if idx == 0:
                pass
            elif idx == 1:
                sent = sentences[idx-1].lower() + "\n" + sent

            elif idx == 2:
                sent = sentences[idx-1].lower() + "\n" + sent
                sent = sentences[idx-2].lower() + "\n" + sent
            else:
                sent = sentences[idx-1].lower() + "\n" + sent
                sent = sentences[idx-2].lower() + "\n" + sent
                sent = sentences[idx-3].lower() + "\n" + sent
            usage_list.append(sent)

    return usage_list


def preposition_check(word, limit_len=100):
    sentences = global_().load_sentences()

    word_prep2sentence = {}
    word_prep2count = {}
    cnt = 0
    for sent in sentences:

        if cnt >= limit_len:
            break

        if not word.lower() in sent.lower():
            continue

        sent = sent.lower()
        word = word.lower()

        sent = tools.remove_non_words(sent)
        sent = tools.remove_special_tokens(sent)

        pos_tagged_sent = tools.pos_tagging(sent)

        for idx, tuple in enumerate(pos_tagged_sent):
            if idx == 0:
                continue

            token, pos_tag = tuple
            previous_token, previous_pos_tag = pos_tagged_sent[idx - 1]

            if previous_token == word and tools.is_pos_prep_or_particle(pos_tag):
                sent = sent.lower()
                sent = sent.replace(" " + token.lower() +
                                    " ", " " + token.upper() + " ")
                sent = sent.replace(
                    " " + previous_token.lower() + " ", " " + previous_token.upper() + " ")

                cnt += 1
                word_prep2sentence = tools.add_allowing_duplication(word_prep2sentence,
                                                                    tools.concatenate(
                                                                        [previous_token, token]),
                                                                    sent)

    for determiner_word, list_ in word_prep2sentence.items():
        word_prep2count[determiner_word] = len(list_)

    return word_prep2count, word_prep2sentence


def preposition_check_case_by_case(word, prep):

    _, word_prep2sentence = preposition_check(word)

    word_prep_usages = []
    key_ = tools.concatenate([word, prep])
    if key_ in word_prep2sentence:
        word_prep_usages = word_prep2sentence[key_]

    return word_prep_usages


if __name__ == "__main__":

    # prep_dict, _ = preposition_check("kill")
    # tools.print_dict(prep_dict)
    #
    prep_case_list = preposition_check_case_by_case("kill", "with")
    tools.print_list(prep_case_list)

    # det_dict, _ = determiner_check("person")
    # tools.print_dict(det_dict)
    #
    # det_case_list = determiner_check_case_by_case("a", "person")
    # tools.print_list(det_case_list)
    #
    # usage_list = check_word_usage("him")
    # tools.print_list(usage_list)
    # #
    # usage_list = check_phrase_usage("pray excuse me")
    # tools.print_list(usage_list)

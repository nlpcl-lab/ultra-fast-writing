import json
import codecs
import glob
import sys
import csv
csv.field_size_limit(sys.maxsize)


def get_file_list_in_dir(dir_, tail_= "", avoiding_phrase=""):
    list_ = glob.glob(dir_ + "/*" + tail_)
    if not avoiding_phrase:
        f_list = list_
    else:
        f_list=[]
        for _ in list_:
            if avoiding_phrase not in _:
                f_list.append(_)
    return f_list


def save_dict_list_to_json_file(dict_list_, dir_):
    with open(dir_, 'w') as f_:
        json.dump(dict_list_, f_,
                  indent=4, sort_keys=False, ensure_ascii=False)

    return 1


def read_file_at_once_dir(dir_,encoding="utf-8"):
    f_ = codecs.open(dir_,encoding=encoding)
    return f_.read()


def read_lines_dir(dir_,encoding="utf-8"):
    f_ = codecs.open(dir_,encoding=encoding)
    list_ = []
    for line in f_:
        list_.append(line.strip())
    f_.close()
    return list_


def print_plain_lines_to_file(list_, dir_):
    f_ = codecs.open(dir_, mode='w', encoding='utf8')
    for item in list_:
        print(item.strip(), file=f_)
    f_.close()
    return 1


def print_multiple_list_to_file(list_, dir_, delimiter="\t"):
    f_ = codecs.open(dir_, mode='w', encoding='utf8')
    for _ in list_:
        print(delimiter.join(_).strip(), file=f_)
    f_.close()


def json2list(dir_):
    with open(dir_) as json_file:
        list_ = json.load(json_file)
    return list_


def print_list_of_rows_to_csv_file(list_, f_name):
    import csv

    with open(f_name, mode='w') as f_out:
        f_writer = csv.writer(f_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for item in list_:
            f_writer.writerow(item)
    return 1


def csv_read(dir_):
    import csv
    matrix_ = []
    with open(dir_) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            matrix_.append(row)
    return matrix_



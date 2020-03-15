import json
import re


def clean_values(arg: list) -> set:
    """
    Function get list of values and clean it from not digit symbols.
    :param arg: list of values(value can be list)
    :return: set of unique string values
    """
    result = []
    for i in arg:
        if isinstance(i, list):
            result += clean_values(i)
        else:
            result.append("".join([j for j in str(i) if j.isdigit()]))
    return set(result)


def text_to_pin_code(text: str) -> str:
    """
    Function get raw text with encoded pin code, decode it, and return valid pin code.
    :param text: raw text
    :return: string - pin code
    """
    text_to_json = json.loads(re.search(r"{(.*)}", text).group(0))
    valid_values = [text_to_json[i] for i in text_to_json if i != i.lower()]  # list of values with valid keys
    set_list = [len(i) for i in clean_values(valid_values)]  # list ranks of unique numbers
    return "".join([str(set_list.count(i)) for i in range(1, 5)])  # count of ranks (1-4)

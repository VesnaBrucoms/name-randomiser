"""Main entry point."""
import json
import random
import sys

from .culture import Culture


def main(culture_key, gender=None):
    cultures = _get_cultures()
    chosen_culture = None
    for culture in cultures:
        if culture.key == culture_key:
            chosen_culture = culture

    print(chosen_culture.get_name(gender))


def _get_cultures():
    names_json = _read_file('./misc/names.json')
    cultures = []
    for culture_key, culture_dict in names_json.items():
        new_culture = Culture(culture_key, culture_dict)
        cultures.append(new_culture)
    return cultures


def _read_file(file_path):
    contents = None
    with open(file_path, mode='r') as name_file:
        contents = json.loads(name_file.read())
    return contents


if __name__ == '__main__':
    if len(sys.argv) == 3:
        culture_key = sys.argv[1]
        name_gender = sys.argv[2]
        main(culture_key, name_gender)
    else:
        print('Invalid number of arguments.')
        print('Usage:')
        print('name_randomiser culture_key gender')

"""Main entry point."""
import json
import random


def main(names_file_path, gender):
    names_json = _read_file(names_file_path)
    order = names_json['order']
    given_names = names_json['given']
    family_names = names_json['family']

    full_name = {}
    decide = random.randrange(0, 101)
    if decide > 0 and decide < 75:
        g_index = random.randrange(0, len(given_names[gender]))
        f_index = random.randrange(0, len(family_names))
        full_name = {
            'given': given_names[gender][g_index],
            'family': family_names[f_index]
        }
    else:
        g_index = random.randrange(0, len(given_names[gender]))
        m_index = random.randrange(0, len(given_names[gender]))
        f_index = random.randrange(0, len(family_names))
        full_name = {
            'given': '{} {}'.format(given_names[gender][g_index], given_names[gender][m_index]),
            'family': family_names[f_index]
        }

    if order == "western":
        print('{} {}'.format(full_name['given'], full_name['family']))
    elif order == "eastern":
        print('{} {}'.format(full_name['family'], full_name['given']))


def _read_file(file_path):
    contents = None
    with open(file_path, mode='r') as name_file:
        contents = json.loads(name_file.read())
    return contents


if __name__ == '__main__':
    main('./misc/names.json', 'male')
    main('./misc/names.json', 'female')

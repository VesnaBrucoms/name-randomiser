"""Main entry point."""
import json
import random

from .culture import Culture


def main(culture_list, culture_name, gender=None):
    chosen_culture = None
    for culture in culture_list:
        if culture.key == culture_name:
            chosen_culture = culture

    # full_name = {}
    # decide = random.randrange(0, 101)
    # if decide > 0 and decide < 75:
    #     g_index = random.randrange(0, len(chosen_culture[gender]))
    #     f_index = random.randrange(0, len(chosen_culture['family']))
    #     full_name = {
    #         'given': chosen_culture[gender][g_index],
    #         'family': chosen_culture['family'][f_index]
    #     }
    # else:
    #     g_index = random.randrange(0, len(chosen_culture[gender]))
    #     m_index = random.randrange(0, len(chosen_culture[gender]))
    #     f_index = random.randrange(0, len(chosen_culture['family']))
    #     full_name = {
    #         'given': '{} {}'.format(chosen_culture[gender][g_index],
    #                                 chosen_culture[gender][m_index]),
    #         'family': chosen_culture['family'][f_index]
    #     }

    print(chosen_culture.get_name(gender))


def _read_file(file_path):
    contents = None
    with open(file_path, mode='r') as name_file:
        contents = json.loads(name_file.read())
    return contents


if __name__ == '__main__':
    names_json = _read_file('./misc/names.json')
    cultures = []
    for culture_key, culture_dict in names_json.items():
        cultures.append(Culture(culture_key, culture_dict))
    main(cultures, 'british', 'male')
    main(cultures, 'british', 'female')
    main(cultures, 'japanese', 'female')

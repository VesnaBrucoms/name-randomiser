"""Main entry point."""
import json
import random


def main(names_file_path, gender):
    names_dict = _read_file(names_file_path)

    full_name = ''
    decide = random.randrange(0, 101)
    if decide > 0 and decide < 75:
        g_index = random.randrange(0, len(names_dict[gender]))
        f_index = random.randrange(0, len(names_dict['family']))
        full_name = '{} {}'.format(names_dict[gender][g_index],
                                   names_dict['family'][f_index])
    else:
        g_index = random.randrange(0, len(names_dict[gender]))
        m_index = random.randrange(0, len(names_dict[gender]))
        f_index = random.randrange(0, len(names_dict['family']))
        full_name = '{} {} {}'.format(names_dict[gender][g_index],
                                      names_dict[gender][m_index],
                                      names_dict['family'][f_index])

    print(full_name)


def _read_file(file_path):
    contents = None
    with open(file_path, mode='r') as name_file:
        contents = json.loads(name_file.read())
    return contents


if __name__ == '__main__':
    main('./misc/names.json', 'male')
    main('./misc/names.json', 'female')

"""Main entry point."""
import random


def main(given_name_file, family_name_file):
    given_names = _read_file(given_name_file)
    family_names = _read_file(family_name_file)

    full_name = ''
    decide = random.randrange(0, 101)
    if decide > 0 and decide < 75:
        g_index = random.randrange(0, len(given_names))
        f_index = random.randrange(0, len(family_names))
        full_name = '{} {}'.format(given_names[g_index],
                                   family_names[f_index])
    else:
        g_index = random.randrange(0, len(given_names))
        m_index = random.randrange(0, len(given_names))
        f_index = random.randrange(0, len(family_names))
        full_name = '{} {} {}'.format(given_names[g_index],
                                      given_names[m_index],
                                      family_names[f_index])

    print(full_name)


def _read_file(file_path):
    contents = None
    with open(file_path, mode='r') as name_file:
        contents = name_file.read()
    return contents.split('\n')


if __name__ == '__main__':
    main('./misc/given_names.txt', './misc/family_names.txt')

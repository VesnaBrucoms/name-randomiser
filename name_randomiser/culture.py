"""Defines the Culture class."""
import random


class Culture():

    def __init__(self, key, culture_dict):
        self._key = key
        self._culture_name = culture_dict['name']
        self._order = culture_dict['order']

        self._given_names = culture_dict['given']
        self._dynasty_names = culture_dict['family']

    def __getitem__(self, key):
        if key == 'dynasty' or key == 'family':
            return self._dynasty_names
        else:
            return self._given_names[key]

    def __str__(self):
        return '{} {} given names, {} dynastic names'.format(self._key,
                                                             len(self._given_names['male']) +
                                                             len(self._given_names['female']),
                                                             len(self._dynasty_names))

    def __repr__(self):
        return '<{} {}: {}>'.format(__name__, self._key, self._culture_name)

    @property
    def key(self):
        """Get the culture's identifier."""
        return self._key

    @property
    def name(self):
        """Get the culture's name."""
        return self._culture_name

    @property
    def order(self):
        """Get the culture's name ordering."""
        return self._order

    def get_name(self, gender):
        g_index = random.randrange(0, len(self[gender]))
        d_index = random.randrange(0, len(self['dynasty']))
        full_name = ''
        if self._order == 'eastern':
            full_name = '{} {}'.format(self['dynasty'][d_index], self[gender][g_index])
        else:
            full_name = '{} {}'.format(self[gender][g_index], self['dynasty'][d_index])

        return full_name

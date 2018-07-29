"""Defines the Culture class."""
import random


class Culture():

    gender_min = 0
    gender_max = 100
    gender_split = 50

    def __init__(self, key, culture_dict):
        self._key = key
        self._culture_name = culture_dict.get('name', key)
        self._order = culture_dict.get('order', 'given')

        self._given_names = culture_dict['given']
        self._family_names = culture_dict['family']

    def __getitem__(self, key):
        if key == 'family':
            return self._family_names
        else:
            return self._given_names[key]

    def __str__(self):
        msg = '{} culture: {} given names, {} dynastic names'
        return msg.format(self._culture_name,
                          len(self._given_names['male']) +
                          len(self._given_names['female']),
                          len(self._family_names))

    def __repr__(self):
        msg = '<{} {}: {}>'
        return msg.format(__name__, self._key, self._culture_name)

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
        if not gender:
            gender = self._set_gender()
        given = self._get_given_name(gender)
        family = self._get_family_name()
        full_name = '{} {}'
        if self._order == 'family':
            full_name = full_name.format(family, given)
        else:
            full_name = full_name.format(given, family)

        return full_name

    def _set_gender(self):
        gender_rand = random.randrange(self.gender_min, self.gender_max)
        if gender_rand < self.gender_split:
            return 'male'
        else:
            return 'female'

    def _get_given_name(self, gender):
        return random.choice(self[gender])

    def _get_family_name(self):
        return random.choice(self['family'])

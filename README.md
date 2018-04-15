# Name Randomiser

*Selects names from multiple lists at random to build a full name.*

## Planned Functionality

Initial this will be a CLI utility that:

* Requires one arg: culture to generate name from
* Has one optional arg: gender
    * If unset, it will pick a gender at random
* Can generate full names with up to 4 given names (excluding family)
    * Longer names will appear less frequently
* Cultures can specify:
    * Male names
    * Female names
    * Family/dynasty names
    * Name order (family name comes either first or last)
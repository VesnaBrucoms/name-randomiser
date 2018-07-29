# Name Randomiser

*Selects names from multiple lists at random to build a full name.*

## Current functionality

Name Randomiser is a CLI utility that:

* Requires arguments:
    * Culture key to generate name from
* Optional arguments:
    * Gender, if unset it will pick a gender at random
* A Culture can specify:
    * Male given names
    * Female given names
    * Family/dynasty names
    * Name order (place family name first or last)
* Cultures are defined in a JSON file

## Planned Functionality

For a first release this will be a CLI utility that:

* ~~Requires arguments~~:
    * ~~Culture key to generate name from~~
* ~~Optional arguments~~:
    * ~~Gender, if unset it will pick a gender at random~~
* ~~Cultures can specify~~:
    * ~~Male given names~~
    * ~~Female given names~~
    * ~~Family/dynasty names~~
    * ~~Name order (place family name first or last)~~
    * Maximum number of given names
        * Longer names will appear less frequently
* Stores a separate `settings.json` with user preferences:
    * order: given or family

Future features:

* Cultures can specify:
    * to allow multi barrelled names
    * to allow dual family names

## Cultures File

Entries italisiced are part of future features, and may be subject to change:

* culture key
    * name (optional)
    * order (optional, default=given)
    * max_names (optional, default=1)
    * _double-barrelled names (optional, default=true)_
    * _dual family names (optional, default=false)_
    * given names
        * male
        * female
    * family names
"""
Library that inflects given noun in Serbian language into all of its forms.
Required inputs are: singular and plural in nominative, gender.
"""

import group_f_c
import exceptions

from collections import Counter as mset
from enum import Enum

VOWELS = ('а', 'е', 'и', 'о', 'у')


class Gender(Enum):
    """ Gramatical gender """
    M = 1
    F = 2
    N = 3


class DeclinationGroup(Enum):
    """ Declination group noun belongs to. """
    # m, ending in consonant, -о and -е
    # n, ending in -о and -е, and where stem stays the same
    GROUP_MN_COE = 1
    # n, ending in -е and stem gains n or t in all cases except nominative
    GROUP_N_E_NT = 2
    # any gender, ending in -а
    GROUP_MFN_A = 3
    # f, ending in consonant (and associated adjective is female - we ignore this)
    GROUP_F_C = 4


def inflect_noun(singular, options):
    """ Takes singular nominative of the noun and additional options.
        Returns an array with cases in singular followed by plural.
    """
    try:
        # Try exceptions list first.
        result = exceptions.return_exception(singular)
        if result != None:
            return result
        # Otherwise try to classify noun type and call appropriate handler.
        group = classify_noun(singular, options)
        if group == DeclinationGroup.GROUP_MN_COE:
            print('MN_COE')
        elif group == DeclinationGroup.GROUP_N_E_NT:
            print('N_E_NT')
        elif group == DeclinationGroup.GROUP_MFN_A:
            print('MFN_A')
        else:
            return group_f_c.inflect(singular)
    except:
        # Let caller decide whether to bail or to continue.
        raise


def classify_noun(singular, options):
    """ Classifies noun into one of the four declination groups. """
    if options['gender'] == Gender.F and ends_with_consonant(singular):
        return DeclinationGroup.GROUP_F_C

    if singular.endswith('а'):
        return DeclinationGroup.GROUP_MFN_A

    if options['gender'] == Gender.N and singular.endswith('е') \
            and has_extra_nt(singular, options['plural']):
        return DeclinationGroup.GROUP_N_E_NT

    if (options['gender'] == Gender.M and ends_with_consonant(singular)) or \
       (options['gender'] in [Gender.N, Gender.M] and (singular.endswith(('о', 'е')))):
        return DeclinationGroup.GROUP_MN_COE

    raise ValueError("Unknown noun declination group.",
                     singular, options)


def ends_with_consonant(noun):
    """ Returns true if string ends with consonant. """
    return not noun.endswith(VOWELS)


def has_extra_nt(singular, plural):
    """ Returns true if non-nominative forms add n or t. """
    difference = mset(plural) - mset(singular)
    return difference['н'] != 0 or difference['т'] != 0

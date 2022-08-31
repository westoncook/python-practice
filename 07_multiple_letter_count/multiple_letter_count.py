def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    counts = {}
    for char in phrase:
        if counts.get(char):
            counts[char] += 1 
        else :
            counts[char] = 1
    return counts
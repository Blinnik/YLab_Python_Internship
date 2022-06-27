from itertools import combinations


def bananas(s) -> set:
    result = set()
    # Word "banana" has 6 letters.
    # We need to calculate the number of skipped letters.
    for combo in combinations(range(len(s)), len(s) - 6):
        # 'str' object does not support item assignment
        one_result = list(s)
        for skipped_letter in combo:
            one_result[skipped_letter] = '-'
        # Turning back into a string type
        one_result = ''.join(one_result)
        if one_result.replace('-', '') == 'banana':
            result.add(one_result)
    return result

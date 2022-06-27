from itertools import combinations_with_replacement


def mul(nums):
    result = 1
    for i in range(len(nums)):
        result *= nums[i]
    return result


def count_find_num(primesL, limit):
    if primesL == []:
        return []
    result = set()

    # Determine the maximum number of factors
    # in order to correctly set the range later

    max_factors = 0
    multiplication = 1
    for i in primesL:
        if i != min(primesL):
            multiplication *= i
            max_factors += 1
    while 1:
        multiplication *= min(primesL)
        if multiplication > limit:
            break
        max_factors += 1

    # Selection of needed values

    for factors_count in range(len(primesL), max_factors + 1):
        for combo in combinations_with_replacement(primesL, factors_count):

            # A condition that checks for the presence
            # of all letters from the source list

            check_elements = list(
                set(combo).symmetric_difference(set(primesL)))
            if check_elements == [] and mul(combo) <= limit:
                result.add(mul(combo))
    if len(result) < 1:
        return []
    else:
        return [len(result), max(result)]

def import_data(year, day):
    with open('../../input/'+str(year)+'/day'+str(day), 'r') as input_raw:
        input_list = input_raw.read().split('\n')
    return input_list


def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1

    return factors


def lcm(nums):
    prime_dict = {}
    for num in nums:
        factor_dict = {}
        for factor in prime_factors(num):
            if factor in factor_dict.keys():
                factor_dict[factor] += 1
            else:
                factor_dict[factor] = 1

        for factor in factor_dict.keys():
            if factor in prime_dict.keys():
                prime_dict[factor] = max(prime_dict.get(factor), factor_dict.get(factor))
            else:
                prime_dict[factor] = factor_dict.get(factor)

    res = 1
    for factor in prime_dict.keys():
        res *= factor ** prime_dict[factor]

    return res

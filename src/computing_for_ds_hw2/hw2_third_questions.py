def total_registered_cases(dic: dict, country: str) -> int:
    """
    7)
    Create a function called "total_registered_cases" that has 2 parameters:
    1) The data structure described above.
    2) A string with the country name.

    The function should return the total number of cases
    registered so far in that country
    """

    return sum(dic[country])

def total_registered_cases_per_country(dic: dict) -> dict:
    """
    8)
    Create a function called "total_registered_cases_per_country"
    that has 1 parameter:
    1) The data structure described above.

    The function should return a dictionary with a key
    per each country and as value the total number of cases
    registered so far that the country had
    """

    result_dict = {}

    for country in dic:
        result_dict[country] = total_registered_cases(dic, country)

    return result_dict

def country_with_most_cases(dic: dict) -> str:
    """
    9)
    Create a function called "country_with_most_cases"
    that has 1 parameter:
    1) The data structure described above

    The function should return the country with the
    greatest total amount of cases
    """

    total_cases = total_registered_cases_per_country(dic)

    return max(total_cases, key=total_cases.get)

if __name__ == "__main__":

    # Tests
    example_dic = {"Spain": [1, 24, 2, 5, 2, 9], "Singapore": [2, 45, 1, 5, 2, 4], "Slovakia": [4, 2, 6, 2, 4, 7, 9]}

    print(total_registered_cases(example_dic, "Spain"))
    print(total_registered_cases_per_country(example_dic))
    print(country_with_most_cases(example_dic))

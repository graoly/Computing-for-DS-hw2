def total_registered_cases(dic: dict, country: str) -> int:
    """
    7)
    Create a function called "total_registered_case" that has 2 parameters:
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
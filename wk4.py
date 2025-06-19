# TASK 1

def sort_dicts_by_key(dict_list, sort_key, reverse=False):
    """
    Sorts a list of dictionaries by a specified key.

    Args:
        dict_list (list): List of dictionaries to sort.
        sort_key (str): The key to sort the dictionaries by.
        reverse (bool): Sort in descending order if True. Default is False (ascending).

    Returns:
        list: A new list of dictionaries sorted by the specified key.
    """
    return sorted(dict_list, key=lambda x: x.get(sort_key, None), reverse=reverse)

data = [
    {'name': 'Queenie Quantum', 'role': 'Lead Sorceress of Code', 'age': 28, 'skills': ['Python', 'React', 'Spellcasting']},
    {'name': 'Ruby Royale', 'role': 'Empress of Algorithms', 'age': 32, 'skills': ['Ruby', 'Machine Learning', 'Crown Design']},
    {'name': 'Duchess Devina', 'role': 'Backend Baroness', 'age': 27, 'skills': ['Django', 'SQL', 'Castle Automation']},
    {'name': 'Countess Cloudia', 'role': 'Cloud Queen', 'age': 29, 'skills': ['AWS', 'Docker', 'Throne Scaling']},
    {'name': 'Princess Pipeline', 'role': 'CI/CD Princess', 'age': 31, 'skills': ['GitHub Actions', 'Bash', 'Royal Deployments']}
]
sorted_data = sort_dicts_by_key(data, 'age')
print(sorted_data)
# Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]
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

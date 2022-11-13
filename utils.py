def reverse_mapping(dictionary):
    reversed_dict = dict([(v, k) for k, v in dictionary.items()])
    return reversed_dict

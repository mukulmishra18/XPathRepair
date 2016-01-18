def chainFunctions(func_list, value):
    if len(func_list) is 1:
        return func_list[0](value)
    return chainFunctions(func_list[1:], func_list[0](value))


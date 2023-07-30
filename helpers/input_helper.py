def enter_list_of_(_type, _input_message=""):
    return list(map(
        _type, input(_input_message).strip().split()
    ))

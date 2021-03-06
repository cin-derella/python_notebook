"""Various validators"""


def validate_integer(
        arg_name,arg_value,min_value = None,max_value = None,
        custom_min_message = None, custom_max_message = None
):
    """

    Args:
        arg_name:
        arg_value:
        min_value:
        max_value:
        custom_min_message:
        custom_max_message:
    """
    if not isinstance(arg_value,int):
        raise TypeError(f'{arg_name} must be an integer.')

    if min_value is not None and arg_value < min_value:
        if custom_min_message is not None:
            raise ValueError(custom_min_message)
        raise ValueError(f'{arg_name} cant be less than {min_value}')

    if max_value is not None and arg_value > max_value:
        if custom_max_message is not None:
            raise  ValueError(custom_max_message)
        raise ValueError(f'{arg_name} cant be greater than {max_value}')



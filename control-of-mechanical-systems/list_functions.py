def scalar_times_list(scalar=1, data_list=[]) -> list:
    """Multiplies each value in list by the scalar
    
    args:
        scalar: number, value to multiply list by
        data_list: list[number], list of int or floats
    
    returns:
        list[nubmer]: original list scaled by the scalar factor
    """
    return [scalar * x for x in data_list]

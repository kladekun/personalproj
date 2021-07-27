def slices(series, length):
    if len(series) < length or length <= 0:
        raise ValueError("Invalid Input")
    slice_list = []
    for i in range(0, len(series)):
        slice = series[i: i + length]
        if len(slice) == length:
            slice_list.append(slice)
    return slice_list

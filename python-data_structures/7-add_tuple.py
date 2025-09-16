#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Handle tuple_a: get first two elements or use 0 for missing ones
    if len(tuple_a) >= 2:
        a1, a2 = tuple_a[0], tuple_a[1]
    elif len(tuple_a) == 1:
        a1, a2 = tuple_a[0], 0
    else:
        a1, a2 = 0, 0
    
    # Handle tuple_b: get first two elements or use 0 for missing ones
    if len(tuple_b) >= 2:
        b1, b2 = tuple_b[0], tuple_b[1]
    elif len(tuple_b) == 1:
        b1, b2 = tuple_b[0], 0
    else:
        b1, b2 = 0, 0
    
    # Return tuple with addition of corresponding elements
    return (a1 + b1, a2 + b2)

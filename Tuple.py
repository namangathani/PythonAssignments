intTuple = (1, 22, 88, 44, 5)
print("Tuple Items = ", intTuple)

intTuple = intTuple + (77,)
print("Tuple Items = ", intTuple)

intTuple = intTuple + (80, 9)
print("Tuple Items = ", intTuple)

intTuple = intTuple[2:5] + (11, 22, 33, 44) + intTuple[7:]
print("Tuple Items = ", intTuple)
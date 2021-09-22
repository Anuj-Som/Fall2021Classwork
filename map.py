# Map from one linear range to another
# Input: two coordinate tuples, an x value
# Output: a y-value mapping from coord1 to coord2

def calculateMap(coord1, coord2, x):
    return (x - coord1[0])*(coord2[1]-coord2[0])/
    (coord1[1]-coord1[0])+coord1[0]


if __name__ == "__main__":
    x = float(input("Input percent to turn into fraction: "))
    print(calculateMap((0, 100), (0, 1), x))

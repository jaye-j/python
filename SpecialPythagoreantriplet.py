def check_triplet(a, b, c):
    return (a**2)+(b**2) == (c**2)

limit = 1000

for x in range(1, limit):
    for y in range(x+1, limit):
        z = limit - (x + y)
        if(check_triplet(x, y, z)):
            if x + y + z == limit:
                print(x)
                print(y)
                print(z)
                print(x * y * z)
                break
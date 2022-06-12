def get_code(order):
    first_code = 20151125
    mult_coeff = 252533
    mod_coeff = 33554393
    code = first_code
    for _ in range(order - 1):
        code = (code * mult_coeff) % mod_coeff
    return code


def get_order(coord):
    return sum(range(sum(coord) - 1)) + coord[1]


if __name__ == "__main__":
    coord = (2981, 3075)
    code = get_code(get_order(coord))
    print(f"Part 1: the Code is: {code}.")

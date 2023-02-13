with open("input.txt", "r") as file:
    contents = file.read().split()
    names = contents[::3]
    products = contents[1::3]
    quantities = [int(x) for x in contents[2::3]]
    dct = {}
    for name, product, quantity in zip(names, products, quantities):
        if name not in dct:
            dct[name] = {}
        if product not in dct[name]:
            dct[name][product] = []
        dct[name][product] += [quantity]
    dct = dict(sorted(dct.items()))
    for name in dct:
        for product in dct[name]:
            dct[name][product] = sum(dct[name][product])
    for name in dct:
        dct[name] = dict(sorted(dct[name].items()))
    for name in dct:
        print(name + ":")
        for product in dct[name]:
            quantity = dct[name][product]
            print(f"{product} {quantity}")

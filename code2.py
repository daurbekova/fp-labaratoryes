def f(data):
    def f2(d):
        dict = d.copy()
        if 'val' in dict:
            dict['val'] += 10
        return dict
    d2 = list(map(f2, data))
    return d2
d = [{'name': 'Umida', 'val': 1}, {'name': 'Damira', 'val': 20}]
d2 = f(d)
print("Original:", d)
print("data - 2:", d2)

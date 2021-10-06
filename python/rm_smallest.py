def rm_smallest(d):
    if len(d) == 0:
        return d
    min_value = 20
    for key in d.keys():
        if d[key] < min_value:
            min_value = d[key]
            min_key = key
    del d[min_key]
    return d

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()
def triple (x):
    return x * 3

def subtract (x, y):
    return x - y

def dictionary_maker (pairs):
    result = {}
    for key, value in pairs:
        result[key] = value
    return result

if __name__ == "__main__":
    print(triple(4))
    print(subtract(40,30))
    print(dictionary_maker([("foo", 1), ("bar", 3), ("hi", 5)]))

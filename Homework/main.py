def nod(a, b):
    if a <= 0 or b <= 0:
        return 0
    
    while b != 0:
        temp = b
        b = a % b
        a = temp
    
    return a


if __name__ == "__main__":
    test_positive()
    test_negative()
    print("Everything passed")
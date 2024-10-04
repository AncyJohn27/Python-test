def even_odd():
    list1 = ["1,2,3,4,5,6,7,8"]
    even = {}
    odd = {}
    for x in list1:
        if x % 2 == 0:
            even.update(x)
            print(even)
        elif x % 2 != 0:
            odd.update(x)
    print(odd, even)
even_odd()

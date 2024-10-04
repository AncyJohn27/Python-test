def character_frequency():
    string = "hellooo"
    count = {}
    for char in string:
        if char in count:
            count[char]+=1
        else:
            count[char]=1
    print("charcter count=", count)
character_frequency()
def main():
    s = input("Enter a string ")
    swap(s)

def swap(st):
    """
    This function swap lower case letter for uppercase
    case letter
    input: A string
    """
    new = []
    for i in st:
        if i.islower():
            new.append(i.upper())
        else:
            new.append(i.lower())
    print(new)
    new = "".join(new)
    print(new)
    return new

main()

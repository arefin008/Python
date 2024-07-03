try:
    my_list = [1, 2, 3]
    index = int(input("Enter an index: "))
    result = my_list[index]
except IndexError:
    print("Error: Index is out of range.")
except ValueError:
    print("Error: Index must be an integer.")

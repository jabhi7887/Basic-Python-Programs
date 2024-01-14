def string_methods():
    string = input("Enter a string: ")
    while True:
        print("\nString Methods Menu:")
        print("1. capitalize()")
        print("2. upper()")
        print("3. lower()")
        print("4. isupper()")
        print("5. islower()")
        print("6. count()")
        print("7. find()")
        print("8. replace()")
        print("9. split()")
        print("10. join()")

        choice = input("\nEnter your choice (1-10): ")
        if choice == "1":
            print("capitalize():", string.capitalize())
        elif choice == "2":
            print("upper():", string.upper())
        elif choice == "3":
            print("lower():", string.lower())
        elif choice == "4":
            print("isupper():", string.isupper())
        elif choice == "5":
            print("islower():", string.islower())
        elif choice == "6":
            sub_string = input("Enter a sub-string: ")
            print("count():", string.count(sub_string))
        elif choice == "7":
            sub_string = input("Enter a sub-string: ")
            print("find():", string.find(sub_string))
        elif choice == "8":
            old_sub_string = input("Enter the sub-string to replace: ")
            new_sub_string = input("Enter the new sub-string: ")
            print("replace():", string.replace(old_sub_string, new_sub_string))
        elif choice == "9":
            string1=input("Enter String with delimeter in between to perform split")
            delimiter = input("Enter the delimiter: ")
            print("split():", string1.split(delimiter))
        elif choice == "10":
            delimiter = input("Enter the delimiter: ")
            print("join():", delimiter.join(string))
        else:
            break

def tuple_methods():
    my_tuple = eval(input("Enter a tuple (e.g., (1, 2, 3)): "))
    while True:
        print("\nTuple Methods Menu:")
        print("1. count()")
        print("2. index()")
        print("3. len()")
        print("4. max()")
        print("5. min()")
        print("6. sum()")
        print("7. sorted()")
        print("8. any()")
        print("9. all()")
        print("10. reversed()")

        choice = input("\nEnter your choice (1-10): ")
        if choice == "1":
            element = eval(input("Enter an element: "))
            print("count():", my_tuple.count(element))
        elif choice == "2":
            element = eval(input("Enter an element: "))
            print("index():", my_tuple.index(element))
        elif choice == "3":
            print("len():", len(my_tuple))
        elif choice == "4":
            print("max():", max(my_tuple))
        elif choice == "5":
            print("min():", min(my_tuple))
        elif choice == "6":
            print("sum():", sum(my_tuple))
        elif choice == "7":
            print("sorted():", sorted(my_tuple))
        elif choice == "8":
            print("any():", any(my_tuple))
        elif choice == "9":
            print("all():", all(my_tuple))
        elif choice == "10":
            print("reversed():", tuple(reversed(my_tuple)))
        else:
            break

while True:
    print("\nMenu:")
    print("1. String Methods")
    print("2. Tuple Methods")
    print("3. Exit")

    option = input("\nEnter your choice (1-3): ")
    if option == "1":
        string_methods()
    elif option == "2":
        tuple_methods()
    elif option == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

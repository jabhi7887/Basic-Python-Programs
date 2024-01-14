def list_methods():
    my_list = list(eval(input("Enter a list (e.g., [1, 2, 3]): ")))
    while True:
        print("\nList Methods Menu:")
        print("1. Access an element by index")
        print("2. Check if an element exists in the list")
        print("3. Find the length of the list")
        print("4. Concatenate two lists")
        print("5. Count the occurrences of an element")
        print("6. Remove an element by value")
        print("7. Sort the list in ascending order")
        print("8. Reverse the elements of the list")
        print("9. Copy the list")
        print("10. Clear the list")

        choice = input("\nEnter your choice (1-10): ")
        if choice == "1":
            index = eval(input("Enter the index: "))
            if 0 <= index < len(my_list):
                print("Element at index", index, ":", my_list[index])
            else:
                print("Invalid index.")
        elif choice == "2":
            element = eval(input("Enter an element to check: "))
            if element in my_list:
                print(element, "exists in the list.")
            else:
                print(element, "does not exist in the list.")
        elif choice == "3":
            print("Length of the list:", len(my_list))
        elif choice == "4":
            another_list = eval(input("Enter another list: "))
            concatenated_list = my_list + another_list
            print("Concatenated List:", concatenated_list)
        elif choice == "5":
            element = eval(input("Enter an element to count: "))
            count = my_list.count(element)
            print("Occurrences of", element, ":", count)
        elif choice == "6":
            element = eval(input("Enter an element to remove: "))
            if element in my_list:
                my_list.remove(element)
                print("Element", element, "removed.")
                print("Updated List:", my_list)
            else:
                print("Element", element, "not found in the list.")
        elif choice == "7":
            my_list.sort()
            print("Sorted List:", my_list)
        elif choice == "8":
            my_list.reverse()
            print("Reversed List:", my_list)
        elif choice == "9":
            list_copy = my_list.copy()
            print("Copied List:", list_copy)
        elif choice == "10":
            my_list.clear()
            print(list(my_list))
            print("List cleared.")
        else:
            print("Invalid choice. Please try again.")

def set_methods():
    my_set = eval(input("Enter a set (e.g., {1, 2, 3}): "))
    print("\nSet Methods Menu:")
    print("1. Add an element to the set")
    print("2. Remove an element from the set")
    print("3. Check if an element exists in the set")
    print("4. Find the length of the set")
    print("5. Create a union of two sets")
    print("6. Create an intersection of two sets")
    print("7. Create a difference between two sets")
    print("8. Create a symmetric difference between two sets")
    print("9. Check if a set is a subset of another set")
    print("10. Check if a set is a superset of another set")

    choice = input("\nEnter your choice (1-10): ")
    if choice == "1":
        element = eval(input("Enter an element to add: "))
        my_set.add(element)
        print("Updated Set:", my_set)
    elif choice == "2":
        element = eval(input("Enter an element to remove: "))
        if element in my_set:
            my_set.remove(element)
            print("Element", element, "removed.")
            print("Updated Set:", my_set)
        else:
            print("Element", element, "not found in the set.")
    elif choice == "3":
        element = eval(input("Enter an element to check: "))
        if element in my_set:
            print(element, "exists in the set.")
        else:
            print(element, "does not exist in the set.")
    elif choice == "4":
        print("Length of the set:", len(my_set))
    elif choice == "5":
        another_set = eval(input("Enter another set: "))
        union_set = my_set.union(another_set)
        print("Union Set:", union_set)
    elif choice == "6":
        another_set = eval(input("Enter another set: "))
        intersection_set = my_set.intersection(another_set)
        print("Intersection Set:", intersection_set)
    elif choice == "7":
        another_set = eval(input("Enter another set: "))
        difference_set = my_set.difference(another_set)
        print("Difference Set:", difference_set)
    elif choice == "8":
        another_set = eval(input("Enter another set: "))
        symmetric_difference_set = my_set.symmetric_difference(another_set)
        print("Symmetric Difference Set:", symmetric_difference_set)
    elif choice == "9":
        another_set = eval(input("Enter another set: "))
        if my_set.issubset(another_set):
            print("The set is a subset of the other set.")
        else:
            print("The set is not a subset of the other set.")
    elif choice == "10":
        another_set = eval(input("Enter another set: "))
        if my_set.issuperset(another_set):
            print("The set is a superset of the other set.")
        else:
            print("The set is not a superset of the other set.")
    else:
        print("Invalid choice. Please try again.")

while True:
    print("\nMenu:")
    print("1. List Methods")
    print("2. Set Methods")
    print("3. Exit")

    option = input("\nEnter your choice (1-3): ")
    if option == "1":
        list_methods()
    elif option == "2":
        set_methods()
    elif option == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

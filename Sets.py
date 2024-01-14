def set_manager_program():
    sets = {'A': {1, 3, 5, 9}, 'B': {2, 3, 4, 6, 7}}

    def display_set(set_names):
        for set_name in set_names.split():
            if set_name.lower() == 'all':
                for name, values in sets.items():
                    print(f"Set '{name}': {values}")
            elif set_name in sets:
                print(f"Set '{set_name}': {sets[set_name]}")
            else:
                print(f"Set '{set_name}' not found.")

    def create_set(set_name):
        sets[set_name] = set()

    def add_element(set_name, element):
        sets[set_name].add(element)

    def remove_element(set_name, element):
        sets[set_name].discard(element)

    def get_cardinality(set_name):
        return len(sets[set_name])

    def perform_operation(set_name1, set_name2, operation):
        set1 = sets[set_name1]
        set2 = sets[set_name2]
        result_set = getattr(set1, operation)(set2)  # getting the attribute of the set
        print(f"Result of {operation}({set_name1}, {set_name2}): {result_set}")

    def is_disjoint(set_name1, set_name2):
        return sets[set_name1].isdisjoint(sets[set_name2])

    def is_subset(set_name1, set_name2):
        return sets[set_name1].issubset(sets[set_name2])

    def is_superset(set_name1, set_name2):
        return sets[set_name1].issuperset(sets[set_name2])

    def get_create_set_input():
        set_name = input("Enter set name: ")
        create_set(set_name)
        print(f"Set '{set_name}' created successfully.")

    def get_add_element_input():
        set_name = input("Enter set name: ")
        element = input("Enter element to add (or 'exit' to stop adding): ")

        while element.lower() != 'exit':
            add_element(set_name, element)
            print(f"'{element}' added to set '{set_name}'.")
            element = input("Enter another element to add (or 'exit' to stop adding): ")

    def get_remove_element_input():
        set_name = input("Enter set name: ")
        element = input("Enter element to remove: ")
        remove_element(set_name, element)
        print(f"'{element}' removed from set '{set_name}'.")

    def get_set_operation_input():
        set_name1 = input("Enter first set name: ")
        set_name2 = input("Enter second set name: ")
        operation = input("Enter set operation (e.g., union, intersection, difference, symmetric_difference): ")
        perform_operation(set_name1, set_name2, operation)

    def get_set_property_input():
        set_name1 = input("Enter first set name: ")
        set_name2 = input("Enter second set name: ")
        print("Are sets disjoint?", is_disjoint(set_name1, set_name2))
        print("Is set 1 a subset of set 2?", is_subset(set_name1, set_name2))
        print("Is set 1 a superset of set 2?", is_superset(set_name1, set_name2))

    def get_cardinality_input():
        set_name = input("Enter set name to get cardinality: ")
        cardinality = get_cardinality(set_name)
        if cardinality is not None:
            print(f"Cardinality of set '{set_name}': {cardinality}")

    while True:
        print("\nOptions:")
        print("1. Create a set")
        print("2. Add elements to a set")
        print("3. Remove an element from a set")
        print("4. Display a set")
        print("5. Perform a set operation")
        print("6. Check set properties")
        print("7. Determine the cardinality of the set")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            get_create_set_input()
        elif choice == "2":
            get_add_element_input()
        elif choice == "3":
            get_remove_element_input()
        elif choice == "4":
            display_set(input("Enter set name(s) or type 'all': "))
        elif choice == "5":
            get_set_operation_input()
        elif choice == "6":
            get_set_property_input()
        elif choice == "7":
            get_cardinality_input()
        elif choice == "8":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# usage
set_manager_program()

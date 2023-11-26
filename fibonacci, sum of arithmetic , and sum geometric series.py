def fibonacci_sequence(n):
    fib_sequence = [0, 1]

    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence

def arithmetic_series_sum(first_term, common_difference, n):
    return n * (2 * first_term + (n - 1) * common_difference) // 2

def geometric_series_sum(first_term, common_ratio, n):
    return first_term * (1 - common_ratio**n) // (1 - common_ratio)

while True:
    print("\nOptions:")
    print("1. Generate Fibonacci sequence")
    print("2. Calculate sum of arithmetic series")
    print("3. Calculate sum of geometric series")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        while True:
            n = int(input("Enter the number of terms: "))
            if n <= 0:
                print("Enter a nonnegative number ")
            else:
                fib_sequence = fibonacci_sequence(n)
                print(f"Fibonacci sequence: {fib_sequence}")
                break

    elif choice == "2":
        a = int(input("Enter the first term: "))
        d = int(input("Enter the common difference: "))
        n = int(input("Enter the number of terms: "))
        print(f"Calculating sum of the arithmetic series for:")
        print(f"First term: {a}\nCommon difference: {d}\nNumber of terms: {n}")
        series_terms = [a + i * d for i in range(n)]
        print(f"Terms of the arithmetic series: {series_terms}")
        print(f"Sum of the arithmetic series: {arithmetic_series_sum(a, d, n)}")

    elif choice == "3":
        a = int(input("Enter the first term: "))
        r = int(input("Enter the common ratio: "))
        n = int(input("Enter the number of terms: "))
        print(f"Calculating sum of the geometric series for:")
        print(f"First term: {a}\nCommon ratio: {r}\nNumber of terms: {n}")
        series_terms = [a * r**i for i in range(n)]
        print(f"Terms of the geometric series: {series_terms}")
        print(f"Sum of the geometric series: {geometric_series_sum(a, r, n)}")

    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")



#def fibonacci_sequence(n):
#    fib_sequence = [0, 1]

#    for _ in range(2, n):
#        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

#    return fib_sequence

#def arithmetic_series_sum(first_term, common_difference, num_terms):
#    return num_terms * (2 * first_term + (num_terms - 1) * common_difference) // 2

#def geometric_series_sum(first_term, common_ratio, num_terms):
#    return first_term * (1 - common_ratio**num_terms) // (1 - common_ratio)

#while True:
#    print("\nOptions:")
#    print("1. Generate Fibonacci sequence")
#    print("2. Calculate sum of arithmetic series")
#    print("3. Calculate sum of geometric series")
#    print("4. Exit")

#    choice = input("Enter your choice: ")

#    if choice == "1":
#        num_terms = int(input("Enter the number of terms: "))
#        fib_sequence = fibonacci_sequence(num_terms)
#        print(f"Fibonacci sequence: {fib_sequence}")
#    elif choice == "2":
#        first_term = int(input("Enter the first term: "))
#        common_diff = int(input("Enter the common difference: "))
#        num_terms = int(input("Enter the number of terms: "))
#        
#        print(f"Calculating sum of the arithmetic series for:")
#        print(f"First term: {first_term}, Common difference: {common_diff}, Number of terms: {num_terms}")
#        
#        series_terms = [first_term + i * common_diff for i in range(num_terms)]
#        print(f"Terms of the arithmetic series: {series_terms}")
#        
#        print(f"Sum of the arithmetic series: {arithmetic_series_sum(first_term, common_diff, num_terms)}")
#    elif choice == "3":
#        first_term = int(input("Enter the first term: "))
#        common_ratio = int(input("Enter the common ratio: "))
#        num_terms = int(input("Enter the number of terms: "))
#        
#        print(f"Calculating sum of the geometric series for:")
#        print(f"First term: {first_term}, Common ratio: {common_ratio}, Number of terms: {num_terms}")
#        
#        series_terms = [first_term * common_ratio**i for i in range(num_terms)]
#        print(f"Terms of the geometric series: {series_terms}")
#        
#        print(f"Sum of the geometric series: {geometric_series_sum(first_term, common_ratio, num_terms)}")
#    elif choice == "4":
#        print("Exiting the program.")
#        break
#    else:
#        print("Invalid choice. Please select a valid option.")

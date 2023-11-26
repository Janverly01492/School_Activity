def append_and_read_file(file_path='myfile.txt'):
    with open(file_path, 'a+') as file:
        user_input = input("Enter any inputs: ")
        file.write(user_input + "\n")
        file.seek(0)
        lines = file.readlines()

    for count, line in enumerate(lines, start=1):
        print(f"Line{count}: {line.strip()}")

    print(f"There are {len(lines)} lines in the file.")

append_and_read_file()
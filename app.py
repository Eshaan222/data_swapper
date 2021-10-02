def fileSwapper():
    file_a = input("Enter the name for file 1 : ")
    file_b = input("Enter the name for file 2 : ")

    with open(file_a, "r") as a:
        data_a = a.read()

    with open(file_b, "r") as a:
        data_b = a.read()

    with open(file_a, "w") as a:
        a.write(data_b)

    with open(file_b, "w") as a:
        a.write(data_a)

fileSwapper()
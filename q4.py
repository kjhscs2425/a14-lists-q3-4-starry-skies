def make_list_of_files(n):
    """
    make a lists of n file names with the format "file_0.txt"
    assume n greater than or equal to 1
    hint: use a loop and append
    return
    """
    list_of_files = []
    for file in range(n):
        list_of_files.append(f"file_{file}.text")
    return list_of_files

print(make_list_of_files(5)) #['file_0.txt', 'file_1.txt', 'file_2.txt', 'file_3.txt', 'file_4.txt']

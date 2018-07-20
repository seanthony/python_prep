def open_file(filename):
    with open(filename, 'r') as file:
        file.readline()
        file_information = file.readlines()

    return file_information

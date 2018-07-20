def open_file(filename):
    ''' str -> [str]
    opens a file of filename and returns a list
    of the line data, but skips the first line
    '''

    with open(filename, 'r') as file:
        file.readline()
        file_information = file.readlines()

    return file_information


def write_file(filename, file_string):
    ''' (str, str) -> None
    '''
    with open(filename, 'w') as file:
        file.write(file_string)

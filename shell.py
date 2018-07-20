import disk
import core


def get_option():
    '''() -> str
    returns the option for the users choice
    '''
    print('What would you like to do today?', '\n\t1. Add Hours',
          '\n\t2. Find Most Hours', '\n\t3. Exit')
    while True:
        choice = input('>>> ')
        if choice in ['1', '2', '3']:
            return choice
        print('oops!', choice, 'is invalid')


def get_username(user_dictionary):
    ''' {str: int} -> str 
    prints out the valid usernames
    and returns the user selected
    username if valid
    '''
    print('Usernames:', ', '.join(user_dictionary.keys()))
    while True:
        username = input('Which user? ')
        if username in user_dictionary.keys():
            return username
        else:
            print(username, 'is an invalid option.')


def get_hours():
    ''' None -> int
    returns a valid number of hours given by the user
    '''
    while True:
        hours = input('How many hours? ')
        if hours.isdigit():
            return int(hours)
        print('invalid entry!')


def add_user_hours(user_dictionary):
    username = get_username(user_dictionary)
    hours = get_hours()
    core.add_hours(user_dictionary, username, hours)
    print(hours, 'added to', username)


def find_most_hours(user_dictionary):
    usernames = core.get_most_hours(user_dictionary)
    for user in usernames:
        print(user, 'has worked', user_dictionary.get(user), 'hours')


def main():
    filename = './roster.txt'
    roster_raw_info = disk.open_file(filename)
    user_dictionary = core.create_user_dictionary(roster_raw_info)

    while True:
        print()
        choice = get_option()
        if choice == '1':
            add_user_hours(user_dictionary)
        elif choice == '2':
            find_most_hours(user_dictionary)
        elif choice == '3':
            break

    file_string = core.create_file_string(user_dictionary)
    disk.write_file(filename, file_string)


if __name__ == '__main__':
    main()

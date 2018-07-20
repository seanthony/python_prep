import disk
import core


def main():
    roster_raw_info = disk.open_file('./roster.txt')
    user_dictionary = core.create_user_dictionary(roster_raw_info)


if __name__ == '__main__':
    main()

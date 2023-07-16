import os
import pyperclip
import sqlite3


def get_country_name(abbreviation):
    conn = sqlite3.connect('iban_splitter.db')
    c = conn.cursor()
    c.execute(f"SELECT country_name FROM country WHERE abbreviation = '{abbreviation}'")
    country_name = c.fetchone()
    conn.close()

    return country_name[0]


def check_iban(iban):
    if not iban:
        print('IBAN is none. Please type something')
        return False
    elif len(iban) > 34:
        print('IBAN is too long. An IBAN has a maximum length of 34 characters.')
        return False
    elif iban[0].isdigit() or iban[1].isdigit():
        print('IBAN is invalid. The first two characters in an IBAN need to be alphabetical characters.')
        return False
    else:
        return True


def get_fours(iban_list):
    set_of_fours = ''

    for x in range(0, 4, 1):
        set_of_fours += iban_list[x]

    return set_of_fours


def build_split_iban(iban_list):
    split_iban = ''

    for x in range(0, 9):
        if len(iban_list) < 4:
            split_iban += ''.join(iban_list)
            break

        split_iban += get_fours(iban_list)
        del iban_list[:4]

        if x == 8:
            break
        else:
            split_iban += ' '

    return split_iban


def main():
    valid = False
    iban = ''

    print('Please input the IBAN you want to split.')

    while not valid:
        iban = input()
        valid = check_iban(iban)

    country_name = get_country_name(iban[:2])
    result = build_split_iban(list(iban))

    pyperclip.copy(result)
    print(f'The IBAN is from the following country: {country_name}.')
    print(f'Here is your result: {result}. It has been copied into your clipboard.')
    os.system('pause')


if __name__ == '__main__':
    main()

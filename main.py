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

    while not valid:
        iban = input()
        valid = check_iban(iban)

    print(build_split_iban(list(iban)))


if __name__ == '__main__':
    main()

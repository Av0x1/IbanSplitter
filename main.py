def get_fours(iban_list):
    set_of_fours = ''
    list_length = len(iban_list)

    for x in range(0, 4, 1):
        set_of_fours += iban_list[x]

    return set_of_fours


iban = input()

iban_list = list(iban)
split_iban = ''

for x in range(0, 9):
    split_iban += get_fours(iban_list)
    del iban_list[:4]

    if x == 8:
        break
    else:
        split_iban += ' '


print(split_iban)
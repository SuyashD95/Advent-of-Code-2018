def createChecksum(inventory):
    ids_containing_letter_twice = 0
    ids_containing_letter_thrice = 0

    for box_id in inventory:
        does_id_contain_letter_twice = False
        does_id_contain_letter_thrice = False

        for letter in box_id[:-1]:
            letter_count = box_id.count(letter)
            if letter_count == 2:
                does_id_contain_letter_twice = True
            elif letter_count == 3:
                does_id_contain_letter_thrice = True

        if does_id_contain_letter_twice:
            ids_containing_letter_twice += 1
        if does_id_contain_letter_thrice:
            ids_containing_letter_thrice += 1

    checksum = ids_containing_letter_twice * ids_containing_letter_thrice
    print("The checksum for the list of box IDs:", checksum)


if __name__ == "__main__":
    with open("input.txt") as inventory:
        createChecksum(inventory)

def diff_in_str(bid_1, bid_2, common_letters):
    diff_chars_count = 0
    for index in range(len(bid_1)):
        if bid_1[index] != bid_2[index]:
            diff_chars_count += 1
        else:
            common_letters.append(bid_1[index])
    return diff_chars_count


def findCommonLettersBetweenIds(box_ids):
    common_letters = []
    for index, box_id in enumerate(box_ids):
        bid_1 = box_id
        for bid_2 in box_ids[index + 1:]:
            # Clearing the common letters found between box ids used in the
            # last call to diff_in_str()
            common_letters.clear()
            if diff_in_str(bid_1, bid_2, common_letters) == 1:
                # Using list's mutability to update lists without returning from the function
                print("Common Letters between the two correct box IDs:", ''.join(common_letters))


if __name__ == "__main__":
    with open("input.txt") as inventory:
        box_ids = []
        for box_id in inventory:
            box_ids.append(box_id[:-1])
        findCommonLettersBetweenIds(box_ids)

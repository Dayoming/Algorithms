def solution(phone_number):
    # Change the last four digits of the phone_number to * through list indexing.
    change_number = phone_number.replace(
        phone_number[:-4], '*'*len(phone_number[:-4]))
    print(change_number)
    return change_number


solution("027778888")

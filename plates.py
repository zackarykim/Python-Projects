##“All vanity plates must start with at least two letters.”
##“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
##“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
##“No periods, spaces, or punctuation marks are allowed.”

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if not 2 <= len(plate) <= 6:
        return False

    if not plate[:2].isalpha():
        return False

    has_digit = False
    first_digit = True

    for char in plate:
        if char.isdigit():
            has_digit = True
            if first_digit:
                if char == "0":
                    return False
                first_digit = False
        elif char.isalpha():
            if has_digit:
                return False
        else:
            return False

    return True


main()

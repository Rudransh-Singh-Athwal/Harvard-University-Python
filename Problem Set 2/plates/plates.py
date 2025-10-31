def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    lettersCount = 0
    numbersCount = 0
    
    if (not(2 <= len(s) <= 6)):
        return False
    
    for ch in s:
        if not(ch.isalpha() or ch.isdecimal()):
            return False
        
        if ch.isalpha():
            if numbersCount > 0:
                return False
            lettersCount += 1
            
        if ch.isdecimal():
            if lettersCount < 2:
                return False
            if ch == '0' and numbersCount == 0:
                return False
            numbersCount += 1
            
    return True


main()
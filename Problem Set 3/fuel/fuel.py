def main():
    while True:
        try:
            fraction = input("Fraction: ")
            a, b = fraction.split("/")
            a = int(a)
            b = int(b)
            
            if a < 0 or b < 0:
                raise ValueError
            
            percentage = round((a / b) * 100)
            
            if a > b:
                continue
            
            if percentage <= 1:
                print('E')
            elif percentage >= 99:
                print('F')
            else:
                print(f"{percentage}%")
                
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break
        
if __name__ == "__main__":
    main()
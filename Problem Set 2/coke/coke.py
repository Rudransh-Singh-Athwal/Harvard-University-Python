def findChange(cost):
    while cost > 0:
        print(f"Amount Due: {cost}")
        coin = int(input("Insert Coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            cost -= coin
    return (-1 * cost)
            
def main():
    change = findChange(50)
    print(f"Change owed: {change}")
    
if __name__ == "__main__":
    main()
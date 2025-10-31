def isVowel(ch):
    return ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'

def omitVowels(word):
    ans = ""
    for ch in word:
        lch = ch.lower()
        if(isVowel(lch)):
            continue
        ans += ch
    
    return ans

def main():
    inp = input("Input: ")
    outp = omitVowels(inp)
    print(f"Output: {outp}")
    
if __name__ == "__main__":
    main()
        
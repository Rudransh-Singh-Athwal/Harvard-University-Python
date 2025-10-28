def solve(ans):
  ans = ans.lower()
  return (ans == "42") | (ans == "forty-two") | (ans == "forty two")

def main():
  text = input("What's your answer to the Great Question of Life? ")
  if(solve(text)):
    print("Yes")
  else:
    print("No")
    
main()
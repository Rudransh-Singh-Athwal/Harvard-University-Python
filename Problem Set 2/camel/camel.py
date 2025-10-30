def camelToSnake(name):
  n = len(name)
  res = ""
  for i in range(n):
    if name[i].islower():
      res += name[i]
    if name[i].isupper():
      res += "_"
      res += name[i].lower()
  
  return res

def main():
  name = input("Enter the name in camel case: ")
  snakeCase = camelToSnake(name)
  print(snakeCase)

main()
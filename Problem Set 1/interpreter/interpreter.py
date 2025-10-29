def calculate(a, op, b):
  res = 0

  if op == "+":
    res = a + b
  elif op == "-":
    res = a - b
  elif op == "*":
    res = a * b
  else:
    res = a / b
    
  res = round(float(res), 1)
  return res
  
def main():
  exp = input("Enter the expression: ")
  a, op, b = exp.split()
  a = int(a)
  b = int (b)
  res = calculate(a, op, b)
  print(res)
  
main()
def calculateEnergy(mass):
  c = 300000000
  c_sq = c * c
  return mass * c_sq

def main():
  mass = int(input("Enter the mass: "))
  energy = calculateEnergy(mass)
  print(energy)
  
  
main()
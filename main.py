import random, os,time
def rollDice(side):
  result = random.randint(1, side)
  return result

def health():
  healthStat = ((rollDice(6) * rollDice(12))/2)+ 10
  return healthStat

def strength():
  strengthStat = ((rollDice(6) * rollDice(8))/2)+ 12
  return strengthStat

while True:
  print ("CHARACTER BUILDER")
  print ()
  name = input ("Name your legend:")
  type = input ("Character type (Human, Elf, Wizard, Orc):")
  print (name)
  print ("Health:", health( ))
  print ("Strength :", strength( ))
  print( )
  print ("May your name go down in Legend....")
  print( )
  again = input ("Again?:")
  if again =="No" or again =="no":
    break
  time.sleep(1)
  os.system("clear")
  
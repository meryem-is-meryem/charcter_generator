simport random,time,os

def character():
  #print("sebroutine for charcter name and type")
  print("charcters type are: human , imp, wizard, elf")
  type=input("enter the type of your charcter: ")
  name=input("enter the name of your charcter: ")

def roll_dice(side):
  random_result=random.randint(1,side)
  return random_result

def health_stat():
  #print("sebroutine for charcter health stats")
  health=(roll_dice(6)*roll_dice(34)/2)+10
  return health

def strength_stat():
  #print("subroutine for charcter health stats")
  strength=(roll_dice(6)*roll_dice(12)/2)+12
  return strength


while True:
  print("**charcter builder**")
  time.sleep(1)
  character()
  time.sleep(1)
  print("HEALTH: ",health_stat())
  time.sleep(1)
  print("STRENGTH: ",strength_stat())
  time.sleep(1)
  print()
  time.sleep(1)
  print("legends never die...")
  yes_no=input("whould you like to choose another charcter: ")
  if yes_no=="yes":
    os.system("clear")
    continue
  else:
    exit()
    
  
  
  


import random,time,os

def character_type():
  #print("sebroutine for charcter name and type")
  print("charcters type are: human , imp, wizard, elf")
  type=input("enter the type of your charcter: ")
  return type

def charcter_name():
  name=input("enter the name of your charcter: ")
  return name

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

print("⚔️ BATTLE TIME ⚔️")
print()
while True:
  print("**charcter builder**")
  time.sleep(1)
  type_ch1=character_type()
  name_ch1=charcter_name()
  health_ch1=health_stat()
  strength_ch1=strength_stat()
  print("charcter number1--> ",name_ch1,"type--> ",type_ch1,"health--> ",health_ch1,"strength--> ",strength_ch1)
  time.sleep(1)
  print()
  print("** ",name_ch1," VS ...")
  type_ch2=character_type()
  name_ch2=charcter_name()
  health_ch2=health_stat()
  strength_ch2=strength_stat()
  print("charcter number2--> ",name_ch2,"type--> ",type_ch2,"health--> ",health_ch2,"strength--> ",strength_ch2)
  time.sleep(1)
  print()
  print("** ",name_ch1," VS **",name_ch2)
  print()
  time.sleep(1)
  print("legends never die...")
  time.sleep(5)
  os.system("clear")
  print("||let the battle begin||")
  print()
  round=1
  winner=None
  while True:
    ch1_dice=roll_dice(6)
    ch2_dice=roll_dice(6)
    diff=abs(strength_ch1-strength_ch2)+1
    if ch1_dice>ch2_dice:
      health_ch2=health_ch2-diff
      if round==1:
        print(name_ch1,"first winner")
      else:
        print(name_ch1,"wins the ",round,"round")
    elif ch2_dice>ch1_dice:
      health_ch1-=diff
      if round==1:
          print(name_ch2,"first winner")
      else:
        print(name_ch2,"wins the ",round,"round")
    else:
      print("////DRAW////")
      print("round--> ",round)
      time.sleep(1)
    print()
    print(name_ch1)
    print("health--> ",health_ch1)
    print()
    print(name_ch2)
    print("health--> ",health_ch2)
    print()
    time.sleep(5)
    os.system("clear")
    if health_ch1<=0:
      print(name_ch1," died")
      winner=name_ch2
      break
    elif health_ch2<=0:
      print(name_ch2," died")
      winner=name_ch1
      break
    else:
      print("DON'T YOU KNOW WE'RE STILL STANDING,LOOKING LIKE A TRUE SURVIVOR!!")
      round+=1
      
  time.sleep(5)
  os.system("clear")
  print("and the winner is...")
  print(winner)
  print("has won in ",round,"rounds")
  yes_no=input("whould you like to choose another charcter: ")
  if yes_no=="yes":
    os.system("clear")
    continue
  else:
    exit()

import random


def easy():
  easynumbers = ['1','2','3','4','5']
  number = random.choice(easynumbers)
  guess = input("Your Guess: ")

  if guess == number:
    print("You Won!")
    playagain = input("Do you want to play again? (y/N) ")

  else:
    print("Wrong!")
    easy()
  
  if playagain == 'y' or 'Y' or '':
    main()
  else:
    exit()

def medium():

  mediumnumbers = ['1','2','3','4','5','6','7','8','9','10']

  number = random.choice(mediumnumbers)
  guess = input("Your Guess: ")

  if guess == number:
    print("You Won!")
    playagain = input("Do you want to play again? (y/N) ")
  else:
    print("Wrong!")
    medium()
  if playagain == 'y' or 'Y' or '':
    medium()
def hard():

  hardnumbers = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']

  number = random.choice(hardnumbers)
  guess = input("Your Guess: ")

  if guess == number:
    print("You Won!")
    playagain = input("Do you want to play again? (y/N) ")
  else:
    print("Wrong!")
    hard()
  if playagain == 'y' or 'Y' or '':
    main()
  else:
    exit()

def veryhard():

  veryhardnumbers = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
  number = random.choice(veryhardnumbers)
  guess = input("Your Guess: ")

  if guess == number:
    print("You Won!")
    playagain = input("Do you want to play again? (y/N) ")
  else:
    print("Wrong!")
    veryhard()
  if playagain == 'y' or 'Y' or '':
    main()
  else:
    exit()

def main():
  print("""
  Difficulty:

  1) Easy (1-5)
  2) Medium (1-10)
  3) Hard (1-15)
  4) Very Hard (1-20)

  5) E X I T
  """)
  choice = input("Your choice: (1-5) ")

  if choice == '1':
    easy()
  elif choice == '2':
    medium()
  elif choice == '3':
    hard()
  elif choice == '4':
    veryhard()
  elif choice == '5':
    print("See you later!")
    exit()
  else:
    print("Invalid Choice!")
    main()

main()
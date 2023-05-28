import random
options = ("piedra","papel","tijera")
round = 1
computer_win = 0
user_win = 0

while True: 
  print("")
  print ("*" * 10)
  print("Round ", round)
  print("Rondas ganadas: ", "Ususario ", user_win, "Computador ", computer_win)
  print("")
  
  user_option = input ("piedra, papel o tijera? ")
  user_option = user_option.lower()
  round += 1
  
  if not user_option in options:
    print("Esa opción no es valida")
    continue 
  
  computer_option = random.choice(options)
  
  print("User option: ", user_option)
  print("Computer option: ", computer_option)
  
  if user_option == computer_option:
    print("Empate")
    
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("Piedra le gana a tijera")
      print("User ganó")
      user_win += 1
    else:
      print("Papel le gana a piedra")
      print("Computer ganó")
      computer_win += 1
      
  elif user_option == "papel":
    if computer_option == "piedra":
      print("Papel le gana a piedra")
      print("User ganó")
      user_win += 1
    else:
      print("Tijera le gana a papel")
      print("Computer ganó")
      computer_win += 1
  elif user_option == "tijera":
    if computer_option == "papel":
      print("Tijera le gana a papel")
      print("User ganó")
      user_win += 1
    else:
      print("Piedra le gana a tijera")
      print("Computer ganó")
      computer_win += 1
  if computer_win == 2:
    print("")
    print("El ganador final es la computadora")
    break
  if user_win == 2:
    print("")
    print("¡El ganador final es el usuario!")
    break 
  
import random


respuesta = "y"

while respuesta == "y":
   
   pregunta= input(str("Quieres tirar un dado de nuevo? y/n : ")).lower()
   numero = random.randint(1,6)

   if numero == 1:
     print("[-----]")
     print("[     ]") 
     print("[  0  ]") 
     print("[     ]") 
     print("[-----]")
   elif numero == 2:
     print("[-----]")
     print("[ 0   ]") 
     print("[     ]") 
     print("[   0 ]") 
     print("[-----]")
   elif numero == 3:
     print("[-----]")
     print("[ 0   ]") 
     print("[  0  ]") 
     print("[   0 ]") 
     print("[-----]")
   elif numero == 4:
     print("[-----]")
     print("[ 0 0 ]") 
     print("[     ]") 
     print("[ 0 0 ]") 
     print("[-----]")
   elif numero == 5:
     print("[-----]")
     print("[ 0 0 ]") 
     print("[  0  ]") 
     print("[ 0 0 ]") 
     print("[-----]")
   else:
     print("[-----]")
     print("[ 0 0 ]") 
     print("[ 0 0 ]") 
     print("[ 0 0 ]") 
     print("[-----]")

   if respuesta == "n":
     print("gracias por jugar")
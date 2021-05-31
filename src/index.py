import colorama
from generate_num import Generate_number
from check_numbers import Checking
from check_numbers_city import Checking as Checking_with_city
from time import sleep
import os

# Colores
rojo = colorama.Fore.RED
no_color = colorama.Style.RESET_ALL


# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Clase principal
class Xphony:
     
     """Takes no arguments
     """
     def __init__(self):

          if os.name == 'nt':
              os.system("cls")
          else:
              os.system("clear")
          self.c = colorama.Fore.LIGHTYELLOW_EX
          self.cr = colorama.Fore.RED
          self.cg = colorama.Fore.GREEN
          self.r = colorama.Style.RESET_ALL
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
          print(self.c, f'''
                
██╗  ██╗     ███████╗ ██████╗ ███╗   ██╗██╗   ██╗
╚██╗██╔╝     ██╔════╝██╔═══██╗████╗  ██║╚██╗ ██╔╝
 ╚███╔╝█████╗█████╗  ██║   ██║██╔██╗ ██║ ╚████╔╝ 
 ██╔██╗╚════╝██╔══╝  ██║   ██║██║╚██╗██║  ╚██╔╝  
██╔╝ ██╗     ██║     ╚██████╔╝██║ ╚████║   ██║   
╚═╝  ╚═╝     ╚═╝      ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   
                                                 
                ''', self.r)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
          # Country code
          print(f"[{self.c}*{self.r}] Input the country code (exclude the '+' symbol)")
          try:
               self.country_code = int(input(f"{self.c}>_{self.r}\t\t"))
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
          except ValueError as e:
               state = False
               while state == False:
                    print(f"[{self.cr}*{self.r}] Input VALID country code")
                    try:
                         self.country_code = int(input(f"{self.cr}>_{self.r}\t\t"))
                         state = True
                    except ValueError:
                         continue
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #         
          # City code
          print(f"[{self.c}*{self.r}] does the country need city code? (y/n)")
          temp_election = input(f"{self.c}>_{self.r}\t\t")
          
          # If no:
          if temp_election.lower() == 'n':
               print(f"[{self.cg}*{self.r}] gotten info: {self.country_code}")
               print(f"[{self.c}*{self.r}] going to generate phone numbers with this info")
               Checking(country=self.country_code)
               
          # If yes:
          elif temp_election.lower() == 'y':
               
               try:
                    
                    print(f"[{self.cg}*{self.r}] input your city code then")
                    self.city_code = int(input(f"{self.c}>_{self.r}\t\t"))
                    
               except ValueError as e:
                    
                    state = False
                    
                    while state == False:
                         
                         print(f"[{self.cr}*{self.r}] Input VALID city code")
                         try:
                              
                              self.city_code = int(input(f"{self.cr}>_{self.r}\t\t"))
                              state = True
                              
                         except ValueError:
                              continue
                         
               print(f"[{self.cg}*{self.r}] gotten info: {self.country_code} {self.city_code}")
               print(f"[{self.c}*{self.r}] going to generate phone numbers with this info")
               Checking_with_city(self.country_code, self.city_code)
          # Else:
          else:
               while temp_election.lower() != 'y' and temp_election.lower() != 'n':
                    print(f"[{self.cr}*{self.r}] Input VALID response! (y/n)")
                    temp_election = input(f"{self.c}>_{self.r}\t\t")
                    
                    # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
                    
                    if temp_election.lower() == 'n':
                         pass
                         print(f"[{self.cg}*{self.r}] gotten info: {self.country_code}")
                         print(f"[{self.c}*{self.r}] going to generate phone numbers with this info")
                         
                    # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
                    
                    elif temp_election.lower() == 'y':
                    
                         try:
                              print(f"[{self.cg}*{self.r}] input your city code then")
                              self.city_code = int(input(f"{self.c}>_{self.r}\t\t"))
                              
                    # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
                    
                         except ValueError as e:
                              state = False
                              while state == False:
                                   print(f"[{self.cr}*{self.r}] Input VALID city code")
                                   try:
                                        self.city_code = int(input(f"{self.cr}>_{self.r}\t\t"))
                                        state = True
                                        
                    # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
                    
                                   except ValueError:
                                        continue
                                   
                    # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
                    
                         print(f"[{self.cg}*{self.r}] gotten info: {self.country_code} {self.city_code}")
                         print(f"[{self.c}*{self.r}] going to generate phone numbers with this info")
                         
                    # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
                    
                    else:
                         continue
x = Xphony
try:
    x()
except KeyboardInterrupt:
    print(rojo, "\nSaliendo...", no_color)
            # Twitter   # Discord
# Code by:
# lVoidi    # VoidVoidi # Vøid#2340
# Black     # None      # Black#5558

from check_numbers_city import Checking as Checking_with_city
from check_numbers import Checking
import colorama
import os

red = colorama.Fore.RED
green = colorama.Fore.GREEN
reset = colorama.Style.RESET_ALL
yellow = colorama.Fore.LIGHTYELLOW_EX
no_color = colorama.Style.RESET_ALL

class Xphony:
     """Takes no arguments
     """
     def __init__(self):
          os.system("cls" if os.name == "nt" else "clear")
          print(yellow, f'''
                
██╗  ██╗     ███████╗ ██████╗ ███╗   ██╗██╗   ██╗
╚██╗██╔╝     ██╔════╝██╔═══██╗████╗  ██║╚██╗ ██╔╝
 ╚███╔╝█████╗█████╗  ██║   ██║██╔██╗ ██║ ╚████╔╝ 
 ██╔██╗╚════╝██╔══╝  ██║   ██║██║╚██╗██║  ╚██╔╝  
██╔╝ ██╗     ██║     ╚██████╔╝██║ ╚████║   ██║   
╚═╝  ╚═╝     ╚═╝      ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   
                                                 
                ''', reset)
          # Country code
          self.country_code = 0
          print(f"[{yellow}*{reset}] Input the country code (exclude the '+' symbol)")
          try:
               self.country_code = int(input(f"{yellow}>_{reset}\t\t"))
          except ValueError as e:
               print(f"[{red}*{reset}] Input VALID city code")
               exit(1)

          print(f"[{yellow}*{reset}] does the country need city code? (y/n)")
          temp_election = input(f"{yellow}>_{reset}\t\t")
          
          if temp_election.lower() == 'n':
               print(f"[{green}*{reset}] gotten info: {self.country_code}")
               print(f"[{yellow}*{reset}] going to generate phone numbers with this info")
               Checking(country=self.country_code)
               
          elif temp_election.lower() == 'y':
               try:
                    print(f"[{green}*{reset}] input your city code then")
                    self.city_code = int(input(f"{yellow}>_{reset}\t\t"))
               except ValueError as e:
                    print(f"[{red}*{reset}] Input VALID city code")
                    exit(1)
               print(f"[{green}*{reset}] gotten info: {self.country_code} {self.city_code}")
               print(f"[{yellow}*{reset}] going to generate phone numbers with this info")
               Checking_with_city(self.country_code, self.city_code)
          else:
               print(f"[{red}*{reset}] Input VALID city code")
               exit(1)
x = Xphony
try:
    x()
except KeyboardInterrupt:
    print(red, "\nSaliendo...", no_color)
            # Twitter   # Discord
# Code by:
# lVoidi    # VoidVoidi # Vøid#2340
# Black     # None      # Black#5558

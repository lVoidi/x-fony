import colorama
from generate_num import Generate_number
from check_numbers import Checking
from time import sleep
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
class Xphony:
     
     """Takes no arguments
     """
     def __init__(self):
          self.c = colorama.Fore.LIGHTYELLOW_EX
          self.cr = colorama.Fore.RED
          self.cg = colorama.Fore.GREEN
          self.r = colorama.Style.RESET_ALL
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
          print(f'''
                
                        mmmm
                       ##"""
 "##  ##"            #######    m####m   ##m####m  "##  ###
   ####                ##      ##"  "##  ##"   ##   ##m ##
   m##m     #####      ##      ##    ##  ##    ##    ####"
  m#""#m               ##      "##mm##"  ##    ##     ###
 """  """              ""        """"    ""    ""     ##
                                                    ###
                ''')
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
          # Country code
          print(f"[{self.c}*{self.r}] Input the country code (exclude the '+' symbol)")
          try:
               self.country_code = int(input(f"{self.c}~»{self.r}     "))
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
          except ValueError as e:
               state = False
               while state == False:
                    print(f"[{self.cr}*{self.r}] Input VALID country code")
                    try:
                         self.country_code = int(input(f"{self.cr}~»{self.r}     "))
                         state = True
                    except ValueError:
                         continue
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #         
          # City code
          print(f"[{self.c}*{self.r}] does the country need city code? (y/n)")
          temp_election = input(f"{self.c}~»{self.r}     ")
          
          # If no:
          if temp_election.lower() == 'n':
               print(f"[{self.cg}*{self.r}] gotten info: {self.country_code}")
               print(f"[{self.c}*{self.r}] going to generate phone numbers with this info")
               print(f"[{self.c}*{self.r}] Input the length of the numbers in the selected country")
               try:
                    self.length = int(input(f"{self.cg}~»{self.r}     "))
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
               except ValueError as e:
                    state = False
                    while state == False:
                         print(f"[{self.cr}*{self.r}] Input VALID length")
                         try:
                              sself.length = int(input(f"{self.cr}~»{self.r}     "))
                              state = True
                         except ValueError:
                              continue
               Checking(country=self.country_code)
               
          # If yes:
          elif temp_election.lower() == 'y':
               
               try:
                    
                    print(f"[{self.cg}*{self.r}] input your city code then")
                    self.city_code = int(input(f"{self.c}~»{self.r}     "))
                    
               except ValueError as e:
                    
                    state = False
                    
                    while state == False:
                         
                         print(f"[{self.cr}*{self.r}] Input VALID city code")
                         try:
                              
                              self.city_code = int(input(f"{self.cr}~»{self.r}     "))
                              state = True
                              
                         except ValueError:
                              continue
                         
               print(f"[{self.cg}*{self.r}] gotten info: {self.country_code} {self.city_code}")
               print(f"[{self.c}*{self.r}] going to generate phone numbers with this info")
               
          # Else:
          else:
               while temp_election.lower() != 'y' and temp_election.lower() != 'n':
                    print(f"[{self.cr}*{self.r}] Input VALID response! (y/n)")
                    temp_election = input(f"{self.c}~»{self.r}     ")
                    
                    # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
                    
                    if temp_election.lower() == 'n':
                         pass
                         print(f"[{self.cg}*{self.r}] gotten info: {self.country_code}")
                         print(f"[{self.c}*{self.r}] going to generate phone numbers with this info")
                         
                    # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
                    
                    elif temp_election.lower() == 'y':
                    
                         try:
                              print(f"[{self.cg}*{self.r}] input your city code then")
                              self.city_code = int(input(f"{self.c}~»{self.r}     "))
                              
                    # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
                    
                         except ValueError as e:
                              state = False
                              while state == False:
                                   print(f"[{self.cr}*{self.r}] Input VALID city code")
                                   try:
                                        self.city_code = int(input(f"{self.cr}~»{self.r}     "))
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


Xphony()
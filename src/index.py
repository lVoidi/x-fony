import phonenumbers
import random
import colorama

class Xphony:
     """Takes no arguments
     """
     def __init__(self):
          self.c = colorama.Fore.LIGHTYELLOW_EX
          self.r = colorama.Style.RESET_ALL
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
          # Country code
          print(f"[{self.c}*{self.r}] Input the country code (exclude the '+' symbol)")
          self.country_code = int(input(f"{self.c}~»{self.r}     "))
          
          print(f"[{self.c}*{self.r}] Input the")
          self.country_code = int(input(f"{self.c}~»{self.r}     "))
          
          

Xphony()
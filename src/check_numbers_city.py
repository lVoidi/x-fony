import phonenumbers
import colorama
from generate_num import Generate_number
from time import sleep
class Checking:
     def __init__(self, country, city):
          """[summary]

          Args:
              phone (string): The phone number
          """
          self.c = colorama.Fore.LIGHTYELLOW_EX
          self.cr = colorama.Fore.RED
          self.cg = colorama.Fore.GREEN
          self.r = colorama.Style.RESET_ALL
          self.count_true = 0
          self.count_false = 0
          self.country_code = country
          self.city_code = city
          print(f"[{self.c}*{self.r}] Input the length of the numbers in the selected country")
          try:
               self.length = int(input(f"{self.cg}~»{self.r}     "))
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
          except ValueError as e:
               state = False
               while state == False:
                    print(f"[{self.cr}*{self.r}] Input VALID length")
                    try:
                         self.length = int(input(f"{self.cr}~»{self.r}     "))
                         state = True
                    except ValueError:
                         continue
          while True:
               try:
                    self.generated_number = Generate_number(self.length).gen_number()
                    self.number = f'+{self.country_code}{self.city_code}{self.generated_number}'
                    self.true_phone(phone=self.number)
                    
               except KeyboardInterrupt:
                    break
                    
     def true_phone(self, phone):
          
          self.phone_number = phonenumbers.parse(f'+{phone}', None)
          
          if phonenumbers.is_valid_number(self.phone_number):
               self.count_true += 1
          else:
               self.count_false += 1
          
          print('generated:{}{}{} {} count_true: {}     count_false: {}\r'.format(self.c, phonenumbers.is_valid_number(self.phone_number),self.r,phone, self.count_true, self.count_false))
import random
from string import digits as all_numbers

class Generate_number:
     def __init__(self, length: int):
          self.length = length
          
     def gen_number(self):
          self.all_generated = ''
          
          for x in range(self.length):
               generation = ''.join(random.sample(all_numbers, 1))
               self.all_generated += generation
               
          return self.all_generated

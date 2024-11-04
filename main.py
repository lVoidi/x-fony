import phonenumbers
import colorama
import random 


def generate_number(country: str, city: str, length: str) -> phonenumbers.phonenumber.PhoneNumber:
    random_number = "".join(str(random.randint(0, 10)) for _ in range(int(length)))
    return phonenumbers.parse(f"+{country}{city}{random_number}", None)


def wrap_color(color, text):
    return f"{color}{text}{colorama.Style.RESET_ALL}"


def main():
    print(wrap_color(colorama.Fore.YELLOW, '''
██╗  ██╗     ███████╗ ██████╗ ███╗   ██╗██╗   ██╗
╚██╗██╔╝     ██╔════╝██╔═══██╗████╗  ██║╚██╗ ██╔╝
 ╚███╔╝█████╗█████╗  ██║   ██║██╔██╗ ██║ ╚████╔╝ 
 ██╔██╗╚════╝██╔══╝  ██║   ██║██║╚██╗██║  ╚██╔╝  
██╔╝ ██╗     ██║     ╚██████╔╝██║ ╚████║   ██║   
╚═╝  ╚═╝     ╚═╝      ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   
'''))
    
    print(f"[{wrap_color(colorama.Fore.YELLOW, '*')}] Input the country code (exclude the '+' symbol)")
    country_code = input(f"{wrap_color(colorama.Fore.YELLOW, '>_')}\t\t")
    
    print(f"[{wrap_color(colorama.Fore.BLUE, '*')}] Input the city code (leave blank if none)")
    city_code = input(f"{wrap_color(colorama.Fore.YELLOW, '>_')}\t\t")
    
    print(f"[{wrap_color(colorama.Fore.YELLOW, '*')}] Input the length of the numbers in the selected country")
    length = input(f"{wrap_color(colorama.Fore.YELLOW, '>_')}\t\t")
    
    print(f"[{wrap_color(colorama.Fore.YELLOW, '*')}] How many numbers do you want to generate?")
    generate = input(f"{wrap_color(colorama.Fore.YELLOW, '>_')}\t\t")
    
    try:
        int(country_code), int(length), int(generate)
        if city_code:
            int(city_code)
    except ValueError:
        print(f"[{colorama.Fore.RED}*{colorama.Style.RESET_ALL}] Invalid values")
        print(f"[{colorama.Fore.RED}*{colorama.Style.RESET_ALL}] {country_code=} {city_code=} {length=}")
        exit(1)
    
    
    numbers = ""
    true_numbers = 0
    
    while true_numbers < int(generate):
        number = generate_number(country_code, city_code, length)
        is_valid = phonenumbers.is_valid_number(number)
        print(f"Generated: {is_valid} {number.national_number}", end="\r")
        if is_valid:
            parsed_number = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164)
            numbers += f"https://wa.me/{parsed_number}\n"
            true_numbers += 1
    
    print()
    
    with open("log.txt", "a") as log:
        log.write(numbers)
        
    print(f"[{wrap_color(colorama.Fore.GREEN, "+")}] Done writting to log.txt")
    
    
if __name__ == "__main__":
    main()
from colorama import Style, Back, Fore
from rich.table import Table
import os
import sys
import base64
from time import sleep
import time
import platform



if platform.system() == 'Windows':
    os.system('cls & title Base64 Tool')  # clear console, change title
elif platform.system() == 'Linux':
    os.system('clear')  # clear console
    sys.stdout.write("\x1b]0;Python Example\x07")  # change title
elif platform.system() == 'Darwin':
    os.system("clear && printf '\e[3J'")  # clear console
    os.system('''echo - n - e "\033]0;Base64 Tool\007"''')  # change title




def decode_function():

    input_string = input(Fore.YELLOW + "[" + Fore.RED + "Decode" + Fore.YELLOW + "]" + Fore.RESET)
    decoded_string = base64.b64decode(input_string).decode()
    print("Decoded string:", decoded_string)




print(Fore.RED + """
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                                                        #
#  ██████╗  █████╗ ███████╗███████╗ ██████╗ ██╗  ██╗    ████████╗ ██████╗  ██████╗ ██╗         ██████╗ ██████╗  ██████╗  #
#  ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝ ██║  ██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║         ██╔══██╗██╔══██╗██╔═══██╗ #
#  ██████╔╝███████║███████╗█████╗  ███████╗ ███████║       ██║   ██║   ██║██║   ██║██║         ██████╔╝██████╔╝██║   ██║ #
#  ██╔══██╗██╔══██║╚════██║██╔══╝  ██╔═══██╗╚════██║       ██║   ██║   ██║██║   ██║██║         ██╔═══╝ ██╔══██╗██║   ██║ #
#  ██████╔╝██║  ██║███████║███████╗╚██████╔╝     ██║       ██║   ╚██████╔╝╚██████╔╝███████╗    ██║     ██║  ██║╚██████╔╝ # 
#  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝      ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  #
#                                                                                                                        # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
  """ + Fore.RESET)

print(Fore.GREEN      + "                                                                                              [1.0 Loaded Succsessfully]")

f = "1" 
s = "2"


#================================================================================================
print(Fore.YELLOW + "[" + Fore.RED + f + Fore.YELLOW + "] " + Fore.GREEN +"INCODE Base64")
print(Fore.YELLOW + "[" + Fore.RED + s + Fore.YELLOW + "] " + Fore.RED + "DECODE Base64" + Fore.RESET)
user_input = input(Fore.YELLOW + "> " + Fore.RESET)
print('\n')
#======================================================================================================



# Validating the user input

if user_input == f:     

    print("\n")
    # Ask for input
    input_string = input(Fore.YELLOW + "[" + Fore.GREEN + "INCODE" + Fore.YELLOW + "]" + Fore.RESET)
    print("\n")

    # Encode the input string in base64
    encoded_string = base64.b64encode(input_string.encode())

    # Print the encoded string
    print("Encoded string:", encoded_string.decode())

elif user_input == s:
       decode_function()
      


else:
   exit()






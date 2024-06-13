#!/usr/bin/env python
import os
import random
import sys
import signal as sigga
from colorama import init, Fore, Style

init(autoreset=True)

ASCII_ART = r"""
                                                                                  
 #### #####   #   ####  #####      #### ##### ####  ####  ##### #####              
#       #    # #  #   #   #       #     #     #   # #   # #     #   #             
#       #   ##### ####    #       #     ####  ####  ####  ####  ####              
#       #   #   # #       #       #     #     #     #   # #     #                 
 ####   #   #   # #       #        #### ##### #     ####  ##### #      #   #   #                                              
"""


def signal_handler(sig, frame):
    queue = [' [+] see you soon...😄 [+] ', ' [+] bye, bye dev...😄 [+] ',
             ' [+] Work is Successfully! [+] ', ' [+] Going to home... [+] ', ' [+] Going to kitchen! [+]',
             '[+] I am hungry! [+]']
    print(Fore.YELLOW + random.choice(queue))
    sys.exit(0)


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    colors = [Fore.CYAN, Fore.YELLOW, Fore.RED, Fore.BLUE, Fore.LIGHTYELLOW_EX, Fore.MAGENTA]
    print(random.choice(colors) + ASCII_ART)

    sigga.signal(sigga.SIGINT, signal_handler)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        print(Fore.RED + "Ошибка: Не удалось импортировать Django. Убедитесь, что оно установлено. 😄")
        raise ImportError("Django import error.") from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()




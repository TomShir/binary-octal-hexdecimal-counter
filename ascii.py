while True:
  try:
    from colorama import Fore 
    import time 
    import sys 
    user=str(input('print numbers in binary ,hexdecimal or octal:'))
    binary='bin'
    hexdecimal='hex'
    octidecimal='oct'
    starting_number=0
    def error_msg(txt):
      for n in txt:
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write(f'{n}')
      else:
        global reset_to_default_color 
        reset_to_default_color=Fore.RESET 
        print(f'{reset_to_default_color}')
      if txt=='':
        pass  
        
    error_msg(txt='')
    number_limit=int(input('Enter your number_limit:'))
    if user==binary:
      while starting_number<number_limit:
        starting_number+=1 
        binaryic=bin(starting_number)
        time.sleep(0.2)
        print(Fore.GREEN)
        print(binaryic[2:],starting_number)
        if starting_number==number_limit:
          print(f'{reset_to_default_color}')
          break 
    elif user==octidecimal:
      print(Fore.BLUE)
      for n in range(starting_number+1,number_limit+1,1):
        print(f'{n} {oct(n)}')
        time.sleep(0.2)
        print('\n')
        if n==number_limit:
         print(f'{reset_to_default_color}')
         break
    elif user==hexdecimal:
        while starting_number<number_limit:
            starting_number+=1 
            print(Fore.RED)
            print(f'{starting_number} {hex(starting_number)}')
            time.sleep(0.2)
            if starting_number==number_limit:
                print(f'{reset_to_default_color}')
                break
  except ValueError:
    error_msg(txt='')

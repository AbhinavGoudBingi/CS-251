
try:
 pin=int(input("Enter the pin: "))
 if pin>=0 and pin<=9999:
  if(pin==4949):
    print("Lock Opened")
    exit()
  print("Wrong PIN! Try again")
  pin=int(input("Enter the pin: "))
  if(pin==4949):
    print("Lock Opened")
  else:
    print("Full alarm")
 else:
    print("Full Alarm")
    exit()

except ValueError:
    print("Full Alarm")
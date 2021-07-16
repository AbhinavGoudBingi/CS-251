import os
os.mkdir("./Data/Survivors_of_Snap")
with open('./Data/Heroes.txt') as f:
    lines = f.read().splitlines()
for word in lines:
 for file in os.listdir("./Data/Avengers_Universe"):
  with open("./Data/Avengers_Universe/%s" % file) as f:
    if word in f.read():
       os.rename("./Data/Avengers_Universe/%s" % file ,"./Data/Survivors_of_Snap/%s" % file)
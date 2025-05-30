a=(input("enter the number:"))
print(f"multiplication table of {a}is:")

try:
   for i in range(1,11):
       print(f"{int(a)}* {i} = {int(a)*i}")
except Exception as e:
    print("invalid error")
    
print("code is done !")
print( "move with next")
    
def add(a,b):
	print(f"addition:{a+b}")
def sub(a,b):
	print(f"subtraction:{a-b}")
def mul(a,b):
	print(f"multiplication:{a*b}")
def div(a,b):
	print(f"division:{a/b}")
def rem(a,b):
	print(f"remainder:{a%b}")
def poww(a,b):
	print(f"power:{a**b}")



while(1):
	print("1.Addition 2.Subtraction 3.Multiplication 4.Division 5.Remainder 6. Power 7.Exit")
	print("Enter your choice")
	ch=int(input())
	if(ch==7):
		break
	print("Enter the two numbers")
	a=int(input())
	b=int(input())
	
	if(ch==1):
		add(a,b)
	elif ch==2:
		sub(a,b)
	elif ch==3:
		mul(a,b)
	elif ch==4:
		div(a,b)
	elif ch==5:
		rem(a,b)
	elif ch==6:
		poww(a,b)
	else:
		print("Invalid choice!")

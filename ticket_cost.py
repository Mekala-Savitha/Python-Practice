Ticket_Cost=int(input("Enter Ticket Cost:"))
age=int(input("Enter Age:"))
minor_concession=Ticket_Cost/2
sr_citizen_concession=Ticket_Cost-(Ticket_Cost*20)/100
if(age<5):
	print("You are child,so no Ticket")
elif(age>5 and age<12):
		print("You are minor,Half Ticket RS.",minor_concession)
elif(age>12 and age<60):
			print("You are major,Ticket Cost RS.",Ticket_Cost)
else:
	print("You are srcitizen,20% concession,so Ticket Cost RS.",sr_citizen_concession)

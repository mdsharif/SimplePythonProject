import os
def cls():
	os.system('cls')

#function 'results'
def results():
	print("inside result")
	f = open('allResults.txt','r')
	print("RollNo.%15sName%16sMarks" %("",""))
	print()
	for line in f:
		data = line.split(':')
		print("%-22s%-20s%-10s\r" %(data[0],data[1],data[2]),end='')
	f.close()
	print()
	print()

#function 'results' end

#function 'score'
def score():
	print("inside score")
#function 'score' end

#function 'addNew'
def addNew():
	print('inside addNew')
#function 'addNew' end

#function 'summary'
def summary():
	print("inside summary")
#function 'summary' end

#function 'modify'
def modify():

	print("inside modify")
#function 'modify' ends

#function 'delete'
def delete():
	print("inside delete")
#function 'delete' ends

#function 'transfer'
def transfer():

	print('inside transfer')
#function 'transfer' ends

##GLOBAL SCOPE

attempt = 0
confirm = True


cls()
while(confirm):

	print("1.Result of All Students")
	print("2.Score of Students")
	print("3.Add Records of a new Students")
	print("4.Summary of Result")
	print("5.Modify the Score")
	print("6.Delete a Record")
	print("7.Transfer data to File")
	print("8.Close the Program")
	
	option = eval(input("\nEnter the Desired Option: "))
	if(option == 1):
		cls()
		results()
	elif(option == 2):
		cls()
		score()
	elif(option == 3):
		cls()
		addNew()
	elif(option == 4):
		cls();
		summary()
	elif(option == 5):
		cls()
		modify()
	elif(option == 6):
		cls()
		delete()
	elif(option == 7):
		cls()
		transfer()
	elif(option == 8):
		cls()
		print("Thank you for using our Application. SEE you SOON")
		confirm = False
	else:
		cls()
		attempt = attempt + 1
		if(attempt != 3):
			print("You Entered a wrong Number.")
			print("U have only",3-attempt," attempt left, post that program will be closed automatically")
		else:
			print("You Have Reached Maximum Limit allowed.Program is Closing Now...")
			print("Program is Successfully Closed.")
			print("Thanks For Using Our Application.\n")
			confirm = False

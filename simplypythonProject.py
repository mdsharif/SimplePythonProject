import os
def cls():
	os.system('cls')

#function 'results'
def results():
	f = open('allResults.txt','r')
	print("RollNo.%15sName%16sMarks" %("",""))
	print()
	for line in f:
		data = line.split(':')	#each fetched recored splitted
		print("%-22s%-20s%-10s\r" %(data[0],data[1],data[2]),end='')
	f.close()
	print()
	print()
#function 'results' end

#function 'score'
def score():
	isFound = False
	print("**Score of a Student**")
	rollNumber = input("Enter Your Roll Number : ")
	f = open('allResults.txt','r')
	for line in f:
		data = line.split(':')
		if(rollNumber == data[0]):
			print("Hi",data[1],"Your score is",data[2])
			isFound = True
	if(isFound == False):
		print("Roll Number",rollNumber,"is not available in our File.")
	f.close()
	print()
	print()
#function 'score' end

#function 'addNew'
def addNew():
	cls()
	print("**Adding a new Record to the File**")
	print("Enter the Below asked Information :")
	rollNumber = input("%10sRoll No. : " %(""))
	name = input("%10sName : " %(""))
	score = input("%10sScore : " %(""))
	f = open('allResults.txt','a')
	f.write("\n")
	f.write(rollNumber+":"+name+":"+score)
	print(name,"'s detail has Successfully Added.")
	f.close()
	print()
	print()
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
	print("3.Add Records of a new Student")
	print("4.Modify the Score")
	print("5.Delete a Record")
	print("6.Transfer data to File")
	print("7.Close the Program")
	
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
		cls()
		modify()
	elif(option == 5):
		cls()
		delete()
	elif(option == 6):
		cls()
		transfer()
	elif(option == 7):
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
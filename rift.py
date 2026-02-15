
import random
import array
import os
import sys

print("         \n\n")



def lvl20(levl)->array:
	global attempts
	attempts+=1
	chance = random.randint(1,100)
	chance_of_success = 50
	chance_of_failure = 47
	chance_of_unup = 3
	
	cos = chance_of_success
	cof = chance_of_failure
	unp = chance_of_unup
	
	if chance >= (100-cos):
		
		levl =[levl[0]+1,True,chance]
		
		return levl
	elif (chance < (cof+unp))and (chance>unp):
		if levl[0]==20:
			levl= [20,True,chance]
			return levl
		else:
			levl = [levl[0]-1,True,chance]
			return levl
	elif chance <= unp:
		
		if a==0: print(" --Unupgradeable-- ")
		levl = [levl[0],False,chance]
		return levl
	
	print(" error is ", levl, "   chance = ", chance)		

def lvl25(levl)->array:
	global attempts
	attempts+=1
	chance = random.randint(1,100)
	chance_of_success = 40
	chance_of_failure = 57
	chance_of_unup = 3
	
	cos = chance_of_success
	cof = chance_of_failure
	unp = chance_of_unup	
	
	if chance >= (100-cos):
		levl = [levl[0]+1,True,chance]
		return levl
	elif (chance < (cof+unp))and (chance>unp):
		if levl[0]==25:
			levl = [25,True,chance]

			return levl
		else:
			levl = [levl[0]-1,True,chance]

			return levl
	elif chance <= unp:
		
		if a==0: print(" --Unupgradeable-- ")
		levl=[levl[0],False,chance]
		return levl
	
	print(" error is ", levl, "   chance = ", chance)		


def lvl30(levl)->array:
	global attempts
	attempts+=1
	chance = random.randint(1,100)
	chance_of_success = 30
	chance_of_failure = 67
	chance_of_unup = 3
	
	cos = chance_of_success
	cof = chance_of_failure
	unp = chance_of_unup
	
	if chance >= (100-cos):
		levl = [levl[0]+1,True,chance]

		return levl
	elif (chance < (cof+unp))and (chance>unp):
		if levl[0]==30:
			levl= [30,True,chance]

			return levl
		else:
			
			return [levl[0]-1,True,chance]
	elif chance <= unp:
		
		if a==0: print(" --Unupgradeable-- ")
		
		levl = [levl[0],False,chance]
		return levl
	
	print(" error is ", levl, "   chance = ", chance)	

def run():
	global attempts
	attempts = 0
	global t
	global target_smelt
	global level
	lev = level
	
	while type(lev) == list and(lev[1]):
		
		if a==1: print(lev[0])
		
		if lev[0]>=30:
			lev = lvl30(lev)
			if lev[1]==False: break
				
		elif lev[0]>=25:
			lev = lvl25(lev)
			if lev[1]==False: break
		
		elif lev[0]>=20:
			lev = lvl20(lev)
			if lev[1]==False: break
	
	if lev[0] >= t:
		target_smelt+=1			
	print("level : " ,lev[0],"    attempts : ",attempts, "  %", lev[2])

		






def upgrade():
	for n in range(a):
		run()
	print(" equipment that reached lvl",t ," created",target_smelt)
	print(" your odds of reaching one in a consecutive upgrade : ", target_smelt/a)

i = int(input("What level to start? : "))
level = [i,True,0]

attempts = 0

target_smelt=0


a = int(input("How many simulation? : "))
t = int(input("Target Smelt : "))




upgrade()

if str(input("retry program? : (y?)"))=="y":
	os.execv(sys.executable, ['python'] + sys.argv)
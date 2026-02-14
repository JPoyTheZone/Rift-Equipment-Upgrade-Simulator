#_______Version 0.9 _______
import random
import os
import array

import SReader

from SReader import Table

tab = Table()
Data = tab.getTableAndTransform()


DPExpended=0
GExpended=0

myEquipment=[12,True,0]
a = 0



class RiftEquipment:
	level = 0
	status = True
	rng = 0
	feedback = ' '
	
	attempts = 1
	successes = 0
	fails = 0
	
	def __init__(self,l):
		self.level = l
		self.status = True
		self.rng = 0
		self.feedback = ' '
	
	def upgrade(self):
		rng = random.randint(1,99)
		rfg = random.random()
		
		chancen = rng+rfg
		
		global DPExpended
		global GExpended
		
		self.attempts+=1
		
		chance_of_success = Data[ self.level ][1]
		chance_of_failure = Data[ self.level ][2]
		chance_of_unup = Data[ self.level ][3]
		
		GoldCost = Data[ self.level ][4]
		DimensionPieceCost = Data[ self.level ][5]
		
		cos = chance_of_success
		cof = chance_of_failure
		unp = chance_of_unup
		
		DPExpended += DimensionPieceCost
		GExpended += GoldCost
		
		if chancen >= (100-cos):
			
			self.level += 1
			self.rng = rng
			self.feedback = "-Upgrade Success!--"
			levl = [self.level,self.status,self.rng,self.feedback]
			self.successes += 1
			return levl
			
		elif (chancen < (cof+unp))and (chancen>unp):
			if self.level%5==0:
				self.rng = rng
				self.feedback = "--'UpgradeFailed'--"
				levl = [self.level,self.status,self.rng,self.feedback]
				self.fails += 1
				return levl
			else:
				self.level-=1
				self.rng=rng
				self.feedback = "--'UpgradeFailed'--"
				levl = [self.level,self.status,self.rng,self.feedback]
				self.fails += 1
				return levl
				
			
		elif chancen <= unp:
			
			self.status = False
			self.rng = rng
			self.feedback = "--Unupgradeable--"
			levl = [self.level,self.status,self.rng,self.feedback]
			self.fails += 1
			return levl
		
		print([self.level,self.status,self.rng],"   ",self.feedback)
		
	
	def getStats(self)->list:
		return [self.level,self.status,self.rng]
		
	def getAttempts(self)-> int:
		return self.attempts

#myEquipment = RiftEquipment(27)

#while myEquipment.status == True:
#	print(myEquipment.upgrade())
	#print(myEquipment.getStats())

#print("Gold Expended : ",GExpended, "    DimensionPiece Expended : ", DPExpended)


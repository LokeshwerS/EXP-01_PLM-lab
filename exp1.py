"""
Created on Sun Aug 24 2021
@author: Lokeshwer S
"""
import math 
import numpy as np 

class mps:
	def __init__(self,inventory,demand,sechduled_reciept,no_of_weeks):
		self.inv=inventory
		self.gr=demand
		self.sr=sechduled_reciept
		self.len=no_of_weeks

	def poh(self):
		poh=[]
		new_inv=self.inv
		for i in range(self.len):
			temp=new_inv+self.sr[i]-self.gr[i]
			if(temp<0):
				temp=0
			poh.append(temp)
			new_inv=new_inv+self.sr[i]-self.gr[i]
		return poh
	
	def pnr(self):
		pnr=[]
		poh=self.poh()
		pnr.append(0)
		for i in range(1,self.len):
			temp=self.gr[i]-poh[i-1]
			if(temp<0):
				temp=0
			pnr.append(temp)
		return pnr
	def por(self):
		por=[]
		pnr=self.pnr()
		for i in range(2,self.len):
			por.append(pnr[i])
		for i in range(2):
			por.append(0)
		return por
		

#inputs
no_of_weeks=8
dem=[150,0,70,0,175,0,90,60]
inv=[260,60,40,80]
#Scheduled reciepts
sr_c=[0, 0, 0, 0, 0, 0, 0, 0]
sr_s=[50, 0, 0, 0, 0, 0, 0, 0]
sr_b=[10, 0, 0, 0, 0, 0, 0, 0]
sr_l=[0, 0, 0, 0, 0, 0, 0, 0]
#Object creation
chair=mps(inv[0],dem,sr_c,no_of_weeks)
dem=[0,0,135,0,90,60,0,0]
back=mps(inv[2],dem,sr_b,no_of_weeks)
seat=mps(inv[1],dem,sr_s,no_of_weeks)
dem=[a*4 for a in dem]
legs=mps(inv[3],dem,sr_l,no_of_weeks)
print('MPS')
print('Chair')
print('Gross requirement \t :', chair.gr)
print('Scheduled reciept \t:', chair.sr)
print('Projected on-Hand \t:', chair.poh())
print('Projected net requirement :', chair.pnr())
print('Planned order receipt \t :', chair.pnr())
print('Planned order release \t :', chair.por())
print()
print('Seat')
print('Gross requirement \t :', seat.gr)
print('Scheduled reciept \t:', seat.sr)
print('Projected on-Hand \t:', seat.poh())
print('Projected net requirement :', seat.pnr())
print('Planned order receipt \t :', seat.pnr())
print('Planned order release \t :', seat.por())
print()
print('Back')
print('Gross requirement \t :',back.gr)
print('Scheduled reciept \t:', back.sr)
print('Projected on-Hand \t:', back.poh())
print('Projected net requirement :', back.pnr())
print('Planned order receipt \t :', back.pnr())
print('Planned order release \t :', back.por())
print('Legs')
print('Gross requirement \t :',legs.gr)
print('Scheduled reciept \t:', legs.sr)
print('Projected on-Hand \t:', legs.poh())
print('Projected net requirement :', legs.pnr())
print('Planned order receipt \t :', legs.pnr())
print('Planned order release \t :', legs.por())
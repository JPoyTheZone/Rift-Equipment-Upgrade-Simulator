try:
	import gspread
except e:
	print(e)
ServiceAccount = gspread.service_account(filename='kgcriftequipsimulator-ce4ca5c8fdde.json' )
#Create a service account object that uses this key.

SpreadSheet= ServiceAccount.open("RiftEquipmentProb")
#Requests to open the file in Google API using service account

worksheet = SpreadSheet.worksheet('Sheet1')
#create a worksheet object, its just a single sheet of the spreadsheet

Alldata = worksheet.get_all_values()
#gets all used cells

def printSpreadSheetName()->str:
	return SpreadSheet

def printData():
	for row in Alldata:
		try:
			print(int(row[0]))
			
		except:
			print(str(row[0]))
	

class Table:
	data = []
	
	def __init__(self):
		self.data = Alldata
	
	def getTableData(self)->list:
	
	#Request the raw table data
		return data
	
	def getTableAndTransform(self)->list:
	#This Function is made to transform the Value Range into their respective data types.
		Table = []
		
		for row in Alldata:
			r=[]
			for col in row:
				
				try:
					r.append(int(col))#Data can be int	
				except:
					r.append(str(col))#Data can be str
			
			Table.append(r)
		return(Table)
	
tab = Table()

k = printSpreadSheetName()

url = ('https://docs.google.com/spreadsheets/d/'+str(k.id.replace(" "," "))+'/edit?usp=drivesdk')
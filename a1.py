# Name : Rupanshoo Saxena
# Roll No : 2019096
# Group : 6 (SECTION A)

import urllib.request  #for Task 1.1
import datetime  #for Task 4


def getLatestRates():   #Task 1.1: uses the above imported library to get latest json string
	""" Returns: a JSON string that is a response to a latest rates query.

	The Json string will have the attributes: rates, base and date (yyyy-mm-dd).
	"""
	url = urllib.request.urlopen("http://api.exchangeratesapi.io/latest")
	data = url.read()   #reads json string
	return data



def getSpecificRates(date): #additional function made to get json string of the specified date
	urlSpec = urllib.request.urlopen("http://api.exchangeratesapi.io/" + str(date))
	dataSpec = str(urlSpec.read()) #reads json string and stores it in the form of normal string
	return dataSpec  #returns normal string




def getRangeOfRates(sDate,eDate): #additional function made to get json strings between given time period(includes data of start name and doesnot take data of end date)
	url3 =  urllib.request.urlopen("https://api.exchangeratesapi.io/history?start_at="+str(sDate)+"&end_at="+str(eDate))
	data3 = str(url3.read())
	return data3  #returns string



def changeBase(amount, currency, desiredCurrency, date):   #Task 1
	""" Outputs: a float value f.
	"""

	t1 = getSpecificRates(date)  #stores json string of that specific date in the form of a normal string
	cur1 = t1.find(currency)     #stores index of current currency from the string
	cur2 = t1.find(desiredCurrency) #stores index of desired currency from the string

	if(cur1 == -1 or cur2 == -1):  #when either of the currencies entered is not present in the string - show error
		return "Wrong currency entered"
	else:


		if currency == "EUR":  #when currency is Euro
			if desiredCurrency == "EUR": #when desired currency is also Euro
				return amount

			temp4 = t1[cur2:] #slices string from the index of the desired currency till the end
			temp5 = temp4.find(",")
			temp6 = temp4.find(":")
			cur2Val = float(temp4[temp6+1:temp5]) #slices string such that it stores the value of the desired currency which is present between the : and ,
			return amount * cur2Val

		temp1 = t1[cur1:] #slices string from the index of the current currency till the end
		temp2 = temp1.find(",")
		temp3 = temp1.find(":")
		cur1Val = float(temp1[temp3+1:temp2]) #slices string such that it stores the value of the current currency which is present between the : and ,
		 
		if desiredCurrency == "EUR":  #when desired currency is EURO
			return amount / cur1Val

		temp4 = t1[cur2:] #slices string from the index of the desired currency till the end
		temp5 = temp4.find(",")
		temp6 = temp4.find(":")
		cur2Val = float(temp4[temp6+1:temp5]) #slices string such that it stores the value of the desired currency which is present between the : and ,
		#print(cur2Val)
	return ((float(cur2Val)/float(cur1Val))*float(amount))  #logic for converting given value from current to desired currency

#print(changeBase(250,"EUR","CNY","2017-06-25"))
#json = getLatestRates()

def valuesList(t2):   #additional function to put all the values of the currency in order of occurence in the json string in a list
 	t2 = str(t2)    #json string converted to str
 	asc = []        #empty list created 
 	temp7 = t2.find(":") 
 	temp8 = t2.find("}")
 	t2 = t2[temp7+1:temp8+1]  #slices string such that the initial part before : and end part after } is removed
 	temp12 = t2.find("MYR")   
 	for i in range(len(t2[0:temp12])): 
 		temp9 = t2.find(":")
 		temp10 = t2.find(",")
 		asc.append(float(t2[temp9 + 1:temp10]))
 		t2 = t2[temp10+1:]
 		if(i==31):
 			break

 		
 	
 	return asc

b = getLatestRates() 
c = valuesList(b)




def printAscending(json):  #Task 2
	""" Output: the sorted order of the Rates 
		You don't have to return anything.
	
	Parameter:
	json: a json string to parse
	"""
	json = valuesList(json)
	ascTemp = []
	for i in range(len(json)):   #finds the min value in the unsorted list, appends that value in a temporary list and removes it from the original list
		temp11 = min(json)    
		ascTemp.append(temp11)
		json.remove(temp11)
	json = ascTemp  #temporary list is stored back into the original list
	#print(json)


	for i in range(len(json)):            #loop for getting output in given form with display of the names of currencies
		asc2 = str(getLatestRates())
		temp13 = asc2.find(str(json[i])) 
		temp14 = asc2[temp13 - 3:temp13 - 6:-1]
		print("1 Euro = " + str(json[i]) + ' ' + temp14[::-1])
		asc2 = asc2[:temp13 - 2] + asc2[temp13:]
		


#printAscending(b)



def extremeFridays(startDate, endDate, currency): #Task 3 : ASSUMPTION- end date's data will also be included
	""" Output: on which friday was currency the strongest and on which was it the weakest.
		You don't have to return anything.
		
	Parameters: 
	stardDate and endDate: strings of the form yyyy-mm-dd
	currency: a string representing the currency those extremes you have to determine
	"""
	t3 = getRangeOfRates(startDate,endDate)
	tdelta1 = datetime.timedelta(days=1) #timedelta prints date of the day according to the count given in the brackets i.e. if days = 7 then it will give date of the day after 7 days
	tdelta2 = datetime.timedelta(days=7) #count of days = 7
	friday=[] #list to store all dates which occur on a friday in the given range
	date1 = datetime.datetime.strptime(startDate,'%Y-%m-%d').date()  #to convert the date from str to datetime
	date2 = datetime.datetime.strptime(endDate,'%Y-%m-%d').date()
	while(date1.weekday()!=4):
		date1 = date1 + tdelta1  #for finding the first friday
	friday.append(str(date1))

	while(date1 < date2):   #adding 7 to get next friday
		date1 = date1 + tdelta2
		friday.append(str(date1)) 

	if(date2.weekday()!=4):   #condition for when the end date is not a friday
		del friday[-1]
	#print(friday)

	

	Dict = {}  #for making a dictionary by the name Dict

	for i in range(len(friday)):       #for storing the values of the given currency in the dictionary with the dates as keys
		temp15 = t3.find(friday[i])
		temp16 = t3[temp15:]
		temp17 = temp16[:temp16.find('}')]
		temp18 = temp17[temp17.find(currency):]
		temp19 = temp18[5:temp18.find(',')]
		if (temp19 == ''):
			continue
		Dict[friday[i]] = temp19 
	
	#print(Dict)
	max_value = max(Dict.values())  #gives max value of currency
	min_value = min(Dict.values())  #gives minimum value of currency
	
	print(currency + " was weakest on " + max(Dict, key=Dict.get) + ". 1 Euro was equal to " +  max_value + " " + currency)  #higher the value of the currency, weaker the currency
	print(currency + " was strongest on " + min(Dict, key=lambda k:Dict[k]) + ". 1 Euro was equal to " +  min_value + " " + currency) #lesser the value of the currency, stronger the currency


#extremeFridays("2019-02-16","2019-06-28","CAD")




def findMissingDates(startDate, endDate):   #Task 4
	""" Output: the dates that are not present when you do a json query from startDate to endDate
		You don't have to return anything.

		Parameters: stardDate and endDate: strings of the form yyyy-mm-dd
	"""
	t4 = getRangeOfRates(startDate,endDate)
	allDates = []   #list to store all the dates from start date to end date
	date3 = datetime.datetime.strptime(startDate,'%Y-%m-%d').date()  
	date4 = datetime.datetime.strptime(endDate,'%Y-%m-%d').date()  
	tdelta = datetime.timedelta(days=1)
	
	while(date3 <= date4):   #including end Date too
		allDates.append(str(date3))
		date3 = date3 + tdelta
	

	missing = []  #list to store all the missing dates

	for i in range(len(allDates)):
		temp19 = t4.find(allDates[i])

		if(temp19 == -1):           #if the date was not there in the json module
			missing.append(allDates[i])
	
	
	print("The following dates were not present:\n")
	for i in range(len(missing)):
		print(missing[i]+'\n')

#findMissingDates("2018-01-01","2018-09-01")

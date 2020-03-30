# Name : Rupanshoo Saxena
# Roll No : 2019096
# Group : 6 (SECTION A)

import unittest
from a1 import changeBase

# TEST cases should cover the different boundary cases.

class testpoint(unittest.TestCase):
	
	def test_change_base(self):
		self.assertEqual(changeBase(1, "INR", "GBP", "2010-10-25"), 0.014340456298200513)     #changing base from weaker currency(greater value) to stronger currency(lesser value) 
		self.assertAlmostEqual(changeBase(250, "INR", "GBP", "2010-10-25"), 3.585114074550128, delta = 0.1)

		self.assertEqual(changeBase(250,"RUB","IDR","2018-10-25"),57903.51668169522)  #Changing base from stronger currency(lesser value) to weaker currency(greater value)
		self.assertAlmostEqual(changeBase(100,"RUB","IDR","2018-10-25"),23161.406672678087, delta = 0.1)
		
		self.assertAlmostEqual(changeBase(250,"EUR","CNY","2017-06-25"),1910.325, delta = 0.1)       #when current currency is EURO
		self.assertAlmostEqual(changeBase(100,"EUR","CNY","2017-06-25"),764.13, delta = 0.1)
		
		self.assertAlmostEqual(changeBase(250,"NOK","EUR","2015-12-05"),27.0284880264, delta = 0.1)   #when desired currency is EURO
		self.assertAlmostEqual(changeBase(100,"NOK","EUR","2015-12-05"),10.81139521, delta = 0.1)
		
		self.assertEqual(changeBase(250,"EUR","EUR","2017-06-25"),250.0)   #when both current currency and desired currency is EURO
		self.assertEqual(changeBase(100,"EUR","EUR","2018-10-25"),100)
		
		self.assertEqual(changeBase(250,"DKK","CND","2017-06-25"),"Wrong currency entered")  #when wrong desired currency is entered
		self.assertAlmostEqual(changeBase(100,"RUP","IDR","2018-10-25"),"Wrong currency entered", delta = 0.1) #when wrong current currency is entered
		
		self.assertEqual(changeBase(0,"DKK","IDR","2019-01-01"),0) #when amount=0
		self.assertAlmostEqual(changeBase(0,"DKK","IDR","2019-01-01"),0) 
		
		self.assertEqual(changeBase(250,"JPY","JPY","2019-04-28"),250) #when currency and desired currency are the same
		self.assertAlmostEqual(changeBase(100,"JPY","JPY","2019-04-28"),100) 

		self.assertAlmostEqual(changeBase(100,"JPY","JPY","2019-04-28"),100) #when currency and desired currency are the same


		# these are just sample values. You have to add testcases (and edit these) for various dates.
		# (don't use the current date as the json would keep changing every 4 minutes)
		# you have to hard-code the 2nd parameter of assertEquals by calculating it manually
		# on a particular date and checking whether your changeBase function returns the same
		# value or not.




if __name__=='__main__':
	unittest.main()
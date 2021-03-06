"""
Problem 3
---------

In Laxmitown, one can exchange a coin of amount X, with three coins of amounts X/2, X/3 and X/4.
But coins cannot be converted if the result is a fractional value. Only whole numbers are valid.

For example, if one deposits a coin worth 36, he get back 3 coins: 18, 12 and 9, with a value of 39
Further 12 can be exchanged for coins: 6, 4 and 3, totalling to 13. The final value being 39 + 13 = 52.
Note that 18 cannot be exchanged further, because 18/4 does not result in a whole number.

Given a number X, write a program to find the maximum value it can be exhanged for.

Owner -Sanjay

"""

class LaxmitownSumClass:
    """Class to have all the functions related to the Sum"""
    
    def __init__(self):
        """constructor function with initial exchange value 0"""
        
        self.amount = 0     
        self.coins_fraction = [2.0, 3.0, 4.0]                                                               #set the fraction as per the requirement
    
    def isWhole(self, x):
        """function to check whether a number is whole number or not"""
        
        if(x % 1 == 0): return True
        else: return False
        
    def IsAllCoinsWhole(self, coin_val):  
        """check whether all the three coins are whole number"""     
         
        return self.isWhole(coin_val / 2.0) and self.isWhole(coin_val / 3.0) and self.isWhole(coin_val / 4.0) #all the fractions should be whole numbers
        
    def callMaxExchangeVal(self, x): 
        """ calculate Maximum Exchange value  """   
        
        for fraction in self.coins_fraction:                
            if self.isWhole(x / fraction):
                if self.IsAllCoinsWhole(x / fraction):                
                    self.callMaxExchangeVal(x / fraction)                                                      # recursive call for child fractions        
                else: 
                    self.amount += x / fraction
            else:
                self.amount += x / fraction
        return 


if __name__ == '__main__':    
    """main method """
    
    specialSum = LaxmitownSumClass()     
    amount = int(input("Please enter coin amount... " ))       
    if specialSum.IsAllCoinsWhole(amount):
        specialSum.callMaxExchangeVal(amount)  
    else:
         specialSum.amount = amount
    print ("Maximum exchange value is " + str(int(specialSum.amount))  +"  :)" )

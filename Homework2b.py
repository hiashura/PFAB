price = input("What is the price of the item?")
 
tax = input("What is the desired rate for sales tax?(expressed as 9.11 without per
cent symbol)")
 
amttax = price * (tax/ 100)
tot = price + amttax                                                              
 
print "If the", price, "is, and the tax is", tax, "%; then the amount of tax is", 
round(amttax, 2), "and the total is", round(tot, 2), "."    
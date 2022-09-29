bill = int(input("Enter amount of bill:"))
people = int(input("Enter number of people:"))
tips = int(input("Enter amount of tips (%):"))

totaltip = bill * tips / 100
pertip = totaltip / people
totalamount = totaltip + bill
perpeople = totalamount / people

print("\nTip amount per person $%.2f"%pertip)
print("\nTotal amount per person $%.2f"%perpeople)
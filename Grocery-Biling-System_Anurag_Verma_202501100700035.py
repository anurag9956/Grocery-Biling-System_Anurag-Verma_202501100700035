price1=float(input("Enter Price for item 1: "))
price2=float(input("Enter Price for item 2: "))
price3=float(input("Enter Price for item 3: "))

totalCost=price1+price2+price3 #Adding prices 
originalTotal=totalCost
discount=0.0

if (totalCost>50):
    discount=(0.1)*totalCost #Discount Calculation
    totalCost=totalCost-discount

print(f'Original Total : ${originalTotal}')

if (discount>0):
    print("Discount Applied : Yes")
    print(f'Final Amount : ${totalCost}')
else:
    print("Discount Applied : No")
    print(f'Final Amount : ${totalCost}')
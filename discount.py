price = int(input("Enter price: "))
quantity = int(input("enter quantity: "))

total = price*quantity
print("total payable. " , total)

if total > 1000:
    print ("10% discount is applicable")
    discount1000 = total*10/100
    print(discount1000)
    finalpayable = total - discount1000
    print("amount payabble: ", finalpayable)
elif total > 500 and total <1000:
    print("5% discount is applicable ")
    discount500 = total*5/100
    finalpayable = total - discount500
    print("amoun payable: ",  finalpayable)
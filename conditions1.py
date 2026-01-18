acutal_amount = float(input("Enter a acutal amount:"))
sale_amount = float(input("Enter a sale amount:"))
if (sale_amount>acutal_amount):
    print("profit!")
    a = sale_amount-acutal_amount
    print(f"we had a profit of ${a}")   
elif (sale_amount==acutal_amount):
    print("It was neither profit not loss")     
else:
    loss = acutal_amount-sale_amount 
    print(f"loss! {loss}")    
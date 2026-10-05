units_consumed=int(input("enter units consumed"))
if(units_consumed<=100):
    total_bill=units_consumed*2
    print(f"total bill {total_bill}")
elif(units_consumed>=101 and units_consumed<=200):
    total_bill=units_consumed*4
    print(f"total bill {total_bill}")
elif(units_consumed>=201 and units_consumed<=300):
    total_bill=units_consumed*6
    print(f"total bill {total_bill}")
elif(units_consumed>300):
    total_bill=units_consumed*8
    print(f"total bill {total_bill}")
else:
    print("invalid units")
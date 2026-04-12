#TODO 7:Calculate the compound interest for a given principal 
# amount, interest rate, and time period

# “P multiplied by (1 plus R divided by 100) raised to the power of T.”
# final amt =  P × (1 + R/100)^T

amount = int(input("enter the amount."))
interest_rate = float(input("enter the % of interest for an amount:"))
time = int(input("enter the time"))

def compound_interest(p, r, t):
    final_amount = round(p * (1 + r/ 100) ** t, 2)
    CI = round(final_amount - p,2)
    return final_amount, CI    
final_amount, CI = compound_interest(p = amount, r=interest_rate, t=time)

print(f"The Final amount is: {final_amount}")
print(f"Compund interset earned: {CI}")
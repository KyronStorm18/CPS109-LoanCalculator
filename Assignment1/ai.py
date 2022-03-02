#The problem: Students often have trouble paying off loans. The following code will help students plan out either how much they need to pay per payment period or how long it will take to pay off their loan. This will be done by using the Amortized Loan formula and Payoff Loan formula respectively.

#Amortized Loan function ('AL'):
def amortized_loan(amount1,term1,i1,n1,p1):
    #Change the interest percentage into an actual number
    i1 = i1/100
    #Need the compounding periods per payment periods which can be computed using compounding periods and payment periods
    c = n1/p1
    #Changes the annual percentage rate (APR) into effective interest rates per payment period
    r = (1+(i1/n1))**c - 1
    #Need to find the total number of payments over the lifespan of the loan 
    lifespan = p1*term1
    #We will be using a formula called the capital recovery formula to find how much each payment the user would need to pay given the parameters
    factor = (r*(1+r)**lifespan)/((1+r)**lifespan - 1)
    #This will give you how much each payment will be to pay off the loan
    answer = round(amount1*factor,2)
    return answer

#Loan Payoff function ('LP'):
def loan_payoff(amount2,i2,ap):
    #Import math library since Loan Payoff formula requires log functions
    import math
    #Changes percentage into a real number
    i2 = i2/100
    #Changes APY to APR
    r = i2/12
    #Finds how long it will take to pay off loan using payoff loan formula
    dividend = math.log(ap/(ap-amount2*r))
    divisor = math.log(1+r)
    answer = int(dividend//divisor)
    return answer

if __name__=="__main__":
    #Asking the user if they want to know how much they would need to pay each payment period (Amortized Loan) or if they want to know how long it would take to pay their loan (Loan Payoff)
    print("Hello! I am the loan calculator! What would you like to calculate today?")
    print("Enter 'AL' to calculate an Amortized Loan")
    print("Enter 'LP' to calculate a Loan Payoff ")
    mode = input()
    
    #If the user inputs anything else, it would tell the user to enter a valid input
    while mode != 'AL' and mode != 'LP':
        print("Invalid input")
        print("Enter 'AL' to calculate an Amortized loan")
        print("Enter 'LP' to calculate a Loan Payoff ")
        mode = input()
    
    #This will trigger Amortized Loan function
    print("---------------------------------------------------------------------------------")
    if mode == 'AL':
       #Code will ask user for all the parameters needed to find how much they would need to pay for each payment period over the course of the lifespan of the loan.
       amount = float(input("Enter the loan amount in CAD: "))
       term = float(input("Enter a loan term in years: "))
       rate = float(input("Enter an interest rate (%): "))
       
       #Will show all the possible values that can be inputted for the following parameters
       print("---------------------------------------------------------------------------------")
       print("The following table are the possible inputs for the next questions:\n ")
       periods = ['Annually -> 1','Semi-Annually -> 2','Quarterly -> 4', 'Monthly-> 12','Semi-Monthly -> 24','Bi-Weekly -> 26','Weekly -> 52', 'Daily -> 365' ]
       for x in periods:
           print(x)
    
       print("---------------------------------------------------------------------------------")
       cmpd = int(input("What will be the compounding periods per year?\n"))
       pmt = int(input("What will be your payment periods per year?\n"))
       print("---------------------------------------------------------------------------------")

       #If the user does not input proper values
       s = [1,2,4,12,24,26,52,365]
       while cmpd not in s or pmt not in s:
           print("Invalid input!")
           cmpd = int(input("What will be the compounding periods per year?\n"))
           pmt = int(input("What will be your payment periods per year?\n"))
           print("---------------------------------------------------------------------------------")

       #Rounds the answer to 2 decimal places
       alanswer = amortized_loan(amount,term,rate,cmpd,pmt)
       print(f"You will make {int(term*pmt)} payments of ${alanswer} to pay off your loan :)")

    #This will trigger Payoff Loan function
    if mode == 'LP':
        #Code asks user for parameters 
        amount = float(input("Enter the loan amount in CAD: "))
        rate = float(input("Enter an interest rate (%): "))
        paypt = float(input("Enter the expected monthly payment in CAD (must be at least 0.5% of the loan payment): "))
        print("---------------------------------------------------------------------------------")

        #If the user puts an invalid amount it will ask for a valid number
        while paypt<(0.005*amount):
            paypt = float(input("Too small! Enter the expected monthly payment in CAD (must be at least 0.5% of the loan):\n "))
            print("---------------------------------------------------------------------------------")
        #Note that this formula does not ask for payment periods or compounding periods. This is due to the fact that the payoff formula can only calculate durations using monthly payments and annual percentage rate (APR)
        
        #Calls Loan Payoff function
        lpanswer = loan_payoff(amount,rate,paypt)
        print(f"It will take {lpanswer} months or {round(lpanswer/12,2)} years to pay off your loan :)")
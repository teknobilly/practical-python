# mortgage.py
#
# Exercise 1.7
# Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with 
# Guido’s Mortgage, Stock Investment, and Bitcoin trading corporation. The 
# interest rate is 5% and the monthly payment is $2684.11.

# Exercise 1.8
# Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?
# Modify the program to incorporate this extra payment and have it print the 
# total amount paid along with the number of months required.
#
#When you run the new program, it should report a total payment of 929,965.62 over 342 months.

# Exercise 1.9
# Modify the program so that extra payment information can be more generally 
# handled. Make it so that the user can set these variables:
#
# extra_payment_start_month = 61
# extra_payment_end_month = 108
# extra_payment = 1000
#
# Make the program look at these variables and calculate the total paid appropriately.
#
# How much will Dave pay if he pays an extra $1000/month for 4 years starting 
# after the first five years have already been paid?



principal    = 500000.00
rate_decimal = 0.05
payment      = 2684.11
total_paid   = 0.0
extra_amount = 0.00
# extra_paycnt = 12 # exercise 1.8
paid_amt     = 0.00
iteration    = 0
extra_payment_start_month = 61 #exercise 1.9
extra_payment_end_month = 108  #exercise 1.9
extra_payment = 1000.00         #exercise 1.9

print("Daves mortgage calculation \r\n\r\n\r\n")
print("Principal:       $",principal)
print("Lending Rate:     ", rate_decimal * 100, "%")
print("Monthly Payment: $", payment)
print("Total Paid:      $", total_paid)

while round(principal, 2) > 0.00:
    iteration += 1   # Month(payment)  count
    print( "Month", iteration, end=" " )

    # If iteration is <= 12 apply the extra payment amount
    ##extra_amount = extra_amount if iteration <= extra_paycnt else 0.0 #exercise 1.8
    if (iteration >= extra_payment_start_month) and (iteration <= extra_payment_end_month) :
        extra_amount = extra_payment
    else:
        extra_amount = 0.0  #exercise 1.9

    paid_amt = round( payment + extra_amount, 2)
    
    # calculate pricipal 
    principal    = principal * (1 + rate_decimal / 12) - paid_amt
    total_paid  += paid_amt
    
    # Display monthly balance
    print( "Payment Amount: $", paid_amt ,  end=' ')
    print( "Total Paid: $",     round(total_paid,2), end=' ')
    print(" Principal Amount: $", round(principal,2) )
    
    # Exercise 1.11 calculate if this is the last payment and determine it's amount
    payment = payment  if ( round(principal,2) - paid_amt >= 0 )  else  ( round(principal * (1 + rate_decimal /12), 2) )


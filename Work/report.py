# report.py
#
# Exercise 2.4

'''
In Exercise 2.7, you wrote a program called report.py that computed the gain/loss of a stock portfolio. In this exercise, you’re going to start modifying it to produce a table like this:

      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84

In this report, “Price” is the current share price of the stock and “Change” is the change in the share price from the initial purchase price.

In order to generate the above report, you’ll first want to collect all of the data shown in the table. Write a function make_report() that takes a list of stocks and dictionary of prices as input and returns a list of tuples containing the rows of the above table.

Add this function to your report.py file. Here’s how it should work if you try it interactively:
'''


def read_portfolio(filename):
    if not filename:
        return []
    file = op
    

def read_prices():

def make_report():    


def print_portfolio_astable( portfolio_data ):
    #  outputs a formatted table from the raw data of the parameter
        
    # Validate the portfolio_data
    try:
        print_data = tuple(portfolio_data)
    except tableerr as error:
        print("Data incompatible to print", tableerr)
           
    # define the column widths
    col_width = 10
    prec_val = 2
    
    # print the table header
    # print column seperator
    
    # Iterate through each line of data:
        # Format and output the line data

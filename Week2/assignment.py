def main():
    # This function gets the distance travelled and gallons use
    # and prints the fuel efficiency in miles per gallon and
    # litres per 100 kilometer
    # returns nothing
    start_in_miles = float(input('Enter the starting odometer reading (miles): '))
    end_in_miles = float(input('Enter  the Ending odometer reading (miles): '))
    amt_in_gallons = float(input('Enter the gallons of fuel used: '))
    mpg = miles_per_gallon(end=end_in_miles,start=start_in_miles, gallons=amt_in_gallons)
    print(f'{mpg:.2f} miles per gallon\n'
          f'{lp100k_from_mpg(mpg):.2f} litres per 100 km')
def miles_per_gallon(end=0.0, start=0.0, gallons=0.0):
    # This function computes the fuel efficiency in miles per gallon
    # returns the miles per gallon in efficieny
    return (end - start)/gallons
def lp100k_from_mpg(mpg):
    return 235.215/mpg
main()
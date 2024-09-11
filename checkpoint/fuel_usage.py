def main():
    # Get an odometer value in U.S. miles from the user.
    starting_odometer = float(input("\nEnter the first odometer reading (miles): "))

    # Get another odometer value in U.S. miles from the user.
    ending_odometer = float(input("Enter the second odometer reading (miles): "))

    # Get a fuel amount in U.S. gallons from the user.
    fuel_used = float(input("Enter the amount of fuel used (gallons): "))

    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = miles_per_gallon(starting_odometer, ending_odometer, fuel_used)

    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)

    # Display the results for the user to see.
    print(f"{mpg:.2f} miles per gallon")
    print(f"{lp100k:.2f} liters per 100 kilometers\n")


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    fuel_efficiency_mpg = (end_miles - start_miles) / amount_gallons
    return fuel_efficiency_mpg

def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    converted_mpg = 235.215 / mpg
    return converted_mpg

# Call the main function so that
# this program will start executing.
main()
import matplotlib.pyplot as plt
import datetime as datet
from math import pi

def draw_bar() :

    # Data
    labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
    sizes = [30, 25, 20, 25]

    # Create bar chart
    plt.bar(labels, sizes)

    # Add title and labels
    plt.title('Fruit Distribution')
    plt.xlabel('Fruits')
    plt.ylabel('Quantity')

    # Show chart
    plt.show()

def draw_pie() :

    # Data
    labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
    sizes = [30, 25, 20, 25]

    # Create pie chart
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')

    # Add title
    plt.title('Fruit Distribution')

    # Show chart
    plt.show()

def find_area_of_cylinder(radius_base, height):
    area = ( 2 * pi * (radius_base ** 2) ) + ( 2 * pi * radius_base * height)
    return area   

def date_time_functions() :  
    todays_date = datet.datetime.now()
    return todays_date

def temperature_conversion_program(temperture, convert_to) :
    if(convert_to == "F") :
       temp = (9 * temperture)/5 + 32
       return f"The temperature in fahrenheit is {temp: .2f}" 
    elif (convert_to == "C") :
          temp = (temperture - 32)*5/9
          return f"The temperature in celsius is {temp: .2f}"
    else :
        return "You entered an invalid convert"    

def factorial(num) :
    fact = 1
    step = 1
    while step <= num :
        fact = fact * step
        step = step + 1
    return fact   

def find_largest_of_n_numbers(n):
    step = 1
    greatestnumber = 0
    while step <= n :
       num = int(input(f"Enter number {step}"))
       if(greatestnumber < num) :
         greatestnumber = num
       step = step + 1 
    return greatestnumber

def input_numbers_into_an_array() :
    arr = list(map(int, input("Enter numbers separated by space: ").split()))
    largest_number_in_array = max(arr)
    smallest_number_in_array = min(arr)
    return largest_number_in_array, smallest_number_in_array 




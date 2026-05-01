import helper as hlp

print("Hello World")
print("This is the data for today")
print("First of all here is today's date in various formats")
td = hlp.date_time_functions()
print(td.strftime("%Y-%m-%d"))     
print(td.strftime("%d/%m/%Y"))     
print(td.strftime("%A, %B %d"))    
print(td.strftime("%I:%M %p"))    

print(f"{td: %Y-%m-%d}")
area_cylind = hlp.find_area_of_cylinder(3, 4)

print("Let us convert some temperatures")
converted_temperature = hlp.temperature_conversion_program(32, "F")
print(converted_temperature)
converted_temperature = hlp.temperature_conversion_program(180, "C")
print(converted_temperature)
converted_temperature = hlp.temperature_conversion_program(180, "X")
print(converted_temperature)

print(f"area of cylinder today is {area_cylind:.2f}")
factorial = hlp.factorial(0)
print(f"{factorial}")
largestnumber = hlp.find_largest_of_n_numbers(3)
print(f"The largest number you entered is {largestnumber}")
largestnumber_in_array_input, smallest_number_in_array_input = hlp.input_numbers_into_an_array()
print(f"The largest number you entered is {largestnumber_in_array_input} and the smallest is {smallest_number_in_array_input}")

#hlp.draw_bar()
#hlp.draw_pie()

###  mr. usuf

print("MR.YUSUF AND SONS ")
print("To calculate simple intrest and compound intrest, enter the required details.")
initial_principal = float(input("Enter your initial principal:  "))
interest_rate = float(input("Enter your initial rate:  "))
number_of_times_interest_per_time_period = float(input("Enter number of times interest per time period:  "))
number_of_time_period_elapse = float(input("Enter your number of time period elapsed :  "))

simple_intrest = initial_principal *(1 + interest_rate * number_of_times_interest_per_time_period)
compound_intrest = initial_principal * (1+(interest_rate/number_of_time_period_elapse))**number_of_time_period_elapse*number_of_times_interest_per_time_period

print("YUSUF AND SONS COMPANY")
print(f'Simple intrest :  {simple_intrest}')
print(f'Compound intrest : {compound_intrest}')

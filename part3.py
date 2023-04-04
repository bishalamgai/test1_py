def convertSalary(salary, country):
    if country == 'Canada':
        converted_salary = salary * 1
        currency_name = 'CAD'
        average_salary = 64000
    elif country == 'USA':
        converted_salary = salary * 1.18
        currency_name = 'USD'
        average_salary = 56516
    elif country == 'Cambodia':
        converted_salary = salary * 0.0002063
        currency_name = 'Cambodian riel'
        average_salary = 5649856
    elif country == 'United Kingdom':
        converted_salary = salary * 0.91
        currency_name = 'Pound Sterling'
        average_salary = 35423
    else:
        print('Invalid country input')
        return
    
    if converted_salary > average_salary:
        print(f'You will be rich in {country} with a salary of {converted_salary:.2f} {currency_name}')
    else:
        print(f'You will be poor in {country} with a salary of {converted_salary:.2f} {currency_name}')
    return converted_salary


salary = float(input('Please enter your salary in Germany: '))
country = input('Enter the country you want to migrate to: ')

convertSalary(salary, country)

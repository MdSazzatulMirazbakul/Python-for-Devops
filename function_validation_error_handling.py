# def electricity_bill(unit, price_per_unit):
#     bill = unit * price_per_unit
#     return  bill
# result = electricity_bill(100, 13)
# print("Total Electricity bill", result)


# def electricity_bill(units, price_per_unit):
#     if units < 0:
#         return "Units can not be negetive"
#     if price_per_unit < 0:
#         return "price can not be negetive"
#     bill = units * price_per_unit
#     return bill
# result = electricity_bill(120, 8)
# print("Total electricity bill: ", result)

# Raising Errors
def electricity_bill(units, price_per_unit):
    if units < 0:
        raise ValueError ("Units can not be negetive")
    if price_per_unit < 0:
        raise ValueError ("Price can not be negetive")
    bill = units * price_per_unit
    return bill
# results = electricity_bill(150, 7)
# print("Total Electricity Bill: ", results)
# try:
#     results = electricity_bill(-150, 7)
#     print("Total Electricity bill: ", results)
# except ValueError as e:
#     print("Error: ", e)

# Type Validation

# def electricity_bill(units, price_per_unit):
#     if not isinstance(units, (int, float)):
#         raise TypeError("Units must be a number")
#     if not isinstance(price_per_unit, (int, float)):
#         raise TypeError("Price must be a number")
#     if units < 0:
#         raise ValueError("units can not be negetive")
#     if price_per_unit < 0:
#         raise ValueError("Price can not be negetive")
#     bill = units * price_per_unit
#     return bill
# try:
#     results = electricity_bill(150, -8)
#     print("Total electricity bill: ", results)
# except TypeError as t:
#     print("Error: ", t)
# except ValueError as e:
#     print("Value Error: ", e)

# Solar panel output calculator

def solar_energy_output(power_kw, sunlight_hours):
    if not isinstance(power_kw, (int, float)):
        raise TypeError("power must be in number")
    if not isinstance(sunlight_hours, (int, float)):
        raise TypeError("Hours should be in number")
    if power_kw <= 0:
        raise ValueError("Power can not be zero or negetive")
    if sunlight_hours < 0:
        raise ValueError("Time can not be negetive")
    enery_output = power_kw * sunlight_hours
    return enery_output
try:
    input = solar_energy_output(0, 9)
    print("Total Output: ", input)
except Exception as e:
    print("Error: ", e)
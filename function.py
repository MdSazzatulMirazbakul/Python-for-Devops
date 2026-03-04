# def great():
#     print("Hello")

# # great()

# def greet(name):
#     print("Hello!", name)

# greet("Bakul")
# greet("Miraz")
# greet("Sazzatul")


# def add(a, b):
#     return(a + b)

# result = add(4, 6)
# print(result)

# def multiply(a , b):
#     return(a * b)
# result = multiply( 13, 56)
# print(result)

# Standard Minute Balue Calculation

# def calculate_smv(operation_time, efficiency):
#     return(operation_time / efficiency)
# smv = calculate_smv(55, 0.73)
# print(smv)

# Production target calculation
# def production_target(smv, total_hours, workers):
#     total_minutes = total_hours * 60
#     return(total_minutes * workers) / smv
# target = production_target(75, 8, 120)
# print(target)

# calculatiing line efficiency
def line_efficiency(produced_pieces, smv, workers, working_hours):
    return(produced_pieces * smv) / (workers * working_hours * 60)
efficiency = line_efficiency(5000, 55, 150, 8)
print(efficiency)
"""This is to define a function to calculate the population density
"""
def population_density(population, land_area):
    return population * 1.0 / land_area

test1 = population_density(19, 1)
expected_result1 = 19
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(1500, 750)
expected_result2 = 2
print("expected result: {}, actual result: {}".format(expected_result2, test2))

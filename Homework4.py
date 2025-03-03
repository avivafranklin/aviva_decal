#2.1
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(numbers)

#2.2
def squarelist(numbers):
    return [number**2 for number in numbers]
squared_list = squarelist(numbers)
print(squared_list)

#2.3
def first_fifteen_elements(squared_list):
    return squared_list[:14]
print(first_fifteen_elements(squared_list))

#2.4
def every_fifth_element(squared_list):
    return squared_list[3::5]
print(every_fifth_element(squared_list))

#2.5
shortened_squared = squared_list[:-3]
def fancy_function(shortened_squared):
    return shortened_squared[::-3]
print(fancy_function(shortened_squared))

#3.1
def create_2d_list():
    matrix = []
    value = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(value)
            value += 1
        matrix.append(row)
    return matrix
_2d_list = create_2d_list()
print(_2d_list)

#3.2
def create_modified_2d_list(_2d_list):
    modified_list = []
    for row in _2d_list:
        new_row = []
        for i in range(len(row)):
            if row[i] %3 == 0:
             new_row.append("?")
            else:
                new_row.append(row[i])
        modified_list.append(new_row)
    return modified_list

modified_2d_list = create_modified_2d_list(_2d_list)
print(modified_2d_list)

#3.3
def sum_non_question_marks(modified_2d_list):
    total_sum = 0
    for row in modified_2d_list:
        for element in row:
            if element != "?":
                total_sum += element
    return total_sum
print(sum_non_question_marks(modified_2d_list))

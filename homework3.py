#1
def computePower(x,y):
    result = 1
    for i in range(y):
        result *= x
    return result
x=2
y=3
print(computePower(x,y))

#2
readings = [15, 14, 17, 20, 23, 28, 20]
def temperatureRange(readings):
    return min(readings), max (readings)
print(temperatureRange(readings))

#3
week = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
def isWeekend(day):
    if day in [6,7]:
        return "True"
    else:
        return "False"
day = 6
print(isWeekend(day))

#4
def fuel_efficiency(distance, fuel):
    efficiency = distance / fuel
    return round(efficiency, 2)
distance = 70
fuel = 21.5
print(fuel_efficiency(distance, fuel))

#5
def decodeNumbers(n):
    last_digit = n % 10
    remaining_digits = n // 10
    num_digits = 1
    while remaining_digits != 0:
        remaining_digits //= 10
        num_digits *= 10
    return last_digit * num_digits + (n//10)
n = 12345
print(decodeNumbers(n))

#6.1
nums = [2024, 98, 131, 2, 3, 72]

def find_min_with_for_loop(nums):
    min_value = nums[0]
    for num in nums:
        if num < min_value:
            min_value = num
    return min_value
print(find_min_with_for_loop(nums))

def find_max_with_for_loop(nums):
    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num
    return max_value
print(find_max_with_for_loop(nums))

#6.2
def find_min_with_while_loop(nums):
    min_value = nums[0]
    value = 1
    while value < len(nums):
        if nums[value] < min_value:
            min_value = nums[value]
        value += 1
    return min_value
print(find_min_with_while_loop(nums))

def find_max_with_while_loop(nums):
    max_value = nums[0]
    value = 1
    while value > len(nums):
        if nums[value] > max_value:
            max_value = nums[value]
        value += 1
    return max_value
print(find_max_with_while_loop(nums))

#7
text = "UC Berkeley, founded in 1868!"
def vowel_and_consonant_count(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return (vowel_count, consonant_count)
print(vowel_and_consonant_count(text))

#8
num = 2468
def digital_root(num):
    if num == 0:
        return 0
    return (num % 10) + digital_root(num // 10)
print(digital_root(num))

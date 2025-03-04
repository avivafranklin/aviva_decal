#1
#1 pwd
#2 ls
#3 cd .., cd brianna_repo, git pull homework.py
#4 git clone homework.py, mv brianna_repo/homework.py /python_decal/judy_decal
#5 cat homework.py, vim homework.py
#6 nano homework.py
#7 git add homework.py, git commit -m "adding homework.py", git push origin main
# 8 git pull origin main, someone editied the document and Judy had not saved those changes locally
# 9 ~/Recents


#2
#2.1
def checkDataType(x):
    return type(x)
print(checkDataType(5.14))
print(checkDataType(True))

#2.2
def evenOrOdd(x):
    if x%2 == 0:
        return "Even"
    else:
        return "Odd"
print(evenOrOdd(7))
print(evenOrOdd(10))


#3
numbers = [1, 2, 3, 4, 5]
def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(sumWithLoop(numbers))


#4
#4.1
letters = ['a', 'b', 'c']
def duplicateList(letters):
    result = []
    for letter in letters:
        result.append(letter)
        result.append(letter)
    return result
print(duplicateList(letters))

#4.2
def square(num):
    return num * num
num = 5
print(square(num))
# have to define num
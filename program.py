import fileinput

result = 0

for line in fileinput.input():
    resutl += line

print(result)

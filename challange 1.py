#Given the names and grades for each student in a class of N  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

#solution

sheet = []
for i in range(0,int(input())):
    sheet.append([input(), float(input())])

secHighest = sorted(list(set([marks for name, marks in sheet])))[1]
print('\n'.join([a for a,b in sorted(sheet) if b == secHighest]))
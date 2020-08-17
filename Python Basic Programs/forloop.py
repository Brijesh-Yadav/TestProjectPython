str = 'python';

for i in str:
    print(i);

list = [1,2,3,4,5]

#2nd loop
print('\n')
print('2nd Loop')
for i in list:
    print(i);

#3rd Loop
print('\n')
print('3rd Loop')
for i in range(10):
    print(i)

#4th Loop
print('\n')
print('4th Loop')
list = ['Peter','Joseph','Ricky','Devansh']
for i in range(len(list)):
    print(list[i])

#5th Loop
print('\n')
print('5th Loop')

for i in range(5):
    for j in range(i):
        print('*',end='');
    print();

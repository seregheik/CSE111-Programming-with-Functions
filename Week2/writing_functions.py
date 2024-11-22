from datetime import datetime

def print_time(task_name) :
    print(task_name)
    print(datetime.now())
    print()

name = 'Osasere'
print_time('fixed name')

for x in range(0,10):
    print(x)
print_time('put in name')
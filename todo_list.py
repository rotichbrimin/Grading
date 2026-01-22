
mark_as_done = 0
task1 = input("Enter first task :")
task2 = input("Enter second task :")

print(f"Your first task is {task1} and your second task is {task2}")

confirm1 = input(f"Is {task1} done ?(yes/no)").lower()
if confirm1 == 'yes':
    mark_as_done += 1

confirm2 = input(f"Is {task2} done ?(yes/no)").lower()
if confirm2 =='yes':
    mark_as_done +=1
    
print(f"You have completed {mark_as_done} out of 2 task.")
class Employee:
  
    def __init__(self):
        print('Employee created.')
  
    def __del__(self):
        print("Destructor called. Employee deleted.")
  
def create_obj():
    print('Making Employee...')
    obj = Employee()
    print('Function end...')
    return obj
  
print('Calling create_obj() function...')
obj = create_obj()
print('Program End...')
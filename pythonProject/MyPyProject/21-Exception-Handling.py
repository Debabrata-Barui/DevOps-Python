'''
Exception Handling :-
    try Block{
        This is the actual business code

        if try block has any exception{
            except or catch block will be executed and here exception will be highlighted
         }
        else{
            else block will be highlighted
        }
    }
    finally block will be executed everytime if try block has any exception or doesn't have any exception

'''

x=10
try:
    print("The value of the X is : ", x)
except:
    print("The X variable is not defined")
else:
    print("X is defined")
finally:
    print("Finally block is run allways")


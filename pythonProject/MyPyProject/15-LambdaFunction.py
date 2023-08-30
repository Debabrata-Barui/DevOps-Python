'''
Lambda Funtion :- A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

Syntax :
lambda arguments : expression

'''
x= lambda a: a + 10
print (x(5))


fun1= lambda a, b: a * b
print(fun1(10,20))

fun1= lambda a,b,c,d,e: a+b+c+d+e
print(fun1(10,20,30,40,50))

# Apply the Lambda Function inside the function
def ecpl(a):
    return lambda x: x * a


varForLambdaFun= ecpl(2) # Pass the argument for Lambda Function

print(varForLambdaFun(10)) # for Function

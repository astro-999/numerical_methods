eps = 0.0001
count = 0
flag = True
def f(x):
    return (x**2 - 4*x -10)
x1 = float(input('enter the intial values  of x1:'))
x2 = float( input('enter the intial values  of x2:'))
if f(x1)*f(x2)>0:
    print('no root exists') 
    flag = False 
while flag == True:
    count+=1 
    x0 = (x1 + x2)/2
    if f(x1)*f(x0)<0:
        x2 = x0
    else:
        x1 = x0
    
    root = round( (x1+x2)/2,4)
    print(f"Iteration :{count}")    
    print(f'root is :{root}\n')
    if abs((x2-x1)/x2)<eps:
        break
    if count == 50:
        break
if count == 50:
    print('try something else as inital')
    
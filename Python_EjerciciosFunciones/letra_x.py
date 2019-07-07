n=5
def letra_x(n):
    for i in range(n):
        lx = ''
        for j in range(n):
            if j in [i, n-i-1]:
                lx += '*'
            else:
                lx += ' '
        print(lx)
    return str(lx)

letra_x(5)



        
    
 


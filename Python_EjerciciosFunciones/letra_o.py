n=5
def letra_o(n):
     
    contain_ini="*"
    
    contain_ini=""
    
    for i in range(n):
        contain_ini+="*"
    print (contain_ini)
    
    contain_med="*"
    
    for i in range(n-2):
        contain_med+=" "
    contain_med+="*\n"
    
    letrao=  str(contain_med*(n-2)+contain_ini) 
    print (letrao)
    return letrao
 
letra_o(n)


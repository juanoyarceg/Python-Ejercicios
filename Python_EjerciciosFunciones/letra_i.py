n=5
def letra_i(n):  

    contain_ini=""
    
    for i in range(n):
        contain_ini+="*"
    print (contain_ini)
    
    contain_med=" " 
    
    for i in range(n-(n-1)):
        contain_med+=" "   
    contain_med+="*\n"
    
 
    letrai=str(contain_med*(n-2)+contain_ini)  
    print (letrai) 
    return letrai        

letra_i(n)


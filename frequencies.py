"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in items:
        k = str(i)
        if not frequencies:
            frequencies[k]=1
        else:
            if k in frequencies.keys():
                frequencies[k]+=1
            else:
                frequencies[k]=1

        
        
        
        
        #if isinstance(i, str):
            #x = 1
            #frequencies[i] = x
            
            #for j in frequencies:
            #    if  

    # Your code goes here
    return frequencies
    #def __main__():

#input =['0', 4,4,'4','d','d','e',0,'a','d','4']
#frequencies(input)
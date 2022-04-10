def wordtracker(filename):
    wds=[]
    count={}
    hand=open(filename)
    for lin in hand:
        lin=lin.strip()
        wds=lin.split()
    #print(wds)
    
    for word in wds:
        count[word]=count.get(word,0)+1 
        
    #print(count)
    newtup=count.items()
    #print(newtup)
    temp=[]
    for k,v in newtup:
        temp.append((v,k))
        
    #print(temp)
    temp=sorted(temp,reverse=True)
    #print(temp)
    for v,k in temp[:5]:
        print(k," ", v)
    
    
if __name__=="__main__":
    print("Hello! We'll help you track your words.")
    filename=input("Please enter your file:")
    print("MAX   frequency")
    wordtracker(filename)
    
        
    

def count(n):
    count=0
    for i in range(n+1):      
        value=str(i).count('7')
        count=count+value
    print ("count:",count)

count(100)
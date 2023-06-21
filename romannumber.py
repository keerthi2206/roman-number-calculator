decimal = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
symbol = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
roman = ""

num = int(input('enter a number: '))

for d in decimal:
    
    q = num//d
    
    idx = decimal.index(d)
    
    x = symbol[idx]*q
    roman = roman + x 

    num = num%d

print(roman)




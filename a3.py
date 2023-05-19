#import termcolor
def C (text,color):
    return text

while True :
#    C = termcolor.colored
    a = float(input ("ghad be meter:  "))
    b = float(input ("vaznbe kg:  "))
    c = a ** 2
    d = round( b / c , 2)
    e = 18.5
    f = 25
    hhh = 24
    k1 = 19.5
    if d > f:
        ho = c * hhh
        ll = b - ho 
        print("shakhes a.b.m shoma:" , C(str(d),'red'))
        print("vazn shoma " +C("zeead",'red') +" ast!")
        print("vazn normal shoma:  " , ho )
        print("ezafeh vazneh shoma:  " , ll )

    elif d < e:
        a2 = c * k1
        ii = a2 - b
        print("shakhes a.b.m shoma: " , C(str(d), 'blue'))
        print("vazn shoma "+C("kam",'blue')+" ast! ")
        print("vazn normal shoma:  " , a2 )
        print("kamboodeh shoma: ", ii )

    else:
        print("shakhes a.b.m shoma:" , C(str(d),'green' ))
        print("vazn shoma "+C("normal",'green')+" ast!")
    
    input('\n\n press '+C('Enter','yellow'))
    print ('\n'*25)

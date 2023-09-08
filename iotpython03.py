#Function 3 : Have Parameter/Have returns ***
def funcA( ) :
    print('AAA')
    print('BBB')
    return 'Wow Wow Wow'

def funcB( ) :
    return 999, True, 10+20

# funcA( ) เขียนได้ แต่เขาไม่ทำกัน
print ( funcA( ) )
x = funcA( )

a, b, c = funcB( ) #***
print(f'{a} {b} {c}')
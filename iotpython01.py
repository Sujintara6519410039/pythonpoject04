#Function 1 : No Parameter/No Return
def funcA( ) :
    print('wow')
    print('woo')
    print('wee')
    print('wea')
    funcB( )
    #ไม่มีคำสั่ง return

def funcB( ) :
    print('Hi') 
    # funcA( ) ทำได้แต่ไม่ควรทำ

funcA( )   
funcA( ) 
funcB( )
funcA( )
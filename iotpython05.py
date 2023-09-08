# หาพื้นที่สีเหลี่ยม และสามเหลียม โดยรับกว้าง ยาว/ฐาน สูง ท่งแป้นพิมพ์ และแสดงผลทางหน้าจอ
# feature การทำงานอะไรบ้าง
# 1. รับค่า กว้างยาว 2. รับค่า ฐาน สูง 
#3. คำนวณพท. สี่เหลี่ยม และแสดงพท.สี่เหลี่ยม 4. คำนวณพท. สามเหลี่ยมและแสดงพท.สามเหลี่ยม
def inputWitdhLong( ) :
    wi = float( input('ป้อนกว้าง : ') )
    lo = float( input('ป้อนยาว : ') )
    return wi, lo

def inputBaseHigh( ) :
    ba = float( input('ป้อนฐาน : ') )
    hi = float( input('ป้อนสูง : ') ) 
    return ba, hi

def calAndShowAreaSquare( wi, lo ) :
    area = wi * lo
    print(f'สี่เหลี่ยมกว้าง {wi} ยาว {lo} มีพื้นที่ {area}')

def calAndShowAreTrianble( ba, hi ) :
    area = ba * hi / 2
    print(f'สามเหลี่ยม {ba} สูง {hi} มีพื้นที่ {area}')


wi, lo = inputWitdhLong( )
calAndShowAreaSquare(wi, lo)
print('......................')
ba, hi = inputBaseHigh( )
calAndShowAreTrianble(ba, hi)
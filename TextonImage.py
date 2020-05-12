from PIL import Image,ImageFont,ImageDraw
import xlrd

path = "test.xlsx"         #import file.xlsx   

inputWorkBook= xlrd.open_workbook(path)
inputWorkSheet= inputWorkBook.sheet_by_index(0)

rows=inputWorkSheet.nrows
    #cols=inputWorkSheet.ncols              #for involving columns
names=[]
for i in range(0,rows):
    names.append(inputWorkSheet.cell_value(i,0))

for j in names:
    str1=j
    img= Image.open('Test.png')     #image file
    font= ImageFont.truetype("arial.ttf",45)
    width,height=font.getsize(str1)
    w=1350/2
    h=1100/2
    draw=ImageDraw.Draw(img)
    draw.text((w,h),str1,font=font,fill='#D4AF37')

    img.show()
    img.save('{}.png'.format(j))





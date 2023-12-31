from sketchpy import library
from sketchpy import canvas

print("""1.APJ Abdul Kalam
      2.Indian Flag
      3.Gojo
      4.BTS
      5.RDJ
      6.Tomholland
      7.Vijay
      8.Import YOUR own picture and sketch it
      """)
c=int(input("Enter your choice"))
if(c==1):
    obj = library.apj()
    obj.draw()
if(c==2):
    obj = library.flag()
    obj.draw()
if(c==3):
    obj = library.gojo()
    obj.draw()
if(c==4):
    obj = library.bts()
    obj.draw()
if(c==5):
    obj = library.rdj()
    obj.draw()
if(c==6):
    obj = library.tom_holland()
    obj.draw()
if(c==7):
    obj = library.vijay()
    obj.draw()
if(c==8):
    obj=canvas.sketch_from_image(input('File name'))
    obj.draw()
else:
    print('Invalid choice')

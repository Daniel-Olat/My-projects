import qrcode
from PIL import Image , ImageDraw
  
  
link_to_website = input("Enter website URL : ")

qrcode_filename = input ("Enter filename to be save as:")

qr = qrcode.QRCode (box_size= 20 , border= 5)
qr.add_data(link_to_website)
image = qr.make_image( fill_color = "black" , background = "white" )
image.save(qrcode_filename)


print(f"Image saved as {qrcode_filename}")
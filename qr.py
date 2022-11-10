import qrcode,os
from PIL import Image

qr = qrcode.make("www.superlife.ci")
qr.save("test.png")

os.system("test.png")
qrcode (
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data('www.superlife.ci')
qr.make(fit=True)
img = qr.make_image(fill_color="red" , back_color="gray") .convert("RGB")
logo_display = Image.open('11.jpg')
logo_display.thumbnail((60,60))

logo_pos= ((img.size[0]- logo_display.size[0])//2,(img.size[1] -logo_display.size[1])//(2) )#pour déplacer l'image sur le qr code

img.paste(logo_display,logo_pos)


img.save("test.png")

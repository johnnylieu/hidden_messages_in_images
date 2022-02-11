inImgPNG = 'dexterLab.png'
inImgJPG = 'dexterLab2.jpg'

outImgPNG = 'topSecret.png'
outImgJPG = 'topSecret2.jpg'

msg = 'Johnny is king'

from stegano import lsb

# we are hiding the text here
lsb.hide(inImgPNG, message=msg).save(outImgPNG)

# we are getting text from the image
message = lsb.reveal(outImgPNG)
print(f'Reveal message: {message}')
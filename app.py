from stegano import lsb

inImgJPG = "sample_secret.jpg"
outImgJPG = "sample_secret2.jpg"

msg = "Johnny is king"

lsb.hide(inImgJPG, message=msg).save(outImgJPG)
message = lsb.reveal(outImgJPG)

print(f"secret message: {message}")
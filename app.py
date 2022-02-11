from stegano import lsb

secret = lsb.hide("sample_secret.jpg", "Johnny is king")

secret.save("sample_secret.jpg")
lsb.reveal("sample_secret.jpg")
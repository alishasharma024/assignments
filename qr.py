import qrcode

qr = qrcode.QRCode(
    version=15,  # 15 means the version of the QR code; higher numbers create larger codes
    box_size=10,  # Size of each box in the QR code
    border=5  # Border size (minimum is 4)
)

data = "https://scriptedsnaps.wordpress.com/"  # URL to encode

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("qrtest.png")  # Save the QR code image to a file

import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpSbG9ZQnplcDFrUnFiZTlQWXFRN3d2@87.247.142.222:33345/?outline=1')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

print(img)
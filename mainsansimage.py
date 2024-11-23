import qrcode
from PIL import Image

# URL à encoder dans le QR code
data = "https://bdev.online/qr/truck"

# Créer le QR code avec la couleur violette
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Haute correction d'erreur
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Générer l'image du QR code en violet
qr_img = qr.make_image(fill_color='purple', back_color='white').convert('RGB')

# Enregistrer l'image finale sans logo
qr_img.save("qr_code_violet.png")

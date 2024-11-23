import qrcode
from PIL import Image

# URL à encoder dans le QR code
data = "https://bdev.online/qr/review"

# Créer le QR code avec la couleur violette
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Haute correction d'erreur pour supporter l'insertion du logo
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Générer l'image du QR code en violet
qr_img = qr.make_image(fill_color='purple', back_color='white').convert('RGB')

# Charger le logo
logo_path = "logo.png"  # Chemin du logo
logo = Image.open(logo_path)

# Redimensionner le logo
logo_size = (qr_img.size[0] // 4, qr_img.size[1] // 4)  # Adapter la taille du logo à environ 25% du QR code
logo = logo.resize(logo_size)

# Calculer la position pour centrer le logo
position = ((qr_img.size[0] - logo.size[0]) // 2, (qr_img.size[1] - logo.size[1]) // 2)
qr_img.paste(logo, position, mask=logo)

# Enregistrer l'image finale avec le logo intégré
qr_img.save("qr_code_violet_avec_logo.png")

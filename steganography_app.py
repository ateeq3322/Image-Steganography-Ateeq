from PIL import Image


def encode_image(cover_path, secret_path, output_path):
    cover = Image.open(cover_path).convert("RGB")
    secret = Image.open(secret_path).convert("RGB")
    secret = secret.resize(cover.size)
    
    encoded = cover.copy()
    cover_pixels = encoded.load()
    secret_pixels = secret.load()

    for i in range(encoded.width):
        for j in range(encoded.height):
            r1, g1, b1 = cover_pixels[i, j]
            r2, g2, b2 = secret_pixels[i, j]
            
            r = (r1 & 0b11111100) | (r2 >> 6)
            g = (g1 & 0b11111100) | (g2 >> 6)
            b = (b1 & 0b11111100) | (b2 >> 6)
            
            cover_pixels[i, j] = (r, g, b)

    encoded.save(output_path)
    print(f"Secret image hidden in {output_path}")

# Decode function
def decode_image(hidden_path, output_path):
    hidden = Image.open(hidden_path)
    hidden_pixels = hidden.load()
    
    decoded = Image.new("RGB", hidden.size)
    decoded_pixels = decoded.load()

    for i in range(hidden.width):
        for j in range(hidden.height):
            r, g, b = hidden_pixels[i, j]

            r = (r & 0b00000011) << 6
            g = (g & 0b00000011) << 6
            b = (b & 0b00000011) << 6

            decoded_pixels[i, j] = (r, g, b)

    decoded.save(output_path)
    print(f"Secret image extracted to {output_path}")


from PIL import Image

def encrypt_image(input_image_path, output_image_path, key):
    # Open the image
    image = Image.open(input_image_path)
    pixels = image.load()

    # Encrypt each pixel
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]

            # Apply the key to each color component
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            # Update the pixel with the new value
            pixels[i, j] = (r, g, b)

    # Save the encrypted image
    image.save(output_image_path)
    print(f"Image encrypted and saved as {output_image_path}")

def decrypt_image(input_image_path, output_image_path, key):
    # Open the encrypted image
    image = Image.open(input_image_path)
    pixels = image.load()

    # Decrypt each pixel
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]

            # Reverse the key operation to get the original color components
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            # Update the pixel with the original value
            pixels[i, j] = (r, g, b)

    # Save the decrypted image
    image.save(output_image_path)
    print(f"Image decrypted and saved as {output_image_path}")

def main():
    print("Image Encryption Tool")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    print("3. Exit")
    
    while True:
        choice = input("Choose an option: ")

        if choice == '1':
            input_image = input("Enter the path to the image to encrypt: ")
            output_image = input("Enter the path to save the encrypted image: ")
            key = int(input("Enter the encryption key (a number): "))
            encrypt_image(input_image, output_image, key)

        elif choice == '2':
            input_image = input("Enter the path to the image to decrypt: ")
            output_image = input("Enter the path to save the decrypted image: ")
            key = int(input("Enter the decryption key (a number): "))
            decrypt_image(input_image, output_image, key)

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()

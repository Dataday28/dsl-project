from cryptography.fernet import Fernet


class Crypt:
    
    def genkey(self, path):
        # Implementar la lógica para generar una clave de encriptación
        key = Fernet.generate_key()
        with open(f"{path}/clave.key", 'wb') as key_file:
            key_file.write(key)
            print(f"Generando clave de encriptación en: {path}")

    def cryptext(self, dst_path, path):
        # Implementar la lógica para cifrar un texto

        with open(dst_path, 'rb') as key_file:
            key = key_file.read()

        cipher_suite = Fernet(key)
        text = path.encode()
        ciphertext = cipher_suite.encrypt(text)

        print(f" \n Texto cifrado: {ciphertext} \n")

    def crypfile(self, dst_path, path):
        # Implementar la lógica para cifrar un archivo

        with open(dst_path, 'rb') as key_file:
            key = key_file.read()

        cipher = Fernet(key)
        
        with open(path, 'rb') as file:
            file_dat = file.read()

        ciphertext = cipher.encrypt(file_dat)

        with open(path + '.enc', 'wb') as file:
            file.write(ciphertext)
        
        print(f"\n Archivo Cifrado: {path} \n")

    def destext(self, dst_path, cryp):
        # Implementar la lógica para descifrar un texto

        with open(dst_path, 'rb') as key_file:
            key = key_file.read()

        cipher = Fernet(key)
        text = cipher.decrypt(cryp)

        print(f"\n Texto descifrado: {text.decode()} \n")

    def desfile(self, dst_path, path):
        # Implementar la lógica para descifrar un archivo

        with open(dst_path, 'rb') as key_file:
            key = key_file.read()

        cipher = Fernet(key)

        with open(path, 'rb') as file:
            file_dat = file.read()

        decrypted_text = cipher.decrypt(file_dat)

        with open(path, 'wb') as file:
            file.write(decrypted_text)
            
        print(f"\n Archivo descifrado: {path} \n")
from cryptography.fernet import Fernet


class Crypt:
    
    def genkey(self, path):
        # Implementar la lógica para generar una clave de encriptación
        try:
            key = Fernet.generate_key()
            with open(f"{path}/clave.key", 'wb') as key_file:
                key_file.write(key)
                print(f"\n Clave generada en: {path} \n")

        except Exception as ex:
            print(f"\n Error al generar la clave: {ex} \n No tiene permiso para crear el archivo\n")
    
    def cryptext(self, dst_path, path):
        # Implementar la lógica para cifrar un texto

        try:
            with open(dst_path, 'rb') as key_file:
                key = key_file.read()
        
        except Exception as ex:
            print(f"\n Error al abrir la clave: {ex} \n No tiene permiso para aceder al archivo  o no lo especifico en la ruta \n")

        cipher_suite = Fernet(key)

        try:
            text = path.encode()
            ciphertext = cipher_suite.encrypt(text)

            print(f" \n Texto cifrado: {ciphertext} \n")

        except Exception as ex:
            print(f"\n Error al crifrar el texto: {ex} \n")

    def crypfile(self, dst_path, path):
        # Implementar la lógica para cifrar un archivo

        try:
            with open(dst_path, 'rb') as key_file:
                key = key_file.read()
        
        except Exception as ex:
            print(f"\n Error al abrir la clave: {ex} \n No tiene permiso para aceder al archivo  o no lo especifico en la ruta \n")

        cipher = Fernet(key)
        
        try:
            with open(path, 'rb') as file:
                file_dat = file.read()

        except Exception as ex:
            print(f"\n Error al abrir el archivo: {ex} \n No tiene permiso para aceder al archivo o no lo especifico en la ruta \n")

        ciphertext = cipher.encrypt(file_dat)

        with open(path, 'wb') as file:
            file.write(ciphertext)
        
        print(f"\n Archivo Cifrado: {path} \n")

    def destext(self, dst_path, cryp):
        # Implementar la lógica para descifrar un texto

        try:
            with open(dst_path, 'rb') as key_file:
                key = key_file.read()
        
        except Exception as ex:
            print(f"\n Error al abrir la clave: {ex} \n No tiene permiso para aceder al archivo  o no lo especifico en la ruta \n")

        cipher = Fernet(key)
        text = cipher.decrypt(cryp)

        print(f"\n Texto descifrado: {text.decode()} \n")

    def desfile(self, dst_path, path):
        # Implementar la lógica para descifrar un archivo
        try:
            with open(dst_path, 'rb') as key_file:
                key = key_file.read()
        
        except Exception as ex:
            print(f"\n Error al abrir la clave: {ex} \n No tiene permiso para aceder al archivo  o no lo especifico en la ruta \n")

        cipher = Fernet(key)

        try: 
            with open(path, 'rb') as file:
                file_dat = file.read()

        except Exception as ex:
            print(f"\n Error al abrir el archivo: {ex} \n No tiene permiso para aceder al archivo o no lo especifico en la ruta \n")

        decrypted_text = cipher.decrypt(file_dat)

        with open(path, 'wb') as file:
            file.write(decrypted_text)
            
        print(f"\n Archivo descifrado: {path} \n")
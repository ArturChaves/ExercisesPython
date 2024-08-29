def cipher(arg, encode):
    encoded = []
    for letter in arg:
        if letter.isalpha():  # Precisamos ver se é uma letra, porque para cifrar ser eficiente não podemos considerar outros caracteres
            start = ord('a') if letter.islower() else ord('A')
            # Desloca o caractere dentro do alfabeto, ou seja o start é subtraido para conseguir pegar o valor dentro do alfabeto do char sendo codificado, e o % 26 garante o range do alfabeto
            encoded.append(chr(start + (ord(letter) - start + encode) % 26))
        else:
            encoded.append(letter)  # Caso não seja uma letra o alg simplesmente da um append nesse char não alpha
    return ''.join(encoded)

def decode(arg, encode):
    return cipher(arg, -encode)

texto_original = "Hi Baby! I love U."
texto_cifrado = cipher(texto_original, 2)
print(f"Texto cifrado: {texto_cifrado}")

texto_decodificado = decode(texto_cifrado, 2)
print(f"Texto decodificado: {texto_decodificado}")

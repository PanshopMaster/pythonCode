class TraductorGirigoncio:
    def __init__(self, texto):
        self.texto = texto

    def modificar_texto(self):
        # la lógica para modificar el texto
        s1 = self.texto.replace('a', 'apa')
        s2 = s1.replace('e', 'epe')
        s3 = s2.replace('i', 'ipi')
        s4 = s3.replace('o', 'opo')
        s5 = s4.replace('u', 'upu')
        return s5
    def enviar_text2(self):
        self.texto
        texto = "hola porciaca"
        return texto

input_text = input("Introduce un texto: ")
traductor = TraductorGirigoncio(input_text)
texto_modificado = traductor.modificar_texto()
texto2 = traductor.enviar_text2()
print(texto_modificado)
print(texto2)
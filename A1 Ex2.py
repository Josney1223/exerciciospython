def letras_favoritas(letra, frase):
    print ("Sua letra favorita:", letra)
    print ("Uma frase importante:", frase)
    n = frase.count(letra)
    print ("Sua letra favorita é a letra", letra, "e ela aparece", n, "vezes na frase", frase)

letras_favoritas("a", "banana")

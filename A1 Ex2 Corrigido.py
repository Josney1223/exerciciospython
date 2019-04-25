def letras_favoritas(letra, frase):
    print ("Sua letra favorita:", letra)
    print ("Uma frase importante:", frase)
    
    if (letra.islower()):
        j = frase.count(letra)
        k = frase.count(letra.upper())
    else:
        j = frase.count(letra)
        k = frase.count(letra.lower())
        
    n = j + k
    print ("Sua letra favorita é a letra", letra, "e ela aparece", n, "vezes na frase", frase)

letras_favoritas("A", "bAnana")

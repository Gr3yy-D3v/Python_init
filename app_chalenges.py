coordenada_x = int(input("me diga um numero onde está X "))
coordenada_Y = int(input("me diga um numero onde está Y "))

if coordenada_x and coordenada_Y > 0:
    print("Você está no primeiro quadrante")
elif coordenada_x < 0 and coordenada_Y > 0:
    print("Você está no segundo quadrante")
elif coordenada_x and coordenada_Y < 0:
    print("Você está no terceiro quadrante")
elif coordenada_x > 0 and coordenada_Y < 0:
    print("Você está no quarto quadrante")
else:
    print("Você está no ponto de origem")
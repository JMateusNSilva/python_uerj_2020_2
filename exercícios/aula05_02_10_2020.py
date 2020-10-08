# EXERCÍCIO 01 - [NAO É POSSÍVEL FAZER NO COLAB] - 
import turtle

cor = input('Escolha uma das cores para sua linha: white, yellow, orange, red, green, blue, purple, gray, black. ')

wn = turtle.Screen()  # Manda abrir a janela do turtle
mateus = turtle.Turtle()


mateus.color(cor)
mateus.forward(150)
mateus.left(90)
mateus.forward(130)

wn.mainloop()          # Espere o usuário fechar a janela do turtle


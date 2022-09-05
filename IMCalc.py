#!/usr/bin/python3

# Calculadora de IMC, por Felipe Miguel Nery Lunkes

from tkinter import *

class IMCalc:

    def __init__(self, win):

        self.lbl1=Label(win, text='Digite sua altura (cm):')
        self.lbl2=Label(win, text='Digite seu peso (kg):')
        self.lbl3=Label(win, text='Seu IMC:')

        self.lbl1.place(x=50, y=50)
        self.lbl2.place(x=50, y=100)
        self.lbl3.place(x=50, y=200)

        self.texto1=Entry(bd=3)
        self.texto1.place(x=200, y=50)
        self.texto2=Entry()
        self.texto2.place(x=200, y=100)
        self.texto3=Entry()
        self.texto3.place(x=200, y=200)

        self.botao1=Button(win, text='Pronto!', command=self.pronto)
        self.botao1.place(x=200, y=150)

    def pronto(self):

        self.texto3.delete(0, 'end')

        altura=int(self.texto1.get())
        peso=int(self.texto2.get())

# Precisamos converter a altura em centímetros para metros na conta

        resultado=peso/((altura/100)*(altura/100))

        self.texto3.insert(END, str(resultado))

        if float(resultado) <= 17:
            classificacao="Muito abaixo do peso"
        elif float(resultado) >= 17 and float(resultado) < 18.49:
            classificacao="Abaixo do peso"
        elif float(resultado) >= 18.50 and float(resultado) < 24.99:
            classificacao="Peso normal"
        elif float(resultado) >= 25 and float(resultado) <= 29.99:
            classificacao="Acima do peso"
        elif float(resultado) >= 30 and float(resultado) <= 34.99:
            classificacao="Obesidade grau I"
        elif float(resultado) >= 35 and float(resultado) <= 39.99:
            classificacao="Obesidade grau II (severa)"
        elif float(resultado) >= 40:
            classificacao="Obesidade III (mórbida)"
        else:
            classificacao="Desconhecida"

        lblCalssificacao=Label(janela, text='Classificação:')
        lblCalssificacao.place(x=50, y=250)
        classific=Entry()
        classific.place(x=150, y=250)
        classific.insert(END, str(classificacao))

janela=Tk()
imcalc=IMCalc(janela)
janela.title('IMCalc por Felipe Lunkes')
janela.geometry("400x300+10+10")
janela.mainloop()
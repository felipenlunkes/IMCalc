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

janela=Tk()
imcalc=IMCalc(janela)
janela.title('IMCalc por Felipe Lunkes')
janela.geometry("400x300+10+10")
janela.mainloop()
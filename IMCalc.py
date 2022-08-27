from tkinter import *

class IMCalc:

    def __init__(self, win):

        self.lbl1=Label(win, text='Digite sua altura (cm):')
        self.lbl2=Label(win, text='Digite seu peso (kg):')
        self.lbl3=Label(win, text='Seu IMC:')

        self.lbl1.place(x=50, y=50)
        self.lbl2.place(x=50, y=100)
        self.lbl3.place(x=50, y=200)

        self.t1=Entry(bd=3)
        self.t1.place(x=200, y=50)
        self.t2=Entry()
        self.t2.place(x=200, y=100)
        self.t3=Entry()
        self.t3.place(x=200, y=200)

        self.b1=Button(win, text='Pronto!', command=self.pronto)
        self.b1.place(x=200, y=150)

    def pronto(self):

        self.t3.delete(0, 'end')

        altura=int(self.t1.get())
        peso=int(self.t2.get())

# Precisamos converter a altura em centímetros para metros na conta

        resultado=peso/((altura/100)*(altura/100))

        self.t3.insert(END, str(resultado))

janela=Tk()
imcalc=IMCalc(janela)
janela.title('IMCalc')
janela.geometry("400x300+10+10")
janela.mainloop()
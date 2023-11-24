import tkinter as tk

class Calculadora(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.crear_widgets()

    def sumar(self):
        self.resultado["text"] = float(self.num1.get()) + float(self.num2.get())

    def restar(self):
        self.resultado["text"] = float(self.num1.get()) - float(self.num2.get())

    def multiplicar(self):
        self.resultado["text"] = float(self.num1.get()) * float(self.num2.get())

    def dividir(self):
        if float(self.num2.get()) != 0:
            self.resultado["text"] = float(self.num1.get()) / float(self.num2.get())
        else:
            self.resultado["text"] = "No se puede dividir entre cero."

    def crear_widgets(self):
        self.num1 = tk.Entry(self)
        self.num1.pack(side="left")

        self.num2 = tk.Entry(self)
        self.num2.pack(side="left")

        self.suma = tk.Button(self)
        self.suma["text"] = "+"
        self.suma["command"] = self.sumar
        self.suma.pack(side="left")

        self.resta = tk.Button(self)
        self.resta["text"] = "-"
        self.resta["command"] = self.restar
        self.resta.pack(side="left")

        self.multiplicacion = tk.Button(self)
        self.multiplicacion["text"] = "*"
        self.multiplicacion["command"] = self.multiplicar
        self.multiplicacion.pack(side="left")

        self.division = tk.Button(self)
        self.division["text"] = "/"
        self.division["command"] = self.dividir
        self.division.pack(side="left")

        self.resultado = tk.Label(self)
        self.resultado["text"] = "Resultado"
        self.resultado.pack(side="left")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                                command=self.master.destroy)
        self.quit.pack(side="bottom")

root = tk.Tk()
app = Calculadora(master=root)
app.mainloop()

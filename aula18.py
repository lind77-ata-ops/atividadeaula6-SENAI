import tkinter as tk




def display():
    texto   = input_t.get()
    mostrar_label.config(text=texto)

janela  =  tk.Tk()
janela.title('teste')


janela.geometry('500x500')


texto =  tk.Label(janela, text = 'Hello',fg='green', bg='yellow', font=('arial', 25))
texto.pack()


input_t =  tk.Entry(janela, font=('arial', 20))
input_t.pack()


b_t = tk.Button(janela, text = 'clique aqui', font=('arial', 20), command=display)
b_t.pack()



mostrar_label  = tk.Label(janela, text = 'mostrar',fg='green', bg='yellow', font=('arial', 25))
mostrar_label.pack()  


janela.mainloop()
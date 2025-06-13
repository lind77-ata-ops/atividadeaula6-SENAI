import tkinter as tk


janela  =  tk.Tk()
janela.title('teste')


janela.geometry('500x500')


texto =  tk.Label(janela, text = 'Hello',fg='green', bg='yellow')
texto.pack()


input_t =  tk.Entry(janela)
input_t.pack()


b_t = tk.Button(janela, text = 'clique aqui')
b_t.pack()



janela.mainloop()
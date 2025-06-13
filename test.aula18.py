import tkinter as tk



def display():
    nome = nome_digitado.get()
    idade = idade_digitada.get()
    MOSTRAR_NOME.config(text=nome)
    MOSTRAR_IDADE.config(text=idade)



janela  =  tk.Tk()
janela.title('SISTEMA DE CADASTRO ')

janela.geometry('500x500')

titulo_pag = tk.Label(janela,text = 'Cadastro de usuários', font=('arial',20))
titulo_pag.grid(row=0,column=0, padx=15, pady=10)


nome_ =  tk.Label(janela, text = 'NOME', bg='yellow', font=('arial',10))
nome_.grid(row=1, column=0, pady=5)

nome_digitado =  tk.Entry(janela, font=('arial', 10))
nome_digitado.grid(row=1, column=1, padx=5, pady=5)


texto =  tk.Label(janela, text = 'IDADE', bg='yellow', font=('arial',10))
texto.grid(row=2, column=0, pady=5)

idade_digitada =  tk.Entry(janela, font=('arial', 10))
idade_digitada.grid(row=2, column=1, padx=5, pady=5)



b_t = tk.Button(janela, text = 'clique aqui', font=('arial', 15), command=display)
b_t.grid(row=3, column=0, padx=5, pady=5)

MOSTRAR_NOME = tk.Label(janela, text = ' MOSTRAR NOME',  font=('arial', 15))
MOSTRAR_NOME.grid(row=5, column=0, padx=5, pady=5)

MOSTRAR_IDADE = tk.Label(janela, text = 'MOSTRAR IDADE', font=('arial', 15))
MOSTRAR_IDADE.grid(row=6, column=0, padx=5, pady=5)

janela.mainloop()
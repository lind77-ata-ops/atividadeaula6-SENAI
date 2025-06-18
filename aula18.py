
import tkinter as tk


def display():
    nome = nome_entry.get()
    idade = idade_entry.get()
    endereco = endereco_entry.get()
    email = E_mail_entry.get()
    celular = celular_entry.get()
    MOSTRAR_NOME.configure(text=nome)
    MOSTRAR_IDADE.configure(text=idade)
    MOSTRAR_EMAIL.configure(text=email)
    MOSTRAR_ENDERECO.configure(text=endereco)
    MOSTRAR_CELULAR.configure(text =celular)
    

root = tk.Tk()
root.geometry('2200x1700')
root.configure(bg='Aquamarine')

tk.Label(root, text='FORMULÁRIO ', font=('Courier New', 28)).grid(row=0, column=0, pady=30, padx=20)


nome_label = tk.Label(root, text='Nome ', font=('Courier New', 28))
nome_label.grid(row=1, column=1, pady=10, padx=20)

nome_entry = tk.Entry(root, font=('', 28))
nome_entry.grid(row=1, column=3, pady=10, padx=20)

idade_label = tk.Label(root, text='Idade ', font=('Courier New', 28))
idade_label.grid(row=2, column=1, pady=10, padx=20)

idade_entry = tk.Entry(root, font=('', 28))
idade_entry.grid(row=2, column=3, pady=10, padx=20)

E_mail_label = tk.Label(root, text='E_mail ', font=('Courier New', 28))
E_mail_label.grid(row=3, column=1, pady=10, padx=20)

E_mail_entry = tk.Entry(root, font=('', 28))
E_mail_entry.grid(row=3, column=3, pady=10, padx=20)


endereco = tk.Label(root, text='Endereço', font=('Courier New', 28))
endereco.grid(row=4, column=1, pady=10, padx=20)

endereco_entry = tk.Entry(root, font=('', 28))
endereco_entry.grid(row=4, column=3, pady=10, padx=20)


celular = tk.Label(root, text='Celular', font=('Courier New', 28))
celular.grid(row=5, column=1, pady=10, padx=20)

celular_entry = tk.Entry(root, font=('', 28))
celular_entry.grid(row=5, column=3, pady=10, padx=20)


btn = tk.Button(root, text='enviar',font=('Courier New', 28), borderwidth=10, command=display)
btn.grid(row=6, column=3, pady=20, padx=20)

MOSTRAR_NOME = tk.Label(root, text='', font=('', 28))
MOSTRAR_NOME.grid(row=7, column=3, pady=20, padx=25)

MOSTRAR_IDADE = tk.Label(root, text='', font=('', 28))
MOSTRAR_IDADE.grid(row=8, column=3, pady=20, padx=25)

MOSTRAR_ENDERECO = tk.Label(root, text='', font=('', 28))
MOSTRAR_ENDERECO.grid(row=9, column=3, pady=20, padx=25)

MOSTRAR_EMAIL = tk.Label(root, text='', font=('', 28))
MOSTRAR_EMAIL.grid(row=10, column=3, pady=20, padx=25)

MOSTRAR_CELULAR = tk.Label(root, text='', font=('', 28))
MOSTRAR_CELULAR.grid(row=11, column=3, pady=20, padx=25)





root.mainloop()

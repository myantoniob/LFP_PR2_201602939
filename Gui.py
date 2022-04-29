from tkinter import *

from setuptools import Command

# Marco
root = Tk()
root.geometry("700x550")
root.resizable(width=False, height=False)

# Main Marco
main_label = LabelFrame(root, width=700, height=550 , padx=20, pady=20)
main_label.grid_propagate(0)
main_label.grid(row=0, column=0)


# Input box

#  ---------------  mid  -------------------
mid_frame = LabelFrame(main_label, width=55, height=500)
mid_frame.place(x=10, y=10)

# Text
scroll_b = Scrollbar(mid_frame)
scroll_b.pack(side=RIGHT, fill=Y)


text = Text(mid_frame, width=55, height=26, yscrollcommand=scroll_b.set)
text.pack()

scroll_b.config(command=text.yview)


# Input 

request = Entry(main_label, width=75, borderwidth=5)
request.place(x=10, y=465)


# load_chat
mensaje = []
mensaje = ['"Bienvenido a La Liga Bot. Ingrese un comando "\n']
def load_chat():
    text.delete('1.0', END)
    mensaje.append(f'"{request.get()} "\n')
    for men in mensaje:
        text.insert(END, men) 





# Botones

b_reporte_errores = Button(main_label, text="  Reporte de errores   ", padx=13, pady=5)
b_reporte_errores.place(x=500, y=10)

b_limpiar_errores = Button(main_label, text="Limpiar log de errores", padx=13, pady=5)
b_limpiar_errores.place(x=500, y=55)

b_reporte_tokens = Button(main_label,  text="   Reporte de tokens   ", padx=13, pady=5)
b_reporte_tokens.place(x=500, y=95)

b_limpiar_tokens = Button(main_label,  text="Limpiar log de tokens ", padx=13, pady=5)
b_limpiar_tokens.place(x=500, y=135)

b_manual_usuario = Button(main_label,  text="  Manual de usuario    ", padx=13, pady=5)
b_manual_usuario.place(x=500, y=175)

b_manual_tecnico = Button(main_label,  text="   Manual tecnico       ", padx=13, pady=5)
b_manual_tecnico.place(x=500, y=215)

b_enviar = Button(main_label, text='          Enviar          ', padx=13, pady=5 , command= load_chat)
b_enviar.place(x=500, y=465)

root.mainloop()
from tkinter import *
import parser

#Abrindo a janela, dando um nome e inicializando seu tamanho
cal = Tk()
cal.title('Calculadora')
cal.geometry('245x365')

# Criando um quadro para colocar o campo de entrada
input_frame = Frame(cal, width = 2, height = 3, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_frame.grid()


# Criando a campo de entrada propriamente dito
display = Entry(input_frame, font = ('times', 18, 'normal'), width = 19, borderwidth= 5, justify= RIGHT)
display.grid(row = 0, column = 0, columnspan= 3, padx= 1, pady= 1)

i=0


#FUNÇÕES===========================================================
#Pegando números inseridos
def get_numbers(n):
    global i
    display.insert(i, n)
    i+=1


#Pegando operação inserida
def get_operation(operator):
    global i
    operator_lenght = len(operator)
    display.insert(i, operator)
    i+=operator_lenght


#Limpa o display
def clear_display():
    display.delete(0, END)


#Corrige o código inserido
def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear_display()
        display.insert(0, 'Erro')


#Fazendo o cálculo da operação
def calculate():
    display_state = display.get()
    try:
        math_expression = parser.expr(display_state).compile()
        result = eval(math_expression)
        clear_display()
        display.insert(0, result)
    except math_expression as identifier:
        clear_display()
        display.insert(0, 'Erro')
#==================================================================================


#Botões Numéricos
#Criando quadros onde ficarão os botões
btns_frame = Frame(cal, width = 320, height = 272.5)
btns_frame.grid()

btn_1 = Button(btns_frame, text="1", command=lambda: get_numbers(1), padx=20, pady=20).grid(row=5, column=0, sticky=W+E)
btn_2 = Button(btns_frame, text="2", command=lambda: get_numbers(2), padx=20, pady=20).grid(row=5, column=1, sticky=W+E)
btn_3 = Button(btns_frame, text="3", command=lambda: get_numbers(3), padx=20, pady=20).grid(row=5, column=2, sticky=W+E)

btn_4 = Button(btns_frame, text="4", command=lambda: get_numbers(4), padx=20, pady=20).grid(row=4, column=0, sticky=W+E)
btn_5 = Button(btns_frame, text="5", command=lambda: get_numbers(5), padx=20, pady=20).grid(row=4, column=1, sticky=W+E)
btn_6 = Button(btns_frame, text="6", command=lambda: get_numbers(6), padx=20, pady=20).grid(row=4, column=2, sticky=W+E)

btn_7 = Button(btns_frame, text="7", command=lambda: get_numbers(7), padx=20, pady=20).grid(row=3, column=0, sticky=W+E)
btn_8 = Button(btns_frame, text="8", command=lambda: get_numbers(8), padx=20, pady=20).grid(row=3, column=1, sticky=W+E)
btn_9 = Button(btns_frame, text="9", command=lambda: get_numbers(9), padx=20, pady=20).grid(row=3, column=2, sticky=W+E)
btn_0 = Button(btns_frame, text="0", command=lambda: get_numbers(0), padx=20, pady=20).grid(row=6, column=1, sticky=W+E)

#Botões De Cálculo

btn_clear = Button(btns_frame, text="C", command=lambda: clear_display(), padx=20, pady=20).grid(row=2, column=0, sticky=W+E)
btn_pow = Button(btns_frame, text="x²", command=lambda: get_operation("**2"), padx=20, pady=20).grid(row=2, column=1, sticky=W+E)
btn_porcentagem = Button(btns_frame, text="%", command=lambda: get_operation("%"), padx=20, pady=20).grid(row=2, column=2, sticky=W+E)
btn_undo = Button(btns_frame, text="⌫", command=lambda: undo(), padx=20, pady=20).grid(row=2, column=3, sticky=W+E)
btn_div = Button(btns_frame, text="/", command=lambda: get_operation("/"), padx=20, pady=20).grid(row=3, column=3, sticky=W+E)
btn_mult = Button(btns_frame, text="*", command=lambda: get_operation("*"), padx=20, pady=20).grid(row=4, column=3, sticky=W+E)
btn_minus = Button(btns_frame, text="-", command=lambda: get_operation("-"), padx=20, pady=20).grid(row=5, column=3, sticky=W+E)
btn_plus = Button(btns_frame, text="+", command=lambda: get_operation("+"), padx=20, pady=20).grid(row=6, column=3, sticky=W+E)
btn_equal = Button(btns_frame, text="=", command=lambda: calculate(), padx=20, pady=20).grid(row=6, column=2, sticky=W+E)
btn_decimal = Button(btns_frame, text=".", command=lambda: get_operation("."), padx=20, pady=20).grid(row=6, column=0, sticky=W+E)

cal.mainloop()

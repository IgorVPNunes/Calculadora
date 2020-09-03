from tkinter import *
import parser

cal = Tk()
cal.title('Calculadora')
cal.geometry('230x340')
dispay = Entry(cal)
dispay.grid(row=1, columnspan=10, sticky=W+E)

i=0

def get_nubers(n):
    global i
    dispay.insert(i, n)
    i+=1

def get_operation(operator):
    global i
    operator_lenght = len(operator)
    dispay.insert(i, operator)
    i+=operator_lenght

def clear_display():
    dispay.delete(0, END)

def undo():
    dispay_state = dispay.get()
    if len(dispay_state):
        dispay_new_state = dispay_state[:-1]
        clear_display()
        dispay.insert(0, dispay_new_state)
    else:
        clear_display()
        dispay.insert(0, 'Erro')

def calculate():
    dispay_state = dispay.get()
    try:
        math_expression = parser.expr(dispay_state).compile()
        result = eval(math_expression)
        clear_display()
        dispay.insert(0, result)
    except math_expression as identifier:
        clear_display()
        dispay.insert(0, 'Erro')


#Botões Numéricos

Button(cal, text="1", command=lambda: get_nubers(1), padx=20, pady=20).grid(row=5, column=0, sticky=W+E)
Button(cal, text="2", command=lambda: get_nubers(2), padx=20, pady=20).grid(row=5, column=1, sticky=W+E)
Button(cal, text="3", command=lambda: get_nubers(3), padx=20, pady=20).grid(row=5, column=2, sticky=W+E)
Button(cal, text="4", command=lambda: get_nubers(4), padx=20, pady=20).grid(row=4, column=0, sticky=W+E)
Button(cal, text="5", command=lambda: get_nubers(5), padx=20, pady=20).grid(row=4, column=1, sticky=W+E)
Button(cal, text="6", command=lambda: get_nubers(6), padx=20, pady=20).grid(row=4, column=2, sticky=W+E)
Button(cal, text="7", command=lambda: get_nubers(7), padx=20, pady=20).grid(row=3, column=0, sticky=W+E)
Button(cal, text="8", command=lambda: get_nubers(8), padx=20, pady=20).grid(row=3, column=1, sticky=W+E)
Button(cal, text="9", command=lambda: get_nubers(9), padx=20, pady=20).grid(row=3, column=2, sticky=W+E)
Button(cal, text="0", command=lambda: get_nubers(0), padx=20, pady=20).grid(row=6, column=1, sticky=W+E)

#Botões De Cálculo

Button(cal, text="C", command=lambda: clear_display(), padx=20, pady=20).grid(row=2, column=0, sticky=W+E)
Button(cal, text="^2", command=lambda: get_operation("**2"), padx=20, pady=20).grid(row=2, column=1, sticky=W+E)
Button(cal, text="%", command=lambda: get_operation("%"), padx=20, pady=20).grid(row=2, column=2, sticky=W+E)
Button(cal, text="⌫", command=lambda: undo(), padx=20, pady=20).grid(row=2, column=3, sticky=W+E)
Button(cal, text="/", command=lambda: get_operation("/"), padx=20, pady=20).grid(row=3, column=3, sticky=W+E)
Button(cal, text="*", command=lambda: get_operation("*"), padx=20, pady=20).grid(row=4, column=3, sticky=W+E)
Button(cal, text="-", command=lambda: get_operation("-"), padx=20, pady=20).grid(row=5, column=3, sticky=W+E)
Button(cal, text="+", command=lambda: get_operation("+"), padx=20, pady=20).grid(row=6, column=3, sticky=W+E)
Button(cal, text="=", command=lambda: calculate(), padx=20, pady=20).grid(row=6, column=2, sticky=W+E)
Button(cal, text=".", command=lambda: get_operation("."), padx=20, pady=20).grid(row=6, column=0, sticky=W+E)

cal.mainloop()

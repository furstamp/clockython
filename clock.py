# Importando Packages

from tkinter import Label, Tk # Package de Interface Gráfica ( Janelas )
import time # Package de Tempo


# Configurando Título e Dimensão

app_window = Tk()
app_window.title("Relógio Virtual") # Título da Janela
app_window.geometry("420x150") # Dimensões do Tamanho da Janela
app_window.resizable(False, False) # Tornando Impossível de Redimensionar a Janela

# Configurando Aparência ( Fontes | Backgrounds )

text_font= ("Boulder", 68, 'bold')  # Nome da Fonte | Tamanho da Fonte | Tipo de Fonte
background = "#11161f" # Cor do Fundo
foreground = "#ffffff" # Cor da Fonte
border_width = 25

# Configurando Labels

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

# Configurando o Horário

def digital_clock():
    time_live = time.strftime("%H:%M:%S") # Hora | Minuto | Segundo
    label.config(text=time_live)
    label.after(200, digital_clock)

# Mantendo Janela em Loop

digital_clock()
app_window.mainloop()

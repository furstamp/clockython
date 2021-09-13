# Relógio Virtual em Python com GUI

## Descrição

Projeto feito em Python. Um relógio virtual simples com Interface Gráfica (GUI), mostrando e atualizando em tempo real o horário atual.

## Imagem Abaixo de Exemplo

<img align="center" src="screenshot/printclock1.png">

<p align="center"><b>Exemplo da Janela</b></p>

## Info das Packages Importadas

~~~py
from tkinter import Label, Tk
import time
~~~

Tkinter é um Module ou Package para o Python. Módulo para criação de aplicativos com Interface Gráfica, sendo possível assim utilizar Botões, Cores, Dimensões, entre outros.
Para saber mais, entre no Link de Info do próprio site oficial do Python.

~~~
https://docs.python.org/3/library/tkinter.html
~~~

Time é um Package nativo do Python, tal usado para tempos e horários.

## Configurações da Janela

Alterar o título da Janela ->

~~~py
app_window.title("Nome da Janela")
~~~

Alterar as dimensões da Janela ->

~~~py
app_window.geometry("420x150")
~~~

Configurar o fundo da Janela ->

~~~py
background = "#11161f"
~~~

Configurar a cor da Fonte ->

~~~py
foreground = "#ffffff"
~~~

Configurar se é possível redimensionar a Janela com mouse ou não ->

~~~py
app_window.resizable(False, False)
~~~

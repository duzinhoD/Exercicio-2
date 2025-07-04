# Importa o módulo tkinter para criar interfaces gráficas
import tkinter as tk
# Importa o módulo de mensagens do tkinter (caixas de alerta)
from tkinter import messagebox
# Importa todas as funções do arquivo Backend.py
import Backend

# Função para atualizar a lista exibida com todos os contatos
def atualizar_lista():
    lista_contatos.delete(0, tk.END)  # Limpa a lista atual
    for contato in Backend.listar_contatos():  # Para cada contato no banco
        lista_contatos.insert(tk.END, contato)  # Insere na interface

# Função para adicionar um novo contato
def adicionar():
    # Obtém os valores digitados nos campos de entrada
    nome = entrada_nome.get()
    telefone = entrada_telefone.get()
    endereco = entrada_endereco.get()
    cpf = entrada_cpf.get()
    # Verifica se nome e telefone foram preenchidos
    if nome and telefone:
        Backend.adicionar_contato(nome, telefone, endereco, cpf)
        atualizar_lista()  # Atualiza a lista exibida
        limpar_campos()    # Limpa os campos de entrada
    else:
        messagebox.showwarning("Atenção", "Nome e telefone são obrigatórios!")

# Função para buscar contatos pelo nome
def buscar():
    nome = entrada_nome.get()
    lista_contatos.delete(0, tk.END)  # Limpa a lista atual
    for contato in Backend.buscar_contato(nome):  # Busca por nome
        lista_contatos.insert(tk.END, contato)  # Exibe na lista

# Função para remover um contato selecionado na lista
def remover():
    try:
        # Obtém o contato selecionado
        selecao = lista_contatos.curselection()
        if selecao:
            item = lista_contatos.get(selecao)
            Backend.remover_contato(item[0])  # Remove pelo ID
            atualizar_lista()
        else:
            messagebox.showinfo("Info", "Nenhum contato selecionado.")
    except IndexError:
        messagebox.showerror("Erro", "Erro ao remover o contato.")

# Função para limpar todos os campos de entrada
def limpar_campos():
    entrada_nome.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)
    entrada_endereco.delete(0, tk.END)
    entrada_cpf.delete(0, tk.END)

# Cria a janela principal da interface
janela = tk.Tk()
janela.title("Agenda de Contatos")  # Define o título da janela

# Cria e posiciona os rótulos e campos de entrada
tk.Label(janela, text="Nome:").grid(row=0, column=0)
entrada_nome = tk.Entry(janela)
entrada_nome.grid(row=0, column=1)

tk.Label(janela, text="Telefone:").grid(row=1, column=0)
entrada_telefone = tk.Entry(janela)
entrada_telefone.grid(row=1, column=1)

tk.Label(janela, text="Endereço:").grid(row=2, column=0)
entrada_endereco = tk.Entry(janela)
entrada_endereco.grid(row=2, column=1)

tk.Label(janela, text="CPF:").grid(row=3, column=0)
entrada_cpf = tk.Entry(janela)
entrada_cpf.grid(row=3, column=1)

# Cria e posiciona os botões
tk.Button(janela, text="Adicionar", command=adicionar).grid(row=4, column=0)
tk.Button(janela, text="Buscar", command=buscar).grid(row=4, column=1)
tk.Button(janela, text="Remover", command=remover).grid(row=5, column=0)
tk.Button(janela, text="Limpar", command=limpar_campos).grid(row=5, column=1)

# Cria e posiciona a lista que exibe os contatos
lista_contatos = tk.Listbox(janela, width=50)
lista_contatos.grid(row=6, column=0, columnspan=2)

# Chama a função para mostrar todos os contatos ao abrir
atualizar_lista()
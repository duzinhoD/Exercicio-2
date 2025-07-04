# Importa o módulo Backend, que lida com o banco de dados
import Backend
# Importa o módulo Gui, que lida com a interface do usuário
import Gui

# Chama a função que cria a tabela no banco de dados (caso ainda não exista)
Backend.criar_tabela()

# Inicia a interface gráfica da aplicação
Gui.janela.mainloop()  # Mantém a janela aberta até que o usuário feche
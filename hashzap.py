
import flet as ft

def main(pagina):
    # criando elemento título, botão... e os demais
    titulo = ft.Text('hashzap')  # Correção: ft.Text('hashzap')

    # criando o popap, janelinha que abre para entrar no chat
    titulo_janela = ft.Text('Bem vindo ao hashzap')
    campo_nome_usuario = ft.TextField(label='Escreva seu nome no chat')

    # função para ativar o botão de enviar mensagem
    def enviar_mensagem(evento):
        botao_enviar_mensagen = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)

    # chat é uma coluna vazia
    chat = ft.Column()

    # criando túnel de comunicação
    def enviar_mensagem_tunel(mensagem):
        texto_chat = ft.Text(mensagem)
        chat.controls.append(texto_chat)
        pagina.update

    # cadastrando o túnel no site para todos os usuários ao mesmo tempo
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        texto_mensagem = campo_mensagem.value  # exibindo a mensagem e o nome do usuário
        nome_usuario = campo_nome_usuario.value
        mensagem = f'{nome_usuario}: {texto_mensagem}'
        pagina.pubsub.send_all(mensagem)  # trazendo o túnel para cá
        campo_mensagem.value = ''  # limpando o campo após enviar
        pagina.update()

    campo_mensagem = ft.TextField(label='Digite sua mensagem')
    botao_enviar_mensagen = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)

    # quero que meu campo de mensagem e meu botão fiquem um ao lado do outro
    linha_mensagem = ft.Row([campo_mensagem, botao_enviar_mensagen])

    # ao entrar no chat
    def entrar_chat(envento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False
        pagina.add(chat)
        pagina.add(linha_mensagem)
        mensagem = f'{campo_nome_usuario} entrou no chat'
        pagina.pubsub.send_all(mensagem)
        pagina.update()

    botao_entrar = ft.ElevatedButton('Entrar no chat', on_click=entrar_chat)

    # criando janela de alerta e colocando os elementos
    janela = ft.AlertDialog(title=titulo_janela, content=campo_nome_usuario, actions=[botao_entrar])  # actions para adicionar todas as ações

    # dando funcionalidade ao botão
    def iniciar_chat(evento):
        # quero que a janela da minha página seja essa janela que você criou aqui
        pagina.dialog = janela
        # padrão quando cria janela ela é fechada, então ponto open é para abrir
        janela.open = True  # Correção: janela.open = True
        # atualiza página
        pagina.update()

    botao_iniciar = ft.ElevatedButton('iniciar chat', on_click=iniciar_chat)

    # adicionando o elemento na página
    pagina.add(titulo)
    pagina.add(botao_iniciar)

# rodar o método
# rodar o método   
# ft.app(main)
ft.app(target=main, view=ft.WEB_BROWSER)
 #posso usar dest forma p definir como quero ver, a cima era apenas uma janela do mac, agora vizualizo com pg de web aba navegador

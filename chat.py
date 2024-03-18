import flet as ft

def main(page):
    text = ft.Text("Hashzap")

    chat = ft.Column()

    def send_message_tunnel(msg):
        print(msg)
        text_message = ft.Text(msg)
        chat.controls.append(text_message)
        page.update()

    page.pubsub.subscribe(send_message_tunnel)

    def send_message(event):
        print("Enviar mensagem")
        page.pubsub.send_all(f"{user_name.value}:  {field_message.value}")
        field_message.value = ""
        page.update()

    field_message = ft.TextField(label="Digite sua mensagem", on_submit=send_message)
    button_send = ft.ElevatedButton("Enviar", on_click=send_message)
    line_send = ft.Row([field_message, button_send])
    
    def enter_chat(event):
        print("Entrar no chat")
        popup.open = False
        page.remove(button_start)
        page.remove(text)
        page.add(chat)
        page.pubsub.send_all(f"{user_name.value} entrou no chat")
        page.add(line_send)
        page.add(button_send)
        page.update()

    title_popup = ft.Text("Bem vindo ao Hashzap")
    user_name = ft.TextField(label="Escreva sua mensagem")
    button_open = ft.ElevatedButton("Entrar no chat", on_click=enter_chat)    
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=title_popup,
        content=user_name,
        actions=[button_open]
    )
    
    def open_popup(event):
        page.dialog = popup
        popup.open = True
        page.update()

    button_start = ft.ElevatedButton("Iniciar chat", on_click=open_popup)
    
    page.add(text)
    page.add(button_start)
ft.app(target=main, view=ft.WEB_BROWSER)
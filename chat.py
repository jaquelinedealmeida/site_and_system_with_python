import flet as ft

def main(page):
    text = ft.Text("Hashzap")
    
    popup = ft.AlertDialog()

    def open_popup(event):
        page.dialog = popup
        popup.open = True
        page.update()

    button_start = ft.ElevatedButton("Iniciar chat", on_click=open_popup)
    
    page.add(text)
    page.add(button_start)
ft.app(target=main) 
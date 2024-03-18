# Creates sites and system with Python

## Step 1
- Creates:
  - Title
  - Button to begging chat
    - Click in the button
      - popup/modal
        - Title: "Bem vindo ao Hashzap"
        - field: "write yor name in the chat"field
        - button: enter in the chat
  - chat
  - bellow of the chat
    - field: "Write your message"
    - button: to send
  
Use the ´flet´ - framework of the Python to creae  app and site. 
    *comand&: ´pip install flet´

*Important*:
ft.WEB_BROWSER - para formato web
page.update() - to adds the changes of the page.

## Step 3:
Creates method
    - main: to adds the page
    - open_popup: to adds the event of click
  
For default the method main receive the page and the method to click receives a event 

## Step 4:

Creates a tunnel of communication between chats with pubsub.
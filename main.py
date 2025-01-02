import flet as ft
import requests
import datetime

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK45
    link = 'https://api-production-7a20.up.railway.app/'
   

    def criar_lista(e):
        # def handle_change(e):
        #     data.value =f'{e.control.value.strftime('%Y-%m-%d')}' 
            # page.add(ft.Text(f"Date changed: {e.control.value.strftime('%Y-%m-%d')}"))
            # data = e.control.value.strftime('%Y-%m-%d')

        # def handle_dismissal(e):
        #     page.add(ft.Text(f"DatePicker dismissed"))
        
        calendario = ft.ElevatedButton(
                "Pick date",
                icon=ft.Icons.CALENDAR_MONTH,
                on_click=lambda e: page.open(
                    ft.DatePicker(
                        first_date=datetime.datetime(year=2023, month=10, day=1),
                        last_date=datetime.datetime(year=2024, month=10, day=1),
                        # on_change=handle_change,
                        # on_dismiss=handle_dismissal,
                    )
                ),
            )
        quantidade = ft.Slider(min=0, max=100, divisions=12, label="{value}")
        local = ft.TextField(label='Insira um local')
        criar_lista = ft.FloatingActionButton("Criar")
        
        page.add(
            ft.Container(
                bgcolor=ft.colors.LIGHT_BLUE,
                border_radius=15,
                content=ft.Column(
                    alignment=ft.alignment.center,
                    controls=[
                    ft.Text(f"{calendario.data}"),
                    calendario,
                    ft.Divider(),
                    ft.Text("Selecione a quantidade de pessoas"),
                    quantidade,
                    ft.Divider(),
                    ft.Text("Selecione o local"),
                    local,
                    ft.Divider(),
                    criar_lista,
                    ]
                ),padding=15,
                
            )
            )


    def logar(e):
        response = requests.post(f'{link}/usuario/acesso/',data={'nome_site':login.value,'nome':login.value,'senha':int(str(senha.value))})
        if response.status_code == 200:
                page.clean()
                page.floating_action_button = ft.FloatingActionButton(icon=ft.Icons.ADD,on_click=criar_lista)
                page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

                page.appbar = ft.AppBar(
                    title=ft.Text("Bottom AppBar Demo"),
                    center_title=True,
                    bgcolor=ft.Colors.GREEN_300,
                    automatically_imply_leading=False,
                )
                page.bottom_appbar = ft.BottomAppBar(
                    bgcolor=ft.Colors.BLUE,
                    shape=ft.NotchShape.CIRCULAR,
                    content=ft.Row(
                        controls=[
                            ft.IconButton(icon=ft.Icons.MENU, icon_color=ft.Colors.WHITE),
                            ft.Container(expand=True),
                            ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE),
                            ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE),
                        ]
                    ),
                )
                page.update()
        else:
            page.add(
                ft.Text("erro")
            )
                
        
    def criar_usuario(e):
        response = requests.post(f'{link}/usuario/criacao/',data={'nome_site':novo_login.value,'nome':novo_login.value,'senha':int(str(nova_senha.value))})
        if response.status_code == 200:
            page.clean()
            page.add(
                 ft.Text("criado",color=ft.colors.BLUE),
                 ft.Container(
                container_login,
                alignment=ft.alignment.center,
            ),
            expand=True,
            )
           

            page.update()
        else:
            
            page.add(
                ft.Text(f"{response}")
            )
            page.update()
    
    def voltar(e):
        page.clean()
        page.add(
        ft.SafeArea(
            ft.Container(
                container_login,
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )
    page.update()


    def page_cadastro(e):
        page.clean()
       
        page.add(
            ft.Container(
                novo_container_login,
                alignment=ft.alignment.center,
                expand=True,

            )
           
        )
        page.update()
    
    login = ft.TextField(
            label="Insira seu usuário",
            label_style=ft.TextStyle(color=ft.colors.WHITE), 
            text_style=ft.TextStyle(color=ft.colors.WHITE), 
            border_color=ft.colors.WHITE,
        
            )
    senha = ft.TextField(
            label="Insira sua senha",
            password=True,
            label_style=ft.TextStyle(color=ft.colors.WHITE), 
            text_style=ft.TextStyle(color=ft.colors.WHITE), 
            border_color=ft.colors.WHITE,
            )
    container_login = ft.Container(
            padding=10,
            border_radius=ft.border_radius.all(15),
            width=500, 
            height=500,
            bgcolor=ft.colors.LIGHT_BLUE_500,
            content=ft.Column(
                controls=[ft.Text("Seja bem vindo ao App de Lista",size=15,color=ft.colors.WHITE,text_align=ft.MainAxisAlignment.CENTER),login,senha,
                    ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.FloatingActionButton("Acessar",width=100,on_click=logar),
                        ft.FloatingActionButton("Criar Usuário",width=100,on_click=page_cadastro)
                    ]
                )
                ],
                alignment=ft.MainAxisAlignment.CENTER
                )
            )
    
    novo_login = ft.TextField(
            label="Insira seu novo usuário",
            label_style=ft.TextStyle(color=ft.colors.WHITE), 
            text_style=ft.TextStyle(color=ft.colors.WHITE), 
            border_color=ft.colors.WHITE,
        
            )
    nova_senha = ft.TextField(
                label="Insira sua nova senha",
                password=True,
                label_style=ft.TextStyle(color=ft.colors.WHITE), 
                text_style=ft.TextStyle(color=ft.colors.WHITE), 
                border_color=ft.colors.WHITE,
                )
    novo_container_login = ft.Container(
                padding=10,
                border_radius=ft.border_radius.all(15),
                width=500, 
                height=500,
                bgcolor=ft.colors.LIGHT_BLUE_500,
                content=ft.Column(
                    controls=[ft.Text("Crie aqui seu usuário",size=15,color=ft.colors.WHITE,text_align=ft.MainAxisAlignment.CENTER),novo_login,nova_senha,
                        ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.FloatingActionButton("Criar e Entrar",width=100,on_click=criar_usuario),
                            ft.FloatingActionButton("voltar ao login",width=100,on_click=voltar)
                        ]
                    )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                    )
                )
    page.add(
        ft.SafeArea(
            ft.Container(
                container_login,
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )
    page.update()

ft.app(main)

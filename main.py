import flet as ft
import requests
import datetime

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK45
    link = 'https://web-production-9df03.up.railway.app/'
    def alterar(e):
        global valor
        if valor == 'qtd_participantes':
            info = int(valor.value)
        else:
            info = str(valor.value)
        response = requests.put(f"{link}/new/lista/",data={"lista_relacionada":item_lista['quando'],f"{cg.value}":f"{info}"})
        if response.status_code == 200:
                banner_alteracao = ft.Banner(
                    bgcolor=ft.Colors.GREEN,
                    leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.BLACK, size=40),
                    content=ft.Text(
                        value="Sucesso a alteração foi realizada",
                        color=ft.Colors.BLACK,
                    ),
                    actions=[
                        ft.TextButton(text="fechar", style=action_button_style, on_click=lambda e:page.close(banner_alteracao)),
                    ],
                )
                page.open(banner_alteracao)
                page.update()
        else:
                banner_alteracao = ft.Banner(
                    bgcolor=ft.Colors.RED,
                    leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.BLACK, size=40),
                    content=ft.Text(
                        value="Houve um erro na alteração",
                        color=ft.Colors.BLACK,
                    ),
                    actions=[
                        ft.TextButton(text="fechar", style=action_button_style, on_click=lambda e:page.close(banner_alteracao)),
                    ],
                )
                page.open(banner_alteracao)
                page.update()
    def alterar_lista_dialog(e):
        global valor
        valor = ft.TextField(label="Insira o novo Valor")
        global cg
        cg = ft.RadioGroup(content=ft.Column([
            ft.Radio(value="qtd_participantes", label="Participantes"),
            ft.Radio(value="local", label="Local")]))
        dlg = ft.AlertDialog(modal=True,
                title=ft.Text(f"Participantes"),
                content=ft.Column(
                     controls=[ cg,
                               valor,ft.Row(
                                    controls=[
                                        ft.FloatingActionButton("Alterar",on_click=alterar),
                                        ft.FloatingActionButton("Fechar",on_click=lambda e:page.close(dlg))
                                    ]
                               ),]
                    
                ),
                on_dismiss=lambda e: page.close(dlg),
                )
        page.open(dlg)
        page.update()

    def ver_participantes(e):
            texto=''
            response = requests.get(f"{link}/lista/participantes/",data={"lista_relacionada":item_lista['quando']})
            participantes = response.json()['participantes']
            for participante in participantes:
                 nome = participante
                 texto += f'{nome}\n'
            dlg = ft.AlertDialog(
                title=ft.Text(f"Participantes"),
                content=ft.Text(f"{texto}"),
                on_dismiss=lambda e: page.close(dlg),
                )
                     
            page.open(dlg)
            page.update()   
    def apagar_lista(e):
        global item_lista
        if senha_cancelamento.value == '1020':
            response = requests.delete(f"{link}//new/lista/",data={"lista_relacionada":f'{tentativa}'}) 
            if response.status_code == 200:
                banner_cancelamento = ft.Banner(
                    bgcolor=ft.Colors.GREEN,
                    leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.BLACK, size=40),
                    content=ft.Text(
                        value="Sucesso a lista foi cancelada",
                        color=ft.Colors.BLACK,
                    ),
                    actions=[
                        ft.TextButton(text="fechar", style=action_button_style, on_click=lambda e:page.close(banner_cancelamento)),
                    ],
                )
                page.open(banner_cancelamento)
                page.update()
            else:
                 banner_cancelamento = ft.Banner(
                    bgcolor=ft.Colors.GREEN,
                    leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.BLACK, size=40),
                    content=ft.Text(
                        value="Senha incorreta",
                        color=ft.Colors.BLACK,
                    ),
                    actions=[
                        ft.TextButton(text="fechar", style=action_button_style, on_click=lambda e:page.close(banner_cancelamento)),
                    ],
                )
                 page.open(banner_cancelamento)
                 page.update()
                 
    def apagar_lista_dialog(e):
        global senha_cancelamento
        senha_cancelamento = ft.TextField(label="Insira a senha de administrador",password=True)
        dlg = ft.AlertDialog(
                modal=True,
                title=ft.Text("Insira a senha para Apagar a lista"),
                on_dismiss=lambda e: page.close(dlg),
                actions=[ft.Column(
                     alignment=ft.alignment.center,
                     controls=[
                          senha_cancelamento,
                          ft.Row(
                               alignment=ft.alignment.center,
                               controls=[
                                    ft.FloatingActionButton("Apagar lista",width=80,on_click=apagar_lista),
                                    ft.FloatingActionButton("fechar",width=80,on_click=lambda e:page.close(dlg))
                               ]
                               
                          )
                     ]
                )]
                )
        page.open(dlg)




    def retirar_nome(e):
        global item_lista
        response = requests.delete(f"{link}/listas/participacao/",data={"lista_relacionada":item_lista['quando'],"participante":login.value})
        if response.status_code == 200:
                dlg = ft.AlertDialog(
                title=ft.Text("Sucesso. Seu nome foi retirado da lista"),
                on_dismiss=lambda e: page.close(dlg),
                )
                page.open(dlg)
                page.update()
        else:
                dlg = ft.AlertDialog(
                title=ft.Text("Houve um erro"),
                on_dismiss=lambda e: page.close(dlg),
                )
                page.open(dlg)
                page.update()

    def participar_lista(e):
        global item_lista
        global total_participantes
        response = requests.post(f"{link}/listas/participacao/",data={"participante":login.value,"lista_relacionada":item_lista['quando'],"status":"ativo"})
        if int(total_participantes.json()['total']) < int(str(item_lista['qtd_participantes'])):
            if response.status_code == 200:
                dlg = ft.AlertDialog(
                title=ft.Text("Sucesso. Agora Você está participando da lista"),
                on_dismiss=lambda e: page.close(dlg),
                )
                page.open(dlg)
                page.update()
            elif response.status_code == 400:
                dlg = ft.AlertDialog(
                title=ft.Text("Erro. Você já está participando da lista"),
                on_dismiss=lambda e: page.close(dlg),
                )
                page.open(dlg)
                page.update()
            else:
                dlg = ft.AlertDialog(
                title=ft.Text("Houve um erro"),
                on_dismiss=lambda e: page.close(dlg),
                )
                page.open(dlg)
                page.update()
        else:
            dlg = ft.AlertDialog(
                title=ft.Text("Número máximo de participantes atingido"),
                on_dismiss=lambda e: page.close(dlg),
                )
            page.open(dlg)
            page.update()
              
    def listas_ativas(e):
        global lista_ativa
        lista_ativa = False
        page.clean()
        page.add(
            barra_navegacao
        )
        response = requests.get(f"{link}/listas/listasativas/")
        if response.status_code == 200:
                for i,item in enumerate(response.json()):
                    global item_lista
                    item_lista = item
                    global tentativa
                    tentativa = item['quando']
                    global total_participantes
                    total_participantes = requests.get(f"{link}/lista/ativa/totalparticipantes/",data={"lista_relacionada":item['quando']})
                    page.add(
                        ft.Card(
                            content=ft.Container(
                                content=ft.Column(
                                    [
                                        ft.ListTile(
                                            leading=ft.Icon(ft.icons.LIST),
                                            title=ft.Text(f"Data: {item['quando']}"),
                                            subtitle=ft.Text(
                                            f"""Local: {item['local']}
                                Participantes: {total_participantes.json()['total']}
                                Máximo: {item['qtd_participantes']}"""
                                            
                                            ,text_align=ft.alignment.center),
                                        ),
                                        ft.Row(
                                            [ft.IconButton(ft.icons.OPEN_IN_NEW,on_click=participar_lista), ft.IconButton(ft.icons.CLOSE,on_click=retirar_nome),ft.IconButton(icon=ft.Icons.PERSON,on_click=ver_participantes),ft.IconButton(icon=ft.Icons.EDIT,on_click=alterar_lista_dialog),ft.IconButton(icon=ft.Icons.DELETE,on_click=apagar_lista_dialog)],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                        ),
                                    ]
                                ),
                                width=400,
                                padding=10,
                            )
                        )
                    
                    )
#                     ft.CupertinoContextMenu(
#                                     content=ft.Text(f"""
# Local: {item['local']}
# Data: {item['quando']}
# Participantes: {total_participantes.json()['total']}
# Máximo: {item['qtd_participantes']}""",color=ft.colors.LIGHT_BLUE),
#                                     actions=[
#                                         ft.CupertinoContextMenuAction(
#                                             text="Participar",
#                                             trailing_icon=ft.Icons.CHECK,
#                                             on_click=participar_lista,
#                                         ),
#                                         ft.CupertinoContextMenuAction(
#                                             text="Retirar Nome",
#                                             trailing_icon=ft.Icons.CANCEL,
#                                             on_click=retirar_nome,
#                                         ),
#                                         ft.CupertinoContextMenuAction(
#                                             text="Editar",
#                                             trailing_icon=ft.Icons.EDIT,
#                                             on_click=lambda e: print("Action 3"),
#                                         ),
#                                         ft.CupertinoContextMenuAction(
#                                             text="Apagar",
#                                             trailing_icon=ft.Icons.DELETE,
#                                             on_click=apagar_lista_dialog,
#                                         ),
#                                         ft.CupertinoContextMenuAction(
#                                             text="Nomes",
#                                             trailing_icon=ft.Icons.FACE,
#                                             on_click=apagar_lista_dialog,
#                                         ),
#                                     ],
#                                 )
#                             )
                    page.update()
    def ver_menu(e):
        global lista_ativa
        lista_ativa = False     

    def close_banner(e):
        global banner
        banner = banner
        page.close(banner)
        page.update()
        
    def criar_listas(e):
        global data
        
        quando = str(data)
        qtd_participantes = quantidade
        response = requests.post(f"{link}/new/lista/",data={'lista_relacionada':quando,"quando":quando,"criador":login.value,"qtd_participantes":qtd_participantes.value,"status":"ativo","local":text_local.value})   
        if response.status_code == 200:
            global banner
            banner = ft.Banner(
            bgcolor=ft.Colors.LIGHT_GREEN,
            leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.BLACK, size=40),
            content=ft.Text(
                value=f"Sucesso uma nova lista foi criada para a data {quando} com {qtd_participantes} participantes",
                color=ft.Colors.BLACK,
            ),
            actions=[   
                ft.TextButton(text="ok", style=action_button_style, on_click=close_banner),
            ],
        ) 
            page.open(banner)
            page.update()
        elif response.status_code == 400:
            banner = ft.Banner(
            bgcolor=ft.Colors.AMBER,
            leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.BLUE, size=40),
            content=ft.Text(
                value=f"Já existe uma lista criada para essa data {quando}",
                color=ft.Colors.BLACK,
            ),
            actions=[   
                ft.TextButton(text="ok", style=action_button_style, on_click=close_banner),
            ],
        ) 
            page.open(banner)
            page.update()
        else:
            banner = ft.Banner(
            bgcolor=ft.Colors.RED,
            leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.BLUE, size=40),
            content=ft.Text(
                value=f"Houve um erro na criação da lista",
                color=ft.Colors.BLACK,
            ),
            actions=[   
                ft.TextButton(text="ok", style=action_button_style, on_click=close_banner),
            ],
        ) 
            page.open(banner)
            page.update()

    def handle_change(e): 
                global data
                data = e.control.value.strftime('%Y-%m-%d')

    def pagina_criar_lista(e):  
            
            global criacao_lista
            criacao_lista = lista = ft.Container(
                        bgcolor=ft.colors.LIGHT_BLUE,
                        border_radius=15,
                        content=ft.Column(
                            alignment=ft.alignment.center,
                            controls=[
                            ft.Text('Selecione uma data'),
                            calendario,
                            ft.Divider(),
                            ft.Text("Selecione a quantidade de pessoas"),
                            quantidade,
                            ft.Divider(),
                            ft.Text("Selecione o local"),
                            text_local,
                            ft.Divider(),
                            ft.FloatingActionButton("Criar",width=50,on_click=criar_listas),
                            ]
                        ),padding=15,
                        
                    )  
            global lista_ativa
            if lista_ativa == False:
                page.clean()
                page.add(
                    lista,
                    barra_navegacao
                    )
                lista_ativa = True
            else:
                 pass


    def logar(e):
        response = requests.post(f'{link}/usuario/acesso/',data={'nome_site':login.value,'nome':login.value,'senha':int(str(senha.value))})
        if response.status_code == 200:
                page.clean()
                page.floating_action_button = ft.FloatingActionButton(icon=ft.Icons.ADD,on_click=pagina_criar_lista)
                page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
                global barra_navegacao
                barra_navegacao = ft.BottomAppBar(
                    bgcolor=ft.Colors.BLUE,
                    shape=ft.NotchShape.CIRCULAR,
                    content=ft.Row(
                        controls=[
                            ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE,on_click=listas_ativas),
                            ft.Container(expand=True),
                            ft.IconButton(icon=ft.Icons.ACCOUNT_BOX, icon_color=ft.Colors.WHITE),
                        ]
                    ),
                )
                page.bottom_appbar = barra_navegacao
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
    global data
    data = None
    global lista_ativa
    lista_ativa = False
    global ver_listas_ativas
    ver_listas_ativas = False
    action_button_style = ft.ButtonStyle(color=ft.Colors.BLUE)
    
    element = ft.DatePicker(
                            first_date=datetime.datetime(year=2025, month=1, day=1),
                            last_date=datetime.datetime(year=2100, month=12, day=31),
                            on_change=handle_change,
                            # on_dismiss=handle_dismissal,
                        )
    calendario = ft.ElevatedButton(
                    "Pick date",
                    icon=ft.Icons.CALENDAR_MONTH,
                    on_click=lambda e: page.open(
                        element
                    ),
                )
    quantidade = ft.Slider(min=0, max=100, divisions=12, label="{value}")
    text_local = ft.TextField(label='Insira um local')
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

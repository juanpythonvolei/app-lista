import flet as ft
import requests
import datetime

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    link = 'https://api-production-0138.up.railway.app/'
    def zerar_placar(e):
        global placar_timea
        global placar_timeb
        placar_timea.value = 0
        placar_timeb.value = 0
        page.update()
    def aumentar_placar_timea(e):
        global placar_timea
        placar_timea.value +=1
        page.update()
    def aumentar_placar_timeb(e):
        global placar_timeb
        placar_timeb.value +=1
        page.update()
    def diminuir_placar_timea(e):
        global placar_timea
        placar_timea.value -=1
        page.update()
    def diminuir_placar_timeb(e):
        global placar_timeb
        placar_timeb.value -=1
        page.update()
    def page_placar(e):
        global placar_timea
        placar_timea = ft.Text(size=80,value=0)
        global placar_timeb
        placar_timeb = ft.Text(size=80,value=0)
        page.clean()
        page.add(
            ft.Row(
                controls=[
                    ft.FloatingActionButton(icon=ft.icons.LOGIN_OUTLINED,on_click=voltar),
                    ft.FloatingActionButton(icon=ft.icons.CLEAR_ROUNDED,on_click=zerar_placar),
                ]
            ),
            ft.Container(
                
                ft.Column(
                    controls=[
                        ft.Text("Time A",size=20,font_family='monospace',weight=ft.FontWeight.BOLD,color=ft.colors.LIGHT_BLUE),
                        ft.Container(bgcolor=ft.colors.BLUE,padding=20,content=placar_timea,border_radius=15),
                        ft.Row(
                            controls=[
                                ft.FloatingActionButton(icon=ft.icons.ADD,bgcolor=ft.colors.GREEN,on_click=aumentar_placar_timea),
                                ft.FloatingActionButton('-',bgcolor=ft.colors.RED,on_click=diminuir_placar_timea)
                            ]
                        )
                    ]
                )
                ,alignment=ft.alignment.center,padding=2
            ),
            ft.Divider(),
            ft.Container(
                
                ft.Column(
                    controls=[
                        ft.Text("Time B",font_family='monospace',weight=ft.FontWeight.BOLD,color=ft.colors.RED,size=20),
                        ft.Container(bgcolor=ft.colors.RED,padding=20,content=placar_timeb,border_radius=15),
                        ft.Row(
                            controls=[
                                ft.FloatingActionButton(icon=ft.icons.ADD,bgcolor=ft.colors.GREEN,on_click=aumentar_placar_timeb),
                                ft.FloatingActionButton('-',bgcolor=ft.colors.BLUE,on_click=diminuir_placar_timeb)
                            ]
                        )
                    ]
                ),
                alignment=ft.alignment.center,padding=2
            )
        )
    def apagar_perfil(e):
        if int(senha_apagar_perfil.value) == int(senha.value):
            response = requests.delete(f'{link}/usuario/manipular/{login.value}/')
            if response.status_code == 202:
                    banner_alteracao_perfil = ft.Banner(
                        bgcolor=ft.Colors.GREEN,
                        leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.BLACK, size=40),
                        content=ft.Text(
                            value="Sucesso. Perfil excluido",
                            color=ft.Colors.BLACK,weight=ft.FontWeight.BOLD,size=20
                        ),
                        actions=[
                            ft.TextButton(text="fechar",color=ft.colors.BLACK, on_click=lambda e:page.close(banner_alteracao_perfil)),
                        ],
                    )
                    page.open(banner_alteracao_perfil)
                    page.clean()
                    voltar()
            else:
                    banner_alteracao_perfil = ft.Banner(
                        bgcolor=ft.Colors.RED,
                        leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.BLACK, size=40),
                        content=ft.Text(
                            value="Erro",
                            color=ft.Colors.BLACK,weight=ft.FontWeight.BOLD,size=20
                        ),
                        actions=[
                            ft.TextButton(text="fechar",color=ft.colors.BLACK, on_click=lambda e:page.close(banner_alteracao_perfil)),
                        ],
                    )
                    page.open(banner_alteracao_perfil)
                    page.update()
        else:
                    banner_alteracao_perfil = ft.Banner(
                        bgcolor=ft.Colors.RED,
                        leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.BLACK, size=40),
                        content=ft.Text(
                            value="Erro Senha incorreta",
                            color=ft.Colors.BLACK,
                            weight=ft.FontWeight.BOLD,size=20
                        ),
                        actions=[
                            ft.TextButton(text="fechar",color=ft.colors.BLACK, on_click=lambda e:page.close(banner_alteracao_perfil)),
                        ],
                    )
                    page.open(banner_alteracao_perfil)
                    page.update()
    def dialog_apagar_perfil(e):
        global senha_apagar_perfil
        senha_apagar_perfil = ft.TextField(label="Insira a sua senha",password=True,label_style=ft.TextStyle(color=ft.colors.WHITE), 
            text_style=ft.TextStyle(color=ft.colors.WHITE), 
            border_color=ft.colors.WHITE,
            icon=ft.icons.PASSWORD)
        dlg = ft.AlertDialog(
                modal=True,
                title=ft.Text("Insira a senha para Apagar o seu perfil",weight=ft.FontWeight.BOLD,size=20),
                on_dismiss=lambda e: page.close(dlg),
                actions=[ft.Column(
                     alignment=ft.alignment.center,
                     controls=[
                          senha_apagar_perfil,
                          ft.Row(
                               alignment=ft.alignment.center,
                               controls=[
                                    ft.FloatingActionButton(icon=ft.icons.DELETE_SHARP,width=80,on_click=apagar_perfil),
                                    ft.FloatingActionButton(icon=ft.icons.CLOSE_OUTLINED,width=80,on_click=lambda e:page.close(dlg))
                               ]
                               
                          )
                     ]
                )]
                )
        page.open(dlg)
    def alterar_perfil(e):
        response = requests.put(f'{link}/usuario/manipular/{login.value}/',data={"senha":int(nova_senha_perfil.value),"nome_site":login.value})
        if response.status_code == 202:
                banner_alteracao_perfil = ft.Banner(
                    bgcolor=ft.Colors.GREEN,
                    leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.BLACK, size=40),
                    content=ft.Text(
                        value="Sucesso a alteração foi realizada",
                        color=ft.Colors.BLACK,weight=ft.FontWeight.BOLD,size=20
                    ),
                    actions=[
                        ft.TextButton(text="fechar",color=ft.colors.BLACK, on_click=lambda e:page.close(banner_alteracao_perfil)),
                    ],
                )
                page.open(banner_alteracao_perfil)
                page.update()
        else:
                banner_alteracao_perfil = ft.Banner(
                    bgcolor=ft.Colors.RED,
                    leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.BLACK, size=40),
                    content=ft.Text(
                        value="Erro",
                        color=ft.Colors.BLACK,weight=ft.FontWeight.BOLD,size=20
                    ),
                    actions=[
                        ft.TextButton(text="fechar",color=ft.colors.BLACK, on_click=lambda e:page.close(banner_alteracao_perfil)),
                    ],
                )
                page.open(banner_alteracao_perfil)
                page.update()
    def page_alterar_perfil(e):
        page.clean()
        global nova_senha_perfil
        nova_senha_perfil = ft.TextField(label="Insira sua nova senha",password=True,label_style=ft.TextStyle(color=ft.colors.WHITE), 
            text_style=ft.TextStyle(color=ft.colors.WHITE), 
            border_color=ft.colors.WHITE,
            icon=ft.icons.PASSWORD)
        informacoes = ft.Container(
            alignment=ft.alignment.center,
            bgcolor=ft.colors.LIGHT_BLUE,
            border_radius=15,
            padding=10,
            content=ft.Column(
                alignment=ft.alignment.center,
                controls=[
                    ft.Text('Altere sua senha',weight=ft.FontWeight.BOLD,size=20),
                    ft.Column(
                        controls=[nova_senha_perfil,ft.FloatingActionButton("Alterar Perfil",icon=ft.Icons.VERIFIED,bgcolor=ft.colors.GREEN,on_click=alterar_perfil)]
                    ),
                    ft.FloatingActionButton('Apagar Perfil',icon=ft.Icons.DELETE,bgcolor=ft.colors.RED,on_click=dialog_apagar_perfil)
                ]
            )
        )
        page.add(informacoes)
        page.update()
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
                        color=ft.Colors.BLACK,weight=ft.FontWeight.BOLD,size=15
                    ),
                    actions=[
                        ft.TextButton(text="fechar",color=ft.colors.BLACK, on_click=lambda e:page.close(banner_alteracao)),
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
                        color=ft.Colors.BLACK,weight=ft.FontWeight.BOLD,size=15
                    ),
                    actions=[
                        ft.TextButton(text="fechar",color=ft.colors.BLACK, on_click=lambda e:page.close(banner_alteracao)),
                    ],
                )
                page.open(banner_alteracao)
                page.update()
    def alterar_lista_dialog(e):
        global valor
        valor = ft.TextField(label="Insira o novo Valor",label_style=ft.TextStyle(color=ft.colors.WHITE), 
            text_style=ft.TextStyle(color=ft.colors.WHITE), 
            border_color=ft.colors.WHITE,
            icon=ft.icons.INFO_ROUNDED)
        global cg
        cg = ft.RadioGroup(content=ft.Column([
            ft.Radio(value="qtd_participantes", label="Participantes"),
            ft.Radio(value="local", label="Local")]))
        dlg = ft.AlertDialog(modal=True,
                title=ft.Text(f"Participantes",weight=ft.FontWeight.BOLD,size=15),
                content=ft.Column(
                     controls=[ cg,
                               valor,ft.Row(
                                    controls=[
                                        ft.FloatingActionButton("Alterar",on_click=alterar,icon=ft.icons.CHANGE_HISTORY)   ,
                                        ft.FloatingActionButton(icon=ft.icons.CLOSE_FULLSCREEN,on_click=lambda e:page.close(dlg))
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
                title=ft.Text(f"Participantes",weight=ft.FontWeight.BOLD,size=20),
                content=ft.Text(f"{texto}",weight=ft.FontWeight.BOLD,size=15),
                on_dismiss=lambda e: page.close(dlg),
                )
                     
            page.open(dlg)
            page.update()   
    def apagar_lista(e):
        if senha_cancelamento.value == '1020':
            response = requests.delete(f"{link}//new/lista/",data={"lista_relacionada":f'{str(var_quando)}'}) 
            if response.status_code == 200:
                banner_cancelamento = ft.Banner(
                    bgcolor=ft.Colors.GREEN,
                    leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.BLACK, size=40),
                    content=ft.Text(
                        value="Sucesso a lista foi cancelada",
                        color=ft.Colors.BLACK,
                        weight=ft.FontWeight.BOLD,size=15
                    ),
                    actions=[
                        ft.TextButton(text="fechar",color=ft.colors.BLACK, on_click=lambda e:page.close(banner_cancelamento)),
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
                        weight=ft.FontWeight.BOLD,size=15
                    ),
                    actions=[
                        ft.TextButton(text="fechar",color=ft.colors.BLACK, on_click=lambda e:page.close(banner_cancelamento)),
                    ],
                )
                 page.open(banner_cancelamento)
                 page.update()
                 
    def apagar_lista_dialog(e):
        global senha_cancelamento
        senha_cancelamento = ft.TextField(label="Insira a senha de administrador",password=True,label_style=ft.TextStyle(color=ft.colors.WHITE), 
            text_style=ft.TextStyle(color=ft.colors.WHITE), 
            border_color=ft.colors.WHITE,
            icon=ft.icons.PASSWORD_ROUNDED)
        dlg = ft.AlertDialog(
                modal=True,
                title=ft.Text("Insira a senha",weight=ft.FontWeight.BOLD,size=15),
                on_dismiss=lambda e: page.close(dlg),
                actions=[ft.Column(
                     alignment=ft.alignment.center,
                     controls=[
                          senha_cancelamento,
                          ft.Row(
                               alignment=ft.alignment.center,
                               controls=[
                                    ft.FloatingActionButton(icon=ft.icons.DELETE_FOREVER_ROUNDED,width=80,on_click=apagar_lista),
                                    ft.FloatingActionButton(icon=ft.icons.CLOSE_ROUNDED,width=80,on_click=lambda e:page.close(dlg))
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
                title=ft.Text("Sucesso. Seu nome foi retirado da lista",weight=ft.FontWeight.BOLD,size=15),
                on_dismiss=lambda e: page.close(dlg),
                )
                page.open(dlg)
                page.update()
        else:
                dlg = ft.AlertDialog(
                title=ft.Text("Houve um erro",weight=ft.FontWeight.BOLD,size=15),
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
                title=ft.Text("Sucesso. Agora Você está participando da lista",weight=ft.FontWeight.BOLD,size=15),
                on_dismiss=lambda e: page.close(dlg),
                )
                page.open(dlg)
                page.update()
            elif response.status_code == 400:
                dlg = ft.AlertDialog(
                title=ft.Text("Erro. Você já está participando da lista",weight=ft.FontWeight.BOLD,size=15),
                on_dismiss=lambda e: page.close(dlg),
                )
                page.open(dlg)
                page.update()
            else:
                dlg = ft.AlertDialog(
                title=ft.Text("Houve um erro",weight=ft.FontWeight.BOLD,size=15),
                on_dismiss=lambda e: page.close(dlg),
                )
                page.open(dlg)
                page.update()
        else:
            dlg = ft.AlertDialog(
                title=ft.Text("Número máximo de participantes atingido",weight=ft.FontWeight.BOLD,size=15),
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
                    global total_participantes
                    total_participantes = requests.get(f"{link}/lista/ativa/totalparticipantes/",data={"lista_relacionada":item['quando']})
                    global var_quando
                    var_quando = item['quando']
                    page.add(
                        ft.Card(
                            content=ft.Container(
                                content=ft.Column(
                                    [
                                        ft.ListTile(
                                            leading=ft.Icon(ft.icons.LIST),
                                            title=ft.Text(f"Data: {item['quando']}",weight=ft.FontWeight.BOLD,size=15),
                                            subtitle=ft.Text(
                                            f"""Local: {item['local']}\n
                                                            Participantes: {total_participantes.json()['total']}\n
                                                            Máximo: {item['qtd_participantes']}
                                """
                                            
                                            ,text_align=ft.alignment.center,weight=ft.FontWeight.BOLD,size=15),
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
                font_family='monospace',
                weight=ft.FontWeight.BOLD,
                size=20
            ),
            actions=[   
                ft.TextButton(text="ok",color=ft.colors.BLACK, on_click=close_banner),
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
                font_family='monospace',weight=ft.FontWeight.BOLD,size=20
            ),
            actions=[   
                ft.TextButton(text="ok",color=ft.colors.BLACK, on_click=close_banner),
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
                font_family='monospace',weight=ft.FontWeight.BOLD,size=20
            ),
            actions=[   
                ft.TextButton(text="ok",color=ft.colors.BLACK,on_click=close_banner),
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
                            ft.Text(f"Selecione uma Data",font_family='monospace',weight=ft.FontWeight.BOLD,size=20),
                            calendario,
                            ft.Divider(),
                            ft.Text("Selecione a quantidade de pessoas",font_family='monospace',weight=ft.FontWeight.BOLD,size=20),
                            quantidade,
                            ft.Divider(),
                            ft.Text("Selecione o local",font_family='monospace',weight=ft.FontWeight.BOLD,size=20),
                            text_local,
                            ft.Divider(),
                            ft.FloatingActionButton("Criar",on_click=criar_listas,icon=ft.icons.NEW_RELEASES_ROUNDED),
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
    def voltar_ao_inicio(e):
        page.clean()
        page.bottom_appbar = None
        page.floating_action_button = None
        voltar(e)

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
                            ft.IconButton(icon=ft.Icons.LOGIN_ROUNDED, icon_color=ft.Colors.WHITE,on_click=voltar_ao_inicio),
                            ft.IconButton(icon=ft.Icons.PERSON, icon_color=ft.Colors.WHITE,on_click=page_alterar_perfil),
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
            voltar()
            banner_criar_usuario = ft.Banner(
            bgcolor=ft.Colors.GREEN,
            leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.BLUE, size=40),
            content=ft.Text(
                value=f"Sucesso O novo usuário foi criado",
                color=ft.Colors.BLACK,
                font_family='monospace',weight=ft.FontWeight.BOLD,size=20
            ),
            actions=[   
                ft.TextButton(text="ok",color=ft.colors.BLACK,on_click=lambda e:page.close(banner_criar_usuario)),
            ],
        ) 
            page.open(banner)
            page.update()
            
        else:
            banner = ft.Banner(
            bgcolor=ft.Colors.RED,
            leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.BLUE, size=40),
            content=ft.Text(
                value=f"Erro ao criar um usuário",
                color=ft.Colors.BLACK,
                font_family='monospace',weight=ft.FontWeight.BOLD,size=20
            ),
            actions=[   
                ft.TextButton(text="ok",color=ft.colors.BLACK,on_click=lambda e:page.close(banner_criar_usuario)),
            ],
        ) 
            page.open(banner)
            page.update()
    
    def voltar(e):
        page.clean()
        page.add(
        ft.FloatingActionButton(icon=ft.icons.SCOREBOARD,bgcolor=ft.colors.BLUE,on_click=page_placar),    
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
    quantidade = ft.Slider(min=0, max=100, divisions=100, label="{value}")
    text_local = ft.TextField(label='Insira um local',label_style=ft.TextStyle(color=ft.colors.WHITE), 
            text_style=ft.TextStyle(color=ft.colors.WHITE), 
            border_color=ft.colors.WHITE,
            icon=ft.icons.PLACE)
    login = ft.TextField(
            label="Insira seu usuário",
            label_style=ft.TextStyle(color=ft.colors.WHITE), 
            text_style=ft.TextStyle(color=ft.colors.WHITE), 
            border_color=ft.colors.WHITE,
            icon=ft.icons.PERSON
        
            )
    senha = ft.TextField(
            label="Insira sua senha",
            password=True,
            label_style=ft.TextStyle(color=ft.colors.WHITE), 
            text_style=ft.TextStyle(color=ft.colors.WHITE), 
            border_color=ft.colors.WHITE,
            icon=ft.icons.PASSWORD
            )
    container_login = ft.Container(
            padding=20,
            width=350,
            height=350,
            border_radius=ft.border_radius.all(15),
            bgcolor=ft.colors.LIGHT_BLUE,
            content=ft.Column(
                controls=[ft.Text("Seja bem vindo ao App de Lista",color=ft.colors.WHITE,text_align=ft.alignment.center,weight=ft.FontWeight.BOLD,size=15),login,senha,
                    ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.FloatingActionButton("Acessar",on_click=logar,icon=ft.icons.ASSIGNMENT),
                        ft.FloatingActionButton("Criar Usuário",on_click=page_cadastro,icon=ft.icons.APP_REGISTRATION)
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
            icon=ft.icons.PERSON
        
            )
    nova_senha = ft.TextField(
                label="Insira sua nova senha",
                password=True,
                label_style=ft.TextStyle(color=ft.colors.WHITE), 
                text_style=ft.TextStyle(color=ft.colors.WHITE), 
                border_color=ft.colors.WHITE,
                icon=ft.icons.PASSWORD
                )
    novo_container_login = ft.Container(
                padding=20,
                border_radius=ft.border_radius.all(15),
                bgcolor=ft.colors.LIGHT_BLUE,
                width=350,
                height=350,
                content=ft.Column(
                    controls=[ft.Text("Crie aqui seu usuário",color=ft.colors.WHITE,text_align=ft.alignment.center,weight=ft.FontWeight.BOLD,size=20),novo_login,nova_senha,
                        ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.FloatingActionButton("Criar",on_click=criar_usuario,icon=ft.icons.ACCOUNT_BOX_ROUNDED),
                            ft.FloatingActionButton("voltar ao login",on_click=voltar,icon=ft.icons.TURN_LEFT_OUTLINED)
                        ]
                    )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                    )
                )
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(
        ft.FloatingActionButton(icon=ft.icons.SCOREBOARD,bgcolor=ft.colors.BLUE,on_click=page_placar),
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

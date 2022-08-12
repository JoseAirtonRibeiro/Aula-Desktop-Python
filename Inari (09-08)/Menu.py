#===============================
from classe_banco_de_dados import *
import posiciona
from tkinter import *
#===============================
#Funções
db = Banco()

def Placeholder_cad_prod(event):
    ent_cad_prod_valor.config(state=NORMAL)
    ent_cad_prod_valor.delete(0, 'end')
    ent_cad_prod_nome.config(state=NORMAL)
    ent_cad_prod_nome.delete(0, 'end')


def Placeholder_com(event):
    ent_compra_cliente.config(state=NORMAL)
    ent_compra_cliente.delete(0, 'end')
    ent_compra_produto.config(state=NORMAL)
    ent_compra_produto.delete(0, 'end')


def Placeholder_cli(event):
    ent_nome.config(state=NORMAL)
    ent_nome.delete(0, 'end')
    ent_email.config(state=NORMAL)
    ent_email.delete(0, 'end')
    ent_telefone.config(state=NORMAL)
    ent_telefone.delete(0, 'end')


def delete():
    ent_nome_prod.delete(0, 'end')
    ent_nome_hist.delete(0, 'end')
    lb_lista_produto.delete(0, 'end')
    lb_lista_quarto.delete(0, 'end')
    ent_nome.delete(0, 'end')
    ent_email.delete(0, 'end')
    ent_telefone.delete(0, 'end')
    ent_cad_prod_nome.delete(0, 'end')
    ent_cad_prod_valor.delete(0, 'end')


def format(event=None):
    nome = ent_nome.get().replace('.', '').replace(',', '').replace('²', '')[:60]
    telefone = ent_telefone.get().replace('-', '').replace('(', '').replace(')', '')[:12]
    valor = ent_cad_prod_valor.get().replace('.', '').replace('²', '')[:7]
    frt_valor = ''
    frt_telefone = ''
    frt_nome = ''

    if event.keysym.lower() == 'backspace': return

    for i in range(len(telefone)):
        if not telefone[i] in '0123456789': continue
        if i in [1]: frt_telefone += telefone[i] + '+ '
        elif i == 7:
            frt_telefone += telefone[i] + '-'
        else:
            frt_telefone +=telefone[i]
    
    for i in range(len(valor)):
        if not valor[i] in '0123456789': continue
        frt_valor += valor[i]

    for i in range(len(nome)):
        if nome[i] in '0123456789': continue
        frt_nome += nome[i]


    ent_nome.delete(0, 'end')
    ent_cad_prod_valor.delete(0, 'end')        
    ent_telefone.delete(0, 'end')


    ent_nome.insert(0, frt_nome)
    ent_cad_prod_valor.insert(0, frt_valor)
    ent_telefone.insert(0, frt_telefone)
#===============================
laranja = '#FF5757'
branco = '#FFFFFF'
cinza = '#D9D9D9'
#===============================
win = Tk()
win.resizable(False, False)
win.geometry('1600x900')
win.title('Inari.Comp')
win.iconbitmap('img/icon.ico')
win.bind('<Button-1>', posiciona.inicio_place)                                    
win.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, win))          
win.bind('<Button-2>', lambda arg: posiciona.para_geometry(arg, win))            
win.bind('<KeyRelease>') 
#===============================
#Frames
frame_cad_cli = Frame(win)
frame_cad_pro = Frame(win)
frame_histori = Frame(win)
frame_menu = Frame(win)
frame_list_pro = Frame(win)
frame_list_qua = Frame(win)
frame_logo = Frame(win)
frame_compra = Frame(win)
#===============================
#imagens
cad_cliente = PhotoImage(file='img/cad_cliente.png')
cad_produto = PhotoImage(file='img/cad_prod.png')
historico = PhotoImage(file='img/historico.png')
list_produto = PhotoImage(file='img/list_prod.png')
list_quarto = PhotoImage(file='img/list_quart.png')
logo = PhotoImage(file='img/logo.png')
menu = PhotoImage(file='img/menu_main.png')
compra_prod = PhotoImage(file='img/Compra.png')
#===============================
#sub-imagens
voltar1 = PhotoImage(file='img/voltar_1.png')
voltar2 = PhotoImage(file='img/voltar_2.png')
log_button = PhotoImage(file='img/log.png')
bt_listar = PhotoImage(file='img/bt_lista.png')
#===============================
#frame_logo
lb_bg_logo = Label(frame_logo, image=logo, bd=0)
lb_bg_logo.pack()
frame_logo.pack()
win.after(100, frame_logo.forget)
#===============================
#frame_cad_cliente
lb_bg_cli = Label(frame_cad_cli, image=cad_cliente, bd=0)
ent_nome = Entry(frame_cad_cli, font='Arial 30', bd=0, bg=branco)
ent_email = Entry(frame_cad_cli, font='Arial 30', bd=0, bg=branco)
ent_telefone = Entry(frame_cad_cli, font='Arial 30', bd=0, bg=branco)
nv_telefone = ent_telefone.get().replace('+', '').replace('-', '').replace(' ', '')
bt_log = Button(frame_cad_cli, image=log_button, bd=0, command=lambda: [db.cadastrar_cliente(ent_nome.get(), ent_email.get(), ent_telefone.get()), frame_menu.pack(), frame_cad_cli.forget(), delete()])
ent_nome.bind('<KeyRelease>', format)
ent_telefone.bind('<KeyRelease>', format)

ent_nome.insert(0, 'Nome...')
ent_nome.config(state=DISABLED)
ent_nome.bind('<Button-1>', Placeholder_cli)

ent_email.insert(0, 'Email...')
ent_email.config(state=DISABLED)
ent_email.bind('<Button-1>', Placeholder_cli)

ent_telefone.insert(0, 'Telefone...')
ent_telefone.config(state=DISABLED)
ent_telefone.bind('<Button-1>', Placeholder_cli)

bt_log.place(width=141, height=142, x=1148, y=668)
ent_nome.place(width=697, height=48, x=861, y=299)
ent_email.place(width=697, height=48, x=861, y=432)
ent_telefone.place(width=697, height=48, x=861, y=566)
frame_cad_cli.pack()
lb_bg_cli.pack()
#===============================
#frame_menu
lb_bg_menu = Label(frame_menu, image=menu, bd=0)
bt_cad_prod = Button(frame_menu, text='Cadastrar Produto', font='Arial 30', bd=0, bg=branco, activebackground=branco, command=lambda: [frame_cad_pro.pack(), frame_menu.forget()])
bt_cad_cli = Button(frame_menu, text='Cadastrar Cliente ', font='Arial 30', bd=0, bg=branco, activebackground=branco, command=lambda: [frame_cad_cli.pack(), frame_menu.forget()])
bt_cad_finalizar = Button(frame_menu, text='Realizar Compra  ', font='Arial 30', bd=0, bg=branco, activebackground=branco, command=lambda: [frame_compra.pack(), frame_menu.forget()])
bt_cad_list_quartos = Button(frame_menu, text='Listar Quartos   ', font='Arial 30', bd=0, bg=branco, activebackground=branco, command=lambda: [frame_list_qua.pack(), frame_menu.forget()])
bt_cad_list_prod = Button(frame_menu, text='Listar Produtos  ', font='Arial 30', bd=0, bg=branco, activebackground=branco, command=lambda: [frame_list_pro.pack(), frame_menu.forget()])
bt_cad_hist = Button(frame_menu, text='Mostrar histórico', font='Arial 30', bd=0, bg=branco, activebackground=branco, command=lambda: [frame_histori.pack(), frame_menu.forget()])


bt_cad_hist.place(width=324, height=57, x=1233, y=478)
bt_cad_list_prod.place(width=323, height=57, x=734, y=558)
bt_cad_list_quartos.place(width=322, height=56, x=732, y=479)
bt_cad_finalizar.place(width=321, height=57, x=1234, y=211)
bt_cad_cli.place(width=321, height=57, x=718, y=289)
bt_cad_prod.place(width=321, height=57, x=718, y=211)
lb_bg_menu.pack()
#===============================
#frame_compra
lb_bg_compra = Label(frame_compra, image=compra_prod, bd=0)
bt_voltar = Button(frame_compra, image=voltar2, bd=0, command=lambda: [frame_menu.pack(), frame_compra.forget()])
ent_compra_cliente = Entry(frame_compra, bd=0, font='Arial 30')
ent_compra_produto = Entry(frame_compra, bd=0, font='Arial 30')
bt_compra_produto = Button(frame_compra, bd=0, image=log_button, command=lambda:[db.comprar_produtos(ent_compra_cliente.get(), ent_compra_produto.get())])

bt_compra_produto.place(width=141, height=142, x=1140, y=669)
ent_compra_cliente.place(width=698, height=48, x=861, y=343)
ent_compra_produto.place(width=697, height=48, x=861, y=476)
bt_voltar.place(width=121, height=121, x=1441, y=51)

ent_compra_produto.insert(0, 'Nome do Produto...')
ent_compra_produto.config(state=DISABLED)
ent_compra_produto.bind('<Button-1>', Placeholder_com)

ent_compra_cliente.insert(0, 'Nome do Cliente')
ent_compra_cliente.config(state=DISABLED)
ent_compra_cliente.bind('<Button-1>', Placeholder_com)


lb_bg_compra.pack()
#===============================
#frame_cad_produto
lb_bg_pro = Label(frame_cad_pro, image=cad_produto, bd=0)
bt_voltar_pro = Button(frame_cad_pro, image=voltar2, bd=0, command=lambda: [frame_menu.pack(), frame_cad_pro.forget()])
ent_cad_prod_nome = Entry(frame_cad_pro, font='Arial 30', bd=0)
ent_cad_prod_valor = Entry(frame_cad_pro, font='Arial 30', bd=0)
nv_valor = ent_cad_prod_valor.get().replace(',', '')
bt_log_prod = Button(frame_cad_pro, image=log_button, bd=0, command=lambda: [db.cadastrar_produto(ent_cad_prod_nome.get(), ent_cad_prod_valor.get(), delete())])

ent_cad_prod_valor.bind('<KeyRelease>', format)

ent_cad_prod_valor.insert(0, 'Valor do Produto')
ent_cad_prod_valor.config(state=DISABLED)
ent_cad_prod_valor.bind('<Button-1>', Placeholder_cad_prod)

ent_cad_prod_nome.insert(0, 'Nome do Produto')
ent_cad_prod_nome.config(state=DISABLED)
ent_cad_prod_nome.bind('<Button-1>', Placeholder_cad_prod)

bt_log_prod.place(width=142, height=136, x=1138, y=676)
ent_cad_prod_nome.place(width=697, height=48, x=861, y=343)
ent_cad_prod_valor.place(width=697, height=48, x=861, y=476)
bt_voltar_pro.place(width=121, height=121, x=1441, y=51)
lb_bg_pro.pack()
#===============================
#frame_list_produto

lb_bg_list = Label(frame_list_pro, image=list_produto, bd=0)

bt_voltar_listpro = Button(frame_list_pro, image=voltar1, bd=0,  command=lambda: [frame_menu.pack(), frame_list_pro.forget(), delete()])
lb_lista_produto = Listbox(frame_list_pro, bd=0, foreground='black',justify=CENTER,font='Arial 50',selectbackground=laranja,selectforeground='white')
ent_nome_prod = Entry(frame_list_pro, font='Arial 30', bd=0)



def search():
    banco = Banco()
    a = ent_nome_prod.get()
    db = banco.listar_produtos(a)
    if a != '0':
        lb_lista_produto.insert(END, db)
    else:
        for y in range(len(banco.pls)):
            print(len(banco.pls))
            lb_lista_produto.insert(END, banco.pls[y])


bt_lista = Button(frame_list_pro, font='Arial 30', bd=0, image=bt_listar, command=search)


ent_nome_prod.place(width=418, height=87, x=126, y=407)

bt_lista.place(width=158, height=137, x=244, y=566)
lb_lista_produto.place(width=618, height=577, x=822, y=224)

bt_voltar_listpro.place(width=121, height=121, x=27, y=31)
lb_bg_list.pack()
#===============================
#frame_list_quarto
lb_bg_quart = Label(frame_list_qua, image=list_quarto, bd=0)
bt_voltar_quart = Button(frame_list_qua, image=voltar1, bd=0, command=lambda: [frame_menu.pack(), frame_list_qua.forget()])
lb_lista_quarto = Listbox(frame_list_qua, bd=0, foreground='black',justify=CENTER,font='Arial 50',selectbackground=laranja,selectforeground='white')

def search3():
    a = ''
    banco = Banco()
    db = banco.listar_produtos(a)
    if a != '':
        lb_lista_produto.insert(END, db)
    else:
        for y in range(len(banco.qua)):
            print(len(banco.qua))
            lb_lista_quarto.insert(END, banco.qua[y])

lb_lista_quarto.place(width=753, height=342, x=421, y=400)
bt_voltar_quart.place(width=121, height=121, x=27, y=31)
lb_bg_quart.pack()
#===============================
#frame_historico
lb_bg_hist = Label(frame_histori, image=historico, bd=0)
bt_voltar_hist = Button(frame_histori, image=voltar1, bd=0, command=lambda: [frame_menu.pack(), frame_histori.forget(), delete()])
ent_nome_hist = Entry(frame_histori, border=0, bg=cinza, font='Arial 20')
lb_historico = Listbox(frame_histori, bd=0, foreground='black',justify=CENTER,font='Arial 50',selectbackground=laranja,selectforeground='white')


def search2():
    banco = Banco()
    b = ent_nome_hist.get()
    db = banco.historico(b)
    if b != '':
        lb_historico.insert(END, db)
    else:
        for y in range(len(banco.qua)):
            print(len(banco.qua))
            lb_historico.insert(END, banco.qua[y])

log_bt_hist = Button(frame_histori, border=0, image=bt_listar, command=search2)

lb_historico.place(width=618, height=577, x=822, y=224)
ent_nome_hist.place(width=423, height=87, x=126, y=407)
log_bt_hist.place(width=158, height=137, x=244, y=566)
bt_voltar_hist.place(width=121, height=121, x=27, y=31)
lb_bg_hist.pack()
#===============================
#frame_logo
lb_bg_logo = Label(frame_logo, image=logo, bd=0)
lb_bg_logo.pack()
#===============================
win.mainloop()
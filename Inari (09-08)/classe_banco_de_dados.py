from tkinter import messagebox
import mysql.connector
from classe_cliente import *
from classe_produto import *

# Criação da classe banco
class Banco:
    def __init__(self):
        self.conexao = mysql.connector.connect( host='localhost', user='root', password='q1w2e3', database='hotel_inariv')
        self.mycursor = self.conexao.cursor()

        self.qua = []
        self.pls = []

    def cadastrar_cliente(self, nome, email, telefone): # Cadastrar cliente
        objeto = Cliente(nome, email, telefone)
        comando_sql = f'insert into Cliente (cliente_nome, cliente_email, cliente_telefone) value ("{objeto.nome}", "{objeto.email}", "{objeto.telefone}")'
        self.mycursor.execute(comando_sql)
        self.conexao.commit()
        messagebox.showwarning(f'Cliente cadastrado','Continuar')

    def cadastrar_produto(self, nome, valor): # Cadastrar produto
        objetoProduto = Produto(nome, valor)
        comando_sql = f'insert into Produto (produto_nome, produto_valor) value ("{objetoProduto.nome}", "{objetoProduto.valor}")'
        self.mycursor.execute(comando_sql)
        self.conexao.commit()
        messagebox.showwarning(f'Produto cadastrado','Continuar')

    def listar_quartos(self, modelo): # Listar todos os quartos
        if modelo == 1:
            comando_sql = f'select * from Quarto where quarto_modelo = "solteiro"'
            self.mycursor.execute(comando_sql)
            list = self.mycursor.fetchall()
            for i in list:
                print('', i)
        elif modelo == 2:
            comando_sql = f'select * from Quarto where quarto_modelo = "casal"'
            self.mycursor.execute(comando_sql)
            list = self.mycursor.fetchall()
            for i in list:
                print('', i)
        elif modelo == 0:
            comando_sql = f'select * from Quarto'
            self.mycursor.execute(comando_sql)
            list = self.mycursor.fetchall()
            for i in list:
                print('', i)
        else:
            print('Digite um valor válido')



    def listar_produtos(self, nome):
        
        if nome == '0':
            comando_sql = f'select * from  produto'
            self.mycursor.execute(comando_sql)
            lista = self.mycursor.fetchall()
            
            for i in lista:
                exib = (f' {i} ').replace(',', ' | ').replace("'", '♦').replace('(', '╠{').replace(')', '}╣')
                self.pls.append(exib)
        else:
            nom = str(nome)
            comando_sql = f'select * from Produto where produto_nome = "{nom}"'
            self.mycursor.execute(comando_sql)
            lista = self.mycursor.fetchall()
            for x in lista:
                exib = (f' {x} ').replace(',', ' | ').replace("'", '♦').replace('(', '╠{').replace(')', '}╣')
                
                print(exib)
                return exib


    def comprar_produtos(self, nomeQuarto, nomeProduto):
        comando_sql = f'select produto_valor from Produto where produto_nome = "{nomeProduto}"'
        self.mycursor.execute(comando_sql)
        list = self.mycursor.fetchall()
        for i in list:
            var1 = str(i)
            var1.replace(',', '')
            var2 = var1.replace('(', '')
            var3 = var2.replace(')', '')
            var4 = var3.replace(',', '')
            var5 = float(var4)
            comando_sql2 = f'insert into historico_compras (historico_quartoNome, historico_produtoNome, historico_produtoValor) value ("{nomeQuarto}", "{nomeProduto}", "{var5}")'
            self.mycursor.execute(comando_sql2)
            self.conexao.commit()
            messagebox.showwarning(f'Compra Realizada','Continuar')
        else:
            pass


    def ocupar_quarto(self, nomeCliente, idQuarto):
        comando_sql = f'select quarto_valor from Quarto where quarto_id = "{idQuarto}"'
        self.mycursor.execute(comando_sql)
        list = self.mycursor.fetchall()
        for i in list:
            var1 = str(i)
            var1.replace(',', '')
            var2 = var1.replace('(', '')
            var3 = var2.replace(')', '')
            var4 = var3.replace(',', '')
            var5 = float(var4)
            comando_sql = f'insert into ficha_quarto (ficha_nomeCliente, ficha_quartoId, ficha_quartoValor) value ("{nomeCliente}", "{idQuarto}", "{var5}")'
            self.mycursor.execute(comando_sql)
            self.conexao.commit()
            comando_sql2 = f'update Quarto set quarto_disponibilidade = "Indisponivel" where quarto_id = "{idQuarto}"'
            self.mycursor.execute(comando_sql2)
            self.conexao.commit()

    def desocupar_quarto(self, nomeCliente):
        comando_sql = f'select ficha_quartoValor from ficha_quarto where ficha_nomeCliente = "{nomeCliente}"'
        self.mycursor.execute(comando_sql)
        list = self.mycursor.fetchall()
        for i in list:
            var1 = str(i)
            var1.replace(',', '')
            var2 = var1.replace('(', '')
            var3 = var2.replace(')', '')
            var42 = var3.replace(',', '')
            var52 = float(var42)
            comando_sql1 = f'select historico_produtoValor from historico_compras where historico_quartoNome = "{nomeCliente}"'
            self.mycursor.execute(comando_sql1)
            list = self.mycursor.fetchall()
            soma = 0
            for i in list:
                var1 = str(i)
                var1.replace(',', '')
                var2 = var1.replace('(', '')
                var3 = var2.replace(')', '')
                var4 = var3.replace(',', '')
                var5 = float(var4)
                soma += var5
            print(f' Gasto total: {soma + var52}')

            comando_sql0 = f'select ficha_quartoId from ficha_quarto where ficha_nomeCliente = "{nomeCliente}"'
            self.mycursor.execute(comando_sql0)
            list = self.mycursor.fetchall()
            for i in list:
                var1 = str(i)
                var1.replace(',', '')
                var2 = var1.replace('(', '')
                var3 = var2.replace(')', '')
                var44 = var3.replace(',', '')
                varid = int(var44)

                comando_sql2 = f'update Quarto set quarto_disponibilidade = "Disponivel" where quarto_id = "{varid}"'
                self.mycursor.execute(comando_sql2)
                self.conexao.commit()
        
        def historico(self, nome_cli):
            if nome_cli == '0':
                comando_sql = f'select historico_produtoValor from historico_compras where historico_quartoNome = "{nome_cli}"'
                self.mycursor.execute(comando_sql)
                lista = self.mycursor.fetchall()
            
            for i in lista:
                exib = (f' {i} ').replace(',', ' | ').replace("'", '♦').replace('(', '╠{').replace(')', '}╣')
                self.pls.append(exib)
            else:
                nom = str(nome_cli)
                comando_sql = f'select * from Produto where produto_nome = "{nom}"'
                self.mycursor.execute(comando_sql)
                lista = self.mycursor.fetchall()
                for x in lista:
                    exib = (f' {x} ').replace(',', ' | ').replace("'", '♦').replace('(', '╠{').replace(')', '}╣')
                
            print(exib)
            return exib
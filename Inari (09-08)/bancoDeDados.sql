create database hotel_inariv;
use hotel_inariv;

create table Cliente(
cliente_id int auto_increment,
cliente_nome varchar(60),
cliente_email varchar(60),
cliente_telefone varchar(10),
primary key (cliente_id));

create table Produto(
produto_id int auto_increment,
produto_nome varchar(40),
produto_valor float,
primary key (produto_id));

create table Quarto(
quarto_id int auto_increment,
quarto_numero varchar(2),
quarto_modelo varchar(50),
quarto_valor float,
quarto_disponibilidade varchar(20),
primary key (quarto_id));

insert into Quarto (quarto_numero, quarto_modelo, quarto_valor, quarto_disponibilidade)
value ('01', 'solteiro', '200.00', 'Disponivel'), ('02', 'casal', '350.00', 'Disponivel'), 
('03', 'casal', '700.00', 'Disponivel'), ('04', 'solteiro', '450.00', 'Disponivel');

create table historico_compras(
historico_id int auto_increment,
historico_quartoNome varchar(60),
historico_produtoNome varchar(40),
historico_produtoValor float,
primary key (historico_id));

create table ficha_quarto(
ficha_id int auto_increment,
ficha_nomeCliente varchar(60),
ficha_quartoId int,
ficha_quartoValor float,
primary key (ficha_id));



select * from Cliente;
select * from Produto;
select * from Quarto;
select * from historico_compras;
select * from ficha_quarto;

#drop database hotel_inariv;
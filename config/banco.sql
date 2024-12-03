drop database biblioteca;
create database biblioteca;
use biblioteca;

create table usuario(
	id_usuario int auto_increment primary key,
	nome varchar(100),
	email varchar(255),
	cpf varchar(13),
	telefone varchar(20),
	admin boolean
);


create table livro(
    id_livro int auto_increment primary key,
    titulo varchar(50),
    autor varchar(50),
    genero varchar(50),
    status varchar(50),
    codigo int
    );

create table emprestimo(
    id_emprestimo int auto_increment primary key,
	titulo varchar(255),
	nome varchar(255)
);

insert into usuario values (1,'admin', 'enzo@gmail.com', 'admin', '991336910', true);
insert into livro values(1,'titulo', 'enzo', 'enzo', 'disponivel', 1);
select * from emprestimo;
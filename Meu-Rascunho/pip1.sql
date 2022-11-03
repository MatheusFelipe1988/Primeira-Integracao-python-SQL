create database pip1;
use pip1;
create table tbpessoas(
idpessoa int not null,
nomepessoa varchar(10),
idade varchar(10),
primary key(idpessoa)
);
INSERT INTO `pip1`.`tbpessoas` (`idpessoa`, `nomepessoa`, `idade`) VALUES ('1', 'matheus', '20');
INSERT INTO `pip1`.`tbpessoas` (`idpessoa`, `nomepessoa`, `idade`) VALUES ('2', 'matheuws', '21');

select * from tbpessoas;
use pip1;
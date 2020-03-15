create database bchirot
use bchirot
drop table Party 
create table Party(
code int identity(1,1),
nameParty nvarchar(25)not null,
charParty char not null

)
go

alter table Party(
code int identity(1,1),
nameParty nvarchar(25)not null,
charParty nvarchar(4) not null
)

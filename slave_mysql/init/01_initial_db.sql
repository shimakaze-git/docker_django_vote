create user 'repl'@'192.168.1.12' identified by 'test-password';
grant replication slave on *.* to 'repl'@'192.168.1.12';
create database hoge;

import sqlite3

banco = sqlite3.connect('db.sqlite3')

cursor = banco.cursor()
#cursor.execute("CREATE TABLE PESSOAS (NOME TEXT, IDADE INTEGER, EMAIL TEXT)")
#cursor.execute("INSERT INTO PESSOAS values ('MARIA', 40, 'MARIA@TESTE.COM')")
#banco.commit();
#cursor.execute("DROP TABLE Carteira ")
#cursor.execute("CREATE TABLE Carteira (ID Integer, nome_carteira TEXT)")
#cursor.execute("INSERT INTO Carteira values (1, 'CARTEIRA001')")
#banco.commit();

cursor.execute("select * from carteira")
print(cursor.fetchall())
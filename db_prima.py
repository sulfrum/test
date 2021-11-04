#!/usr/bin/env python3

import sqlite3


conn = sqlite3.connect('db_prima.db')

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS personaggi(nome text, hp_max integer, hp integer, mana_max integer, mana integer)")
c.execute("CREATE UNIQUE INDEX IF NOT EXISTS index_pg on personaggi(nome)")
c.execute("INSERT OR IGNORE INTO personaggi VALUES ('Piridina',100,100,90,80)")
c.execute("INSERT OR IGNORE INTO personaggi VALUES ('Piridina',100,100,90,80)")

conn.commit()

c.execute("CREATE TABLE IF NOT EXISTS mob(nome text, AI text, AU text, AE text, AO text)")
c.execute("CREATE UNIQUE INDEX IF NOT EXISTS index_mob on personaggi(nome)")
c.execute("INSERT OR IGNORE INTO mob VALUES ('Piridina',100,100,90,80)")
c.execute("INSERT OR IGNORE INTO mob VALUES ('Palone',100,100,90,80)")
c.execute("INSERT OR IGNORE INTO mob VALUES ('Ravoso',100,100,90,80)")
c.execute("INSERT OR IGNORE INTO mob VALUES ('Corazo',100,100,90,80)")
c.execute("INSERT OR IGNORE INTO mob VALUES ('Licto',100,100,90,80)")

conn.commit()

print("=== Pg  ===")
for riga in c.execute('SELECT * FROM Personaggi ORDER BY nome'):
            print(riga)

print("=== Mob ===")
for riga in c.execute('SELECT * FROM mob ORDER BY nome'):
            print(riga)

# Metodo sporco
symbol = 'Licto'
a=c.execute("SELECT * FROM mob WHERE nome = '%s'" % symbol)
print("== Select (sporco) ==")
print(a.fetchone())

# Metodo pulito
t = ('Licto',)
c.execute('SELECT * FROM mob WHERE nome=?', t)
print("== Select (pulito) ==")
print(c.fetchone())

# Inserimenti multipli puliti
mobbini = [('Giulio', 1, 1, 1, 1),
            ('Carlo', 2, 3, 1000, 72),
            ('Van', 1, 23, 500, 53),]

c.executemany('INSERT INTO mob VALUES (?,?,?,?,?)', mobbini)

print("=== Mob ===")
for riga in c.execute('SELECT * FROM mob ORDER BY nome'):
            print(riga)

conn.commit()
conn.close()

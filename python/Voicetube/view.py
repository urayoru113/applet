from sqlite import Database

vt = Database('voicetube.db')
vt.table = 'Sound_Euphonium'
vt.select()
print(vt.fetchall())

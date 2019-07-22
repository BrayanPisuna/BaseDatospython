import pymysql
import sys

bd=pymysql.connect(host='localhost',port=3306, user='root', passwd='', db='usuarios')
cur=bd.cursor()



cur.execute("INSERT INTO usuarios (Id, nombre, apellido, fisica, matematica, sociales, lenguaje) VALUES ('17243585','david','pisuña','5','7','8','7')")
			


bd.commit()
bd.close()
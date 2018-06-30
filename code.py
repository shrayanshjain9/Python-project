#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"

import cgi
import MySQLdb
data=cgi.FieldStorage()
name=data.getvalue('name')
#print name
fname=data.getvalue('fname')
gender=data.getvalue('a')
email=data.getvalue('email')
password=data.getvalue('password')
con=MySQLdb.connect("127.0.0.1","root","","project",3306)
query="insert into ipec(name,fname,gender,email,password) values ('"+name+"','"+fname+"','"+gender+"','"+email+"','"+password+"')"
cur=con.cursor()
cur.execute(query)
con.commit()
con.close()
print """
<script>
window.location.href='login.py'
</script>
"""










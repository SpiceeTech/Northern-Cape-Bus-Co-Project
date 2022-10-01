from django.shortcuts import render
from matplotlib.backend_bases import cursors
import mysql.connector as sql
fn=''
ln=''
pn=''
idnum=''
em=''
pwd=''
# Create your views here.

def home(request):
  return render(request, 'home.html')

def info(request):
  return render(request, 'info.html')

def about_us(request):
  return render(request, 'about-us.html')

def contact(request):
  return render(request, 'contacts.html')

def login(request):
  return render(request, 'login.html')

def registration(request):
  global fn, ln, pn, idnum, em, pwd
  if request.method=='post':
    m=sql.connect(host="localhost", user="root", password="Thato@1234", database='ncbuses_db')
    cursor=m.cursor()
    d=request.POST
    for key,value in d.items():
      if key=="name":
        fn=value
      if key=="surname":
        ln=value
      if key=="phone":
        pn=value
      if key=="id_no":
        idnum=value
      if key=="email":
        em=value
      if key=="password":
        pwd=value

    c="insert into Loyal_users Values('{}','{}','{}','{}','{}','{}')".format(fn,ln,idnum,pn,em,pwd)
    cursor.execute(c)
    m.commit()

  return render(request, 'registration.html')

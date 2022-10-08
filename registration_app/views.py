from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
pn=''
idnum=''
em=''
pwd=''
# Create your views here.
def registration(request):
    global fn,ln,pn,idnum,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Thato@1234",database='ncbuses_db')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="name":
                fn=value
            if key=="surname":
                ln=value
            if key=="phone":
                pn=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
            if key=="id_no":
                idnum=value
        
        c="insert into loyal_customerstbl Values('{}','{}','{}','{}','{}','{}')".format(fn,ln,idnum,pn,em,pwd)
        cursor.execute(c)
        m.commit()

    return render(request,'registration.html')
from django.shortcuts import render
import pymysql as MySQL
def index(request):
    return render(request,'index.html')
def admin_login(request):
    return render(request,"AdminLogin.html",{'msg':''})
def check_login(request):
    try:
        con = MySQL.connect(host='localhost', port=3306, user='root', passwd='1234', db='pms')
        smt = con.cursor()
        q = "select * from admin where adminid='{}' and password='{}'".format(request.POST['aid'],request.POST['pwd'])
        print(q)
        smt.execute(q)
        print(1)
        row = smt.fetchone()
        if(row):
            print(2)
            request.session['SES_ADMIN']=row
            print(3)
            return render(request, "AdminHome.html")
        else:
           
            return render(request, "AdminLogin.html", {'msg': 'Invalid Login Id/Password'})
        con.close()

    except Exception as e:
        print(e)
        return render(request, "AdminLogin.html", {'msg': e})
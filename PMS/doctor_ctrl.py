from django.shortcuts import render
import pymysql as MySQL

def doctor_login(request):
    return render(request,"DoctorLogin.html",{'msg':''})
def check_login(request):
    try:
        con = MySQL.connect(host='localhost', port=3306, user='root', passwd='1234', db='pms')
        smt = con.cursor()
        q = "select * from doctors where doctorid={} and password={}".format(request.POST['did'],request.POST['pwd'])
        smt.execute(q)
        row = smt.fetchone()
        con.close()
        if(row):
            request.session['SES_DOCTOR']=row
            return render(request, "DoctorHome.html")
        else:
            return render(request, "DoctorLogin.html", {'msg': 'Invalid Login Id/Password'})


    except Exception as e:
        return render(request, "DoctorLogin.html", {'msg': e})
def doctor_interface(request):
    try:
     rows=request.session['SES_ADMIN']
     return render(request,"Doctor.html",{'msg':''})
    except:
     return render(request, "AdminLogin.html", {'msg': ''})

def doctor_interface(request):
    try:
     rows=request.session['SES_ADMIN']
     return render(request,"Doctor.html",{'msg':''})
    except:
     return render(request, "AdminLogin.html", {'msg': ''})
def edit_doctor(request):
  try:
   con = MySQL.connect(host='localhost', port=3306, user='root', passwd='123', db='pms')
   print('connected')
   smt = con.cursor()

   btn=request.GET['btn']
   if btn=="Edit":
    dname=request.GET['dname']
    dob = request.GET['dob']
    gen = request.GET['gen']
    add = request.GET['add']
    state = request.GET['state']
    city = request.GET['city']
    hcity = request.GET['hcity']
    email = request.GET['email']
    mob = request.GET['mob']
    special = request.GET['special']
    degree = request.GET['degree']
    password = request.GET['pass']
    q="update doctors set doctorname='{}',dob='{}',gender='{}',address='{}',states='{}',city='{}',mobileno='{}',email='{}',hospitalcity='{}',specialization='{}',degrees='{}',password='{}'  where doctorid={}".format(dname,dob,gen,add,state,city,mob,email,hcity,special,degree,password,request.GET['did'])
    print(q)
    smt.execute(q)
    con.commit()
   elif btn=='Delete':
    q="delete from doctors where doctorid={}".format(request.GET['did'])
    smt.execute(q)
    con.commit()
   con.close()
  except Exception as e:
     print(e)
  return display_all(request)
def edit_picture(request):
 try:
  imgfile = request.FILES['img']

  con = MySQL.connect(host='localhost', port=3306, user='root', passwd='123', db='pms')
  print('connected')
  smt = con.cursor()
  q ="update doctors set image='{}' where doctorid={}".format(imgfile.name,request.POST['did'])
  print(q)
  smt.execute(q)
  con.commit()
  F = open("d:/PMS/asset/" + imgfile.name, "wb")
  for chunk in imgfile.chunks():
    F.write(chunk)
  F.close()

  con.close()
  return display_all(request)
 except Exception as e:
  return display_all(request)

def doctor_submit(request):
  try:
    dname=request.POST['dname']
    dob = request.POST['dob']
    gen = request.POST['gen']
    add = request.POST['add']
    state = request.POST['state']
    city = request.POST['city']
    hcity = request.POST['hcity']
    email = request.POST['email']
    mob = request.POST['mob']
    special = request.POST['special']
    degree = request.POST['degree']
    imgfile = request.FILES['img']
    password = request.POST['pass']
    con=MySQL.connect(host='localhost',port=3306,user='root',passwd='123',db='pms')
    print('connected')
    smt=con.cursor()
    q="insert into doctors(doctorname,dob,gender,address,states,city,mobileno,email,hospitalcity,specialization,degrees,password,image)values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(dname,dob,gen,add,state,city,mob,email,hcity,special,degree,password,imgfile.name)
    print(q)
    smt.execute(q)
    con.commit()
    F=open("d:/PMS/asset/"+imgfile.name,"wb")
    for chunk in imgfile.chunks():
      F.write(chunk)
    F.close()

    con.close()
    return render(request, "Doctor.html",{'msg':'Record Submitted'})
  except Exception as e:
    return render(request, "Doctor.html", {'msg': e})


def display_all(request):
  try:
    con = MySQL.connect(host='localhost', port=3306, user='root', passwd='123', db='pms')
    smt = con.cursor()
    q="select * from doctors"
    smt.execute(q)
    rows=smt.fetchall()
    con.close()
    return render(request, "DoctorDisplayAll.html", {'rows': rows})
  except Exception as e:
    return render(request, "DoctorDisplayAll.html", {'rows':None})

def display_by_id(request):
  try:
    con = MySQL.connect(host='localhost', port=3306, user='root', passwd='123', db='pms')
    smt = con.cursor()
    q="select * from doctors where doctorid={}".format(request.GET['id'])
    smt.execute(q)
    row=smt.fetchone()
    con.close()
    return render(request, "DoctorDisplayByID.html", {'row': row})
  except Exception as e:
    return render(request, "DoctorDisplayByID.html", {'row':None})

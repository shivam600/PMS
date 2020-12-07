from django.shortcuts import render
import pymysql as MySQL
def patient_interface(request):
     rows=fetchAllDoctors()
     return render(request,"patient.html",{'msg':'','rows':rows})

def fetchAllDoctors():
    try:
        con = MySQL.connect(host='localhost', port=3306, user='root', passwd='1234', db='pms')
        smt = con.cursor()
        q = "select * from doctors"
        smt.execute(q)
        rows = smt.fetchall()
        con.close()
        return rows
    except Exception as e:
        return (None)



def edit_patient(request):
  try:
   con = MySQL.connect(host='localhost', port=3306, user='root', passwd='123', db='pms')
   print('connected')
   smt = con.cursor()

   btn=request.GET['btn']
   if btn=="Edit":
       pname = request.GET['pname']
       dob = request.GET['dob']
       gen = request.GET['gen']
       add = request.GET['add']
       state = request.GET['state']
       city = request.GET['city']
       email = request.GET['email']
       mobile = request.GET['mob']
       admitfor = request.GET['admitfor']
       bloodgroup = request.GET['bloodgroup']
       admittime = request.GET['admittime']
       rn = request.GET['room_no']
       bn = request.GET['bed_no']
       status = request.GET['status']
       password = request.GET['password']

       q="update patient set patientname='{}',dob='{}',gender='{}',address='{}',states='{}',city='{}',email='{}',mobileno='{}',admitfor='{}',bloodgroup='{}',admittime='{}',room_no='{}',bed_no='{}',password='{}'  where patientid={}".format(pname,dob,gen,add,state,city,email,mobile,admitfor,bloodgroup,admittime,rn,bn,status,password,request.GET['did'])
       print(q)
       smt.execute(q)
       con.commit()
   elif btn=='Delete':
    q="delete from patients where patientid={}".format(request.GET['did'])
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


def patient_submit(request):
  try:
    did=request.POST['did']
    pname=request.POST['pname']
    dob = request.POST['dob']
    gen = request.POST['gen']
    add = request.POST['add']
    state = request.POST['state']
    city = request.POST['city']
    email = request.POST['email']
    mob = request.POST['mob']
    admitfor = request.POST['admitfor']
    bloodgroup = request.POST['sym']
    admittime = request.POST['time']
    rn = request.POST['roomno']
    bn = request.POST['badno']
    status = request.POST['status']
    imgfile = request.FILES['image']
    password = request.POST['password']
    con=MySQL.connect(host='localhost',port=3306,user='root',passwd='123',db='pms')
    print('connected')
    smt=con.cursor()
    q="insert into patients(doctorsid,patientname,dob,gender,address,states,city,email,mobileno,admitfor,bloodgroup,admittime,roomno,bedno,status,password,image)values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(did,pname,dob,gen,add,state,city,email,mob,admitfor,bloodgroup,admittime,rn,bn,status,password,imgfile.name)
    print(q)
    smt.execute(q)
    con.commit()
    F = open("d:/PMS/asset/" + imgfile.name, "wb")
    for chunk in imgfile.chunks():
        F.write(chunk)
    F.close()
    con.close()
    rows=fetchAllDoctors()
    return render(request, "Patient.html", {'msg': 'Record Submitted','rows':rows})
  except Exception as e:
      return render(request, "Patient.html", {'msg': e,'rows':None})

def display_all(request):
  try:
    con = MySQL.connect(host='localhost', port=3306, user='root', passwd='123', db='pms')
    smt = con.cursor()
    q="select * from patients"
    smt.execute(q)
    rows=smt.fetchall()
    con.close()
    return render(request, "PatientDisplayAll.html", {'rows': rows})
  except Exception as e:
    return render(request, "PatientDisplayAll.html", {'rows':None})

def search_patient(request):
    return render(request,"SearchPatient.html",{'msg':''})
    
def display_by_id(request):
  try:
    con = MySQL.connect(host='localhost', port=3306, user='root', passwd='123', db='pms')
    smt = con.cursor()
    q="select * from patient where patientid={}".format(request.GET['id'])
    smt.execute(q)
    row=smt.fetchone()
    con.close()
    return render(request, "PatientDisplayById.html", {'row': row})
  except Exception as e:
    return render(request, "PatientDisplayById.html", {'row':None})





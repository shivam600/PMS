from django.shortcuts import render
import pymysql as MySQL
def fetchAllPatient():
    try:
        con = MySQL.connect(host='localhost', port=3306, user='root', passwd='1234', db='pms')
        smt = con.cursor()
        q = "select * from patients"
        smt.execute(q)
        rows = smt.fetchall()
        con.close()
        return rows
    except Exception as e:
        return (None)
def dailyreport_interface(request):
  try:
      rows=fetchAllPatient()
      return render(request, "DailyReport.html",  {'msg':'','rows':rows})
  except Exception as e:
      return render(request, "DailyReport.html", {'msg': e})

def dailyreport_submit(request):
  try:
      did = request.POST['did']
      pid = request.POST['pid']
      date = request.POST['date']
      time = request.POST['time']
      temp = request.POST['temp']
      bp = request.POST['bp']
      ecg = request.POST['ecg']
      con = MySQL.connect(host='localhost', port=3306, user='root', passwd='123', db='pms')
      print('connected')
      smt = con.cursor()
      q = "insert into dailyreport(doctorid,patientid,currentdate,currenttime,temprature,bloodpressure,ecgstatus)values({},{},'{}','{}','{}','{}','{}')".format(did,pid,date,time,temp,bp,ecg)
      print(q)
      smt.execute(q)
      con.commit()
      con.close()
      return render(request, "DailyReport.html", {'msg': 'Record Submitted'})

  except Exception as e:
      return render(request, "DailyReport.html", {'msg': e})



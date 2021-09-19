from flask import session, Flask, url_for, request, current_app
import random
import string
from datetime import date
import datetime
import mysql.connector
from apart.models import *
import flask
from django.contrib import messages
import os
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.contrib.auth import get_user_model, authenticate, login, logout
User = get_user_model()

app = Flask(__name__)
app.secret_key = "secret!!!"

with app.app_context():
    # within this block, current_app points to app.
    print('current_app.name')

# Create your views here.


def loginView(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        authUser = authenticate(
            username=username,
            password=password,
        )
        if authUser is not None:
            login(request, authUser)
            if username == "ad123":
                return render(request, 'approve.html')
            if username == "secretary":
                return render(request, 'Secretary.html')
            if username == "president":
                return render(request, 'President.html')
            if username == "treasure":
                return render(request, 'Treasurer.html')
            return render(request, 'welcome.html')
        else:
            messages.error(request, 'Invalid Credentials')
        return render(request, 'login.html')
    return render(request, 'login.html')


def register(request):
    u = User()
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == "POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        createNewUser = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
        )
        createNewUser.save()
        return redirect('/')
    return render(request, 'register.html')


def logoutView(request):
    logout(request)
    return redirect('/login/')


def landing(request):
    return render(request, 'landingpage.html')


def flatin(request):
    return render(request, 'flatin.html')


def financial(request):
    return render(request, 'financial.html')


def viewmaintain(request):
    return render(request, 'viewmaintain.html')


def Welcome(request):
    wel = homowner.objects.all()
    return render(request, 'welcome.html', {"homowner": wel})


def duespayment(request):
    return render(request, 'duespayment.html')


def incexp(request):
    return render(request, 'incExp.html')


def payment(request):
    return render(request, 'payment.html')


# def complaint(request):
 #   return render(request, 'complaint.html')


def compt(request):
    return render(request, 'compt.html')


def aprove(request):
    return render(request, 'approve.html')


def secret(request):
    return render(request, 'Secretary.html')


def Sviewcomp(request):
    return render(request, 'secretaryViewComplaint.html')


def userprof(request):
    return render(request, 'newProfile.html')
# def  financestat(request):
 #   return render(request,'financialStatus.html')


def viewmain(request):
    return render(request, 'viewMaintenance.html')


def viewcomp(request):
    viw = compaint.objects.all()
    return render(request, 'viewComplaint.html', {"compaint": viw})


def createNot(request):
    return render(request, 'createNotice.html')


def presi(request):
    return render(request, 'President.html')


def flatowninfo(request):
    results = homowner.objects.all()
    return render(request, 'flatOwnerInfo.html', {"homowner": results})


def apprnoti(request):
    return render(request, 'approveNotice.html')


def homeuser(request):
    return render(request, 'homeOwnerDet.html')


def treasure(request):
    return render(request, 'Treasurer.html')


def homedetails(request):
    return render(request, 'home details.html')


def Addresd(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phono = request.POST.get('Phone Number')
        flat = request.POST.get('Flat No')
        emailid = request.POST.get('Email Id')
        Type = request.POST.get('type')
        homowner.objects.create(
            name=name,
            phono=phono,
            flat=flat,
            emailid=emailid,
            Type=Type,
        )

    return render(request, 'addresd.html')


def AddExpense(request):
    if request.method == "POST":
        category = request.POST.get('category')
        company = request.POST.get('Company')
        amount = request.POST.get('Amount')
        tranid = request.POST.get('Tranid')
        bildate = request.POST.get('bildate')
        expense.objects.create(
            category=category,
            company=company,
            amount=amount,
            tranid=tranid,
            bildate=bildate,
        )

    return render(request, 'addexpense.html')


def Apartment(request):
    if request.method == "POST":
        aptno = request.POST.get('aptno')
        area = request.POST.get('area')
        Bathroom = request.POST.get('Bathroom')
        Bedroom = request.POST.get('Bedroom')
        parking = request.POST.get('Parking')
        regMonth = request.POST.get('regMonth')
        apartment.objects.create(
            aptno=aptno,
            area=area,
            Bathroom=Bathroom,
            Bedroom=Bedroom,
            parking=parking,
            regMonth=regMonth,
        )

    return render(request, 'newProfile.html')


def AddIncome(request):
    if request.method == "POST":
        typeo = request.POST.get('typeo')
        payer = request.POST.get('payer')
        amount = request.POST.get('Amount')
        tranid = request.POST.get('Tranid')
        bildate = request.POST.get('bildate')
        income.objects.create(
            typeo=typeo,
            payer=payer,
            amount=amount,
            tranid=tranid,
            bildate=bildate,
        )

    return render(request, 'addincome.html')


def Addcomplaint(request):
    if request.method == "POST":
        uid = request.POST.get('uid')
        category = request.POST.get('category')
        reason = request.POST.get('reason')
        dt = request.POST.get('dt')

        compaint.objects.create(
            uid=uid,
            category=category,
            reason=reason,
            dt=dt,

        )

    return render(request, 'complaint.html')


def paymain(request):
    if request.method == "POST":
        usid = request.POST.get('usid')
        mon = request.POST.get('mon')
        trans = request.POST.get('trans')
        amount = request.POST.get('amount')
        Maint.objects.create(
            usid=usid,
            mon=mon,
            trans=trans,
            amount=amount,
        )
    return render(request, 'payMaintainance.html')


def financialStatus(request):

    conn = mysql.connector.connect(
        user='root', host='localhost', port='3306', password='', db="Apartmang")
    myquery = conn.cursor()

    myquery.execute(
        "SELECT typeo, SUM(amount) FROM apart_income GROUP BY typeo")

    income = "<table width='300px' cellpadding='5'>\n<tr>\n<th><center>Type</center></th>\n<th><center>Amount</center></th>\n</tr>\n"
    incTot = 0

    for row in myquery:
        income += "<tr>\n<td><center>" + \
            str(row[0])+"</center></td>\n<td><center>&#8377; " + \
            str(row[1])+"</center></td>\n</tr>\n"
        incTot += row[1]

    income += "<tr>\n<th><center>Total</center></th>\n<th><center>&#8377; " + \
        str(incTot)+"</center></th>\n</tr>\n</table>"

    myquery.execute(
        "SELECT category, SUM(amount) FROM apart_expense GROUP BY category")

    expense = "<table width='300px' cellpadding='5'>\n<tr>\n<th><center>Category</center></th>\n<th><center>Amount</center></th>\n</tr>\n"
    expTot = 0

    for row in myquery:
        expense += "<tr>\n<td><center>" + \
            str(row[0])+"</center></td>\n<td><center>&#8377; " + \
            str(row[1])+"</center></td>\n</tr>\n"
        expTot += row[1]

    expense += "<tr>\n<th><center>Total</center></th>\n<th><center>&#8377; " + \
        str(expTot)+"</center></th>\n</tr>\n</table>"

    finStat = "<strong>Net balance amount: &#8377; " + \
        str(incTot - expTot)+"</strong>"

    return render(request, 'financialStatus.html', {"income": income, "expense": expense, "finStat": finStat})


def viewIncomeExpenditure(request):

    today = datetime.datetime.now()
    mon = today.month

    conn = mysql.connector.connect(
        user='root', host='localhost', port='3306', password='', db="Apartmang")
    myquery = conn.cursor()

    myquery.execute(
        "SELECT typeo, SUM(amount) FROM apart_income WHERE month(bildate)="+str(mon)+" GROUP BY typeo")

    income = "<table width='300px' cellpadding='5'>\n<tr>\n<th><center>Type</center></th>\n<th><center>Amount</center></th>\n</tr>\n"
    incTot = 0

    for row in myquery:
        income += "<tr>\n<td><center>" + \
            str(row[0])+"</center></td>\n<td><center>&#8377; " + \
            str(row[1])+"</center></td>\n</tr>\n"
        incTot += row[1]

    income += "<tr>\n<th><center>Total</center></th>\n<th><center>&#8377; " + \
        str(incTot)+"</center></th>\n</tr>\n</table>"

    myquery.execute(
        "SELECT category, SUM(amount) FROM apart_expense WHERE month(bildate)="+str(mon)+" GROUP BY category")

    expense = "<table width='300px' cellpadding='5'>\n<tr>\n<th><center>Category</center></th>\n<th><center>Amount</center></th>\n</tr>\n"
    expTot = 0

    for row in myquery:
        expense += "<tr>\n<td><center>" + \
            str(row[0])+"</center></td>\n<td><center>&#8377; " + \
            str(row[1])+"</center></td>\n</tr>\n"
        expTot += row[1]

    expense += "<tr>\n<th><center>Total</center></th>\n<th><center>&#8377; " + \
        str(expTot)+"</center></th>\n</tr>\n</table>"

    monthNet = "<strong>Net income this month: &#8377; " + \
        str(incTot - expTot)+"</strong>"

    return render(request, 'incExp.html', {"income": income, "expense": expense, "monthNet": monthNet})


def AddDetails(request):
    if request.method == "POST":
        flatNo = request.POST.get('flatNo')
        name = request.POST.get('name')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        occupation = request.POST.get('occupation')
        comm_address = request.POST.get('comm_address')
        perm_address = request.POST.get('perm_address')
        idproof = request.POST.get('idproof')
        CommAddProof = request.POST.get('CommAddProof')
        PermAddProof = request.POST.get('PermAddProof')
        SaleDeed = request.POST.get('SaleDeed')
        homowndet.objects.create(
            flatNo=flatNo,
            name=name,
            email=email,
            dob=dob,
            occupation=occupation,
            comm_address=comm_address,
            perm_address=perm_address,
            idproof=idproof,
            CommAddProof=CommAddProof,
            PermAddProof=PermAddProof,
            SaleDeed=SaleDeed,
        )
    return render(request, 'home details.html')


def uploadHomeOwnIdProof(request):
    if 'user' in session:
        uid = session['user']
    else:
        return redirect(url_for('login'))

    if request.method == 'POST':
        photo = request.files['photoFile']

        i = 0
        while (True):
            fname = "templates/static"
            if not os.path.exists(fname):
                break
            i += 1

        photo.save(fname)

        conn = mysql.connector.connect(
            user='root', host='localhost', port='3306', password='', db="Apartmang")

        conn.execute("UPDATE homowndet SET idproof='/" +
                     fname+"' WHERE flatNo='"+uid+"'")
        conn.commit()
        conn.close()

        return render(request, 'home details.html')

    return "oops"


def payment(request):

    aptno = request.user

    today = datetime.datetime.now()
    month = today.month

    conn = mysql.connector.connect(
        user='root', host='localhost', port='3306', password='', db="Apartmang")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM apart_apartment WHERE aptno='"+str(aptno)+"'")
    res = cursor.fetchall()

    regMonth = 8

    maintAmt = 1300
    cursor.execute(
        "SELECT * FROM apart_apartment WHERE aptno='"+str(aptno)+"'")

    cursor = cursor.fetchall()

    if len(cursor) != 0:
        lastMonth = month - 1

    else:
        lastMonth = regMonth - 1

    toPay = month - lastMonth

    if toPay > 0:
        payDet = "You need to <strong>pay</strong> maintenance for <strong>" + \
            str(toPay) + " months</strong>."
    elif toPay == 0:
        payDet = "Your maintenance payment is <strong>settled up!</strong>"
    else:
        payDet = "You have paid maintenance for <strong>" + \
            str(-1 * toPay) + " months</strong> in <strong>advance</strong>."

    return render(request, 'payment.html', {"user": aptno, "payDet": payDet, "maintAmt": maintAmt})


def makePayment(request):
    uid = request.user

    today = datetime.datetime.now()
    month = today.month

    months = int(month)
    try:
        conn = mysql.connector.connect(
            user='root', host='localhost', port='3306', password='', db="Apartmang")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM apart_apartment WHERE aptno='"+uid+"'")
        cursor = cursor.fetchall()
        regMonth = (cursor[0][6])
        print(regMonth)
        maintAmt = 1300
        cursor.execute("SELECT * FROM apart_maint WHERE usid='"+uid+"'")
        cursor = cursor.fetchall()
        if len(cursor) != 0:
            lastMonth = cursor[-1][0]
        else:
            lastMonth = regMonth - 1
        tranLength = 10
        tran_characters = string.ascii_letters + string.digits
        tranNum = ''.join(random.choice(tran_characters)
                          for i in range(tranLength))

        totPayment = months * maintAmt

        today = datetime.datetime.now()
        year = today.year
        month = today.month
        monthNum = (year - 1970) * 12 + month

        for i in range(months):
            lastMonth += 1

            cursor.execute("INSERT INTO apart_maint"+uid.replace("-", "_").replace("/", "_") +
                           " VALUES ("+str(lastMonth)+", '"+tranNum+"', "+str(maintAmt)+"),"+str(uid)+"")
            cursor.execute("INSERT INTO apart_income (typeo, payer, amount,bildate) VALUES ('Maintenance','" +
                           uid + "', " + str(totPayment) + ",  " + str(monthNum) + ")")

        conn.commit()
        conn.close()

        return tranNum

    except Exception as e:

        print(e)

        return "failure"


def duespayment(request):
    uid = request.user

    conn = mysql.connector.connect(
        user='root', host='localhost', port='3306', password='', db="Apartmang")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM apart_apartment WHERE aptno='"+str(uid)+"'")
    cursor = cursor.fetchall()

    today = datetime.datetime.now()
    month = today.month

    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

    cursor1 = conn.cursor()
    cursor1.execute("SELECT * FROM apart_maint WHERE usid='"+str(uid)+"'")
    cursor1 = cursor1.fetchall()
    regMonth = 8
    if len(cursor1) != 0:
        lastMonth = cursor1[-1][0]

    else:
        lastMonth = int(regMonth) - 1

    toPay = month - lastMonth

    income = "<table width='300px' cellpadding='5'>\n<tr>\n<th><center>Month</center></th>\n<th><center>Transaction Id</center></th>\n<th><center>amount</center></th>\n</tr>\n"

    incTot = 0

    for row in cursor1:
        y = row[0] // 12 + 1970
        m = row[0] % 12
        if m == 0:
            m = 12
            y -= 1
        income += "<tr>\n<td><center>"+str(months[m-1])+"</center></td>\n<td><center>"+str(
            row[2])+"</center></td>\n<td><center>&#8377; "+str(row[3])+"</center></td>\n</tr>\n"

    income += "</table>"
    if toPay > 0:
        payDet = "You need to <strong>pay</strong> maintenance for <strong>" + \
            str(toPay) + " months</strong>."
    elif toPay == 0:
        payDet = "Your maintenance payment is <strong>settled up!</strong>"
    else:
        payDet = "You have paid maintenance for <strong>" + \
            str(-1 * toPay) + " months</strong> in <strong>advance</strong>."

    return render(request, 'duespayment.html', {"income": income, "payDet": payDet})


def viewMaintenance(request):

    today = datetime.datetime.now()
    month = today.month
    conn = mysql.connector.connect(
        user='root', host='localhost', port='3306', password='', db="Apartmang")
    cursor = conn.cursor(buffered=True)
    cursor.execute("SELECT COUNT(aptno) FROM apart_apartment")
    cur = cursor.fetchall()
    print(cur)
    totApts = cur
    maintDets = "<table width='500px' cellpadding='5'>\n<tr>\n<th><center>Apartment</center></th>\n<th><center>Status</center></th>\n</tr>\n"

    cursor.execute("SELECT aptno FROM apart_apartment")
    cur1 = cursor.fetchall()
    totPaid = 0

    for row in cur1:
        aptNo = row[0]

        maintDets += "<tr>\n<td><center>"+aptNo+"</center></td>\n"
        cursor2 = conn.cursor()
        cursor2.execute(
            "SELECT * FROM apart_apartment WHERE aptNo='"+aptNo+"'")
        cursor2 = cursor2.fetchall()

        regMonth = cursor2[0][6]
        print(regMonth)
        maintAmt = 1300
        cursor3 = conn.cursor()
        cursor.execute("SELECT * FROM apart_maint")

        cursor3 = cursor.fetchall()

        print(cursor3)
        if len(cursor3) != 0:
            lastMonth = cursor3[-1][0]
        else:
            lastMonth = regMonth - 1
        toPay = month - lastMonth

        paid = toPay * maintAmt * -1

        totPaid += paid

        if toPay > 0:
            maintDets += "<td style='color: red'><center>Dues: " + \
                str(toPay) + " months (&#8377; "+str(paid)+"/-)</center></td>\n"
        elif toPay == 0:
            maintDets += "<td style='color: blue'><center>Settled up</center></td>\n"
        else:
            maintDets += "<td style='color: green'><center>Advance payment: " + \
                str(-1 * toPay) + " months (&#8377; " + \
                str(paid)+"/-)</center></td>\n"

        maintDets += "</tr>\n"

    maintDets += "</table>\n<br><br>\n"

    if totPaid < 0:
        maintDets += "<strong style='color: red'>Total: &#8377; " + \
            str(totPaid)+"/-</strong>"
    elif totPaid == 0:
        maintDets += "<strong style='color: blue'>Total: &#8377; " + \
            str(totPaid)+"/-</strong>"
    else:
        maintDets += "<strong style='color: green'>Total: &#8377; " + \
            str(totPaid)+"/-</strong>"

    return render(request, 'viewMaintenance.html', {"totApts": totApts, "maintDets": maintDets})

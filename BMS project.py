#BMS---> banking mangement system
import mysql.connector
mydb=mysql.connector.connect(
                             host='localhost',
                             user='root',
                             password='Himanshu',
                             database='bank1'
                             )


def openacc():
    name=input('Enter The Customer Name:')
    accno=input('Enter The Ac/No:')
    dob=input('Enter The DOB:')
    address=input('Enter The Address:')
    contact=int(input('Enter The Contact No:'))
    openbal=int(input('Enter The Balance:'))

    data=(name,accno,dob,address,contact,openbal)
    sql=('insert into account values(%s,%s,%s,%s,%s,%s)')
    data1=(name,accno,openbal)
    sql1=('insert into amount values(%s,%s,%s)')
    

     
    x=mydb.cursor()
    x.execute(sql,data)
    x.execute(sql1,data1)
    mydb.commit()
    print('Data Enter Successfully')
    main()

def depoamo():
    amount=input('Enter The Amount You Want To Deposit:')
    ac=input('Enter The Acc No:')
    a='select bal from amount where accno=%s'
    data=(ac,)

    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[0]+int(amount)
    sql=('update amount set bal=%s where accno=%s')
    d=(t,ac)
    x.execute(sql,d)
    mydb.commit()
    main()
    
def withamo():
    amount=input('Enter The Amount You Want To  Withdraw:')
    ac=input('Enter The Acc No:')
    a='select bal from amount where accno=%s'
    data=(ac,)

    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[0]-int(amount)
    sql=('update amount set bal=%s where accno=%s')
    d=(t,ac)
    x.execute(sql,d)
    mydb.commit()
    main()

def balenq():
    ac=input('Enter The Acc No:')
    a='select bal from amount where accno=%s'
    data=(ac,)

    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    print("Balance For Account No :",ac,"Is",result[0])
    main()

def disdetails():
    ac=input('Enter The Acc No:')
    a='select *from account where accno=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    print(result)
    main()

def closeacc():
     ac=input('Enter The Acc No:')
     sql="delete from account where accno=%s"
     sql1="delete from amount where accno=%s"
     data=(ac,)
     x=mydb.cursor()
     x.execute(sql,data)
     x.execute(sql1,data)
     mydb.commit()
     main()




    
def main():
        print('''
            1.Open New Account
            2.Deposite Amount
            3.Withdraw Amount
            4.Balance Enquiry
            5.Display Customer Details
            6.Close An Account''')
        choice=input('Enter The Task You Want To Perform:')
        if(choice=='1'):
            openacc()
        elif(choice=='2'):
            depoamo()
        elif(choice=='3'):
            withamo()
        elif(choice=='4'):
            balenq()
        elif(choice=='5'):
            disdetails()
        elif(choice=='6'):
            closeacc()
        else:
            print('invalid choice......')
            main()
            
main()

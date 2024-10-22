

import mysql.connector as mycon
from datetime import date
mydb=mycon.connect(host='localhost', user='root', passwd='1234567890')
mycur=mydb.cursor()
def create():
 mycur.execute('create database project')
 mycur.execute('use project')
 sqlstmt='CREATE TABLE customer(acno int auto_increment primary key,name char(30) DEFAULT NULL,pin int not null,address varchar(100) DEFAULT NULL,phone varchar(15) DEFAULT NULL,email varchar(80) DEFAULT NULL,aadhar_no varchar(20) DEFAULT NULL,acc_type varchar(20) DEFAULT NULL,status char(15) DEFAULT NULL,balance int DEFAULT NULL)'
 mycur.execute(sqlstmt)
 sqlstmt='create table transaction(tid int auto_increment primary key ,dot date ,amount int(11) ,type char(15),acno int(11),Index(acno),FOREIGN KEY(acno) REFERENCES customer (acno) on update cascade on delete cascade)ENGINE = INNODB;'
 mycur.execute(sqlstmt)
 mydb.commit()
 
def main_menu():
 while True:
  print('_'*70)
  print()
  a='Welcome to "UNITED ARYAN BANK" '
  print(a.center(70))
  print('_'*70)
  print("*"*70)
  b='\t\t1. Open a new account'
  c='\t\t2. Modify account'
  d='\t\t3. Close account'
  e='\t\t4. Make transaction'
  j='\t\t5. Search account '
  f='\t\t6. Bank report '
  q='\t\t7. Exit/Quit'
  print(b.ljust(40))
  print(c.ljust(40))
  print(d.ljust(40))
  print(e.ljust(40))
  print(j.ljust(40))
  print(f.ljust(40))
  print(q.ljust(40))
  print("*"*70)
  print('_'*70)
  choice = int(input("Select your choice number from the above menu:"))
  if choice == 1:
   add_account()
  if choice == 2:
   modify_account()
  if choice == 3:
   close_account()
  if choice ==4 :
   transaction_menu()
  if choice ==5 :
   search_menu()
  if choice == 6:
   report_menu()
  if choice ==7 :
   print()
   print('THANKS FOR VISIT')
   print('VISIT AGAIN')
   print('HAVE A NICE DAY')
   break
 
def add_account():
 
 mycur.execute('use project')
 name = input('Enter Name :')
 addr = input('Enter address ')
 phone = input('Enter Phone no :')
 email = input('Enter Email :')
 aadhar = input('Enter AAdhar no :')
 actype = input('Account Type (saving/current ) :')
 balance = int(input('Enter opening balance :'))
 pin = int(input('Enter pin'))
 data=(name,addr,phone,email,aadhar,actype,'active',balance,pin)
 sql = 'insert into customer(name,address,phone,email,aadhar_no,acc_type,status,balance,pin) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
 mycur.execute(sql,data)
 mydb.commit()
 print('New customer added successfully')
 sql = 'select acno from customer where pin="'+ str(pin)+'";'
 mycur.execute(sql)
 records = mycur.fetchall()
 x=records[0][0]
 print()
 print('Your account number is',x)
 
def modify_account():
 mycur.execute('use project')
 acno = input('Enter customer Account No :')
 print('Modify screen ')
 print('\n 1. Customer Name')

 print('\n 2. Customer Address')
 print('\n 3. Customer Phone No')
 print('\n 4. Customer Email ID')
 print('\n 5. Customer Pin')
 choice = int(input('What do you want to change ? '))
 
 field_name=''
 if choice == 1:
  field_name ='name'
 if choice == 2:
  field_name = 'address'
 if choice == 3:
  field_name = 'phone'
 if choice == 4:
  field_name = 'email'
 if choice == 5:
  x=input('Enter your pin')
  y=[(int(x),)]
  sql = 'select pin from customer where acno="'+ str(acno)+'";'
  mycur.execute(sql)
  records = mycur.fetchall()
 if y==records:
  field_name = 'pin'
 else:
  print('Invalid pin')
  new_data = input('Enter New value :')
  sql ='update customer set ' + field_name + '="'+ new_data +'" where acno='+acno+';'
  mycur.execute(sql)
  mydb.commit()
  print('Customer Information modified..')
 
def close_account():
 mycur.execute('use project')
 acno = input('Enter customer Account No :')
 sql ='update customer set status="close" where acno ='+acno+';'
 mycur.execute(sql)
 mydb.commit()
 print('Account closed')
def report_menu():
 while True:
  print(' Report Menu')
  print("\n1. Daily Report")
  print('\n2. Monthly Report')
  print('\n3. Account Details')
  print('\n4. Back to Main Menu')
  choice = int(input('Enter your choice ...: '))
  if choice == 1:
   daily_report()
  if choice == 2:
   monthly_report()
  if choice == 3:
   account_details()
  if choice == 4:
   break
def daily_report():
 today = date.today()
 mycur.execute('use project')
 sql = 'select tid,dot,amount,type,acno from transaction t where dot="'+ str(today)+'";'
 mycur.execute(sql)
 records = mycur.fetchall()
 print('Daily Report :',today)
 print('-'*120)
 q,w,i,k,a='Transaction id','date of transaction','Amount','Type','Account number'
 print(q.center(20),end='')
 print(w.center(20),end='')
 print(i.center(20),end='')
 print(k.center(20),end='')
 print(a.center(20))
 print()
 for record in records:
  print(str(record[0]).center(20),end='')
  print(str(record[1]).center(20),end='')
  print(str(record[2]).center(20),end='')
  print(str(record[3]).center(20),end='')
  print(str(record[4]).center(20),end='')
  print()
  print('-'*120)
  
 wait = input('\n\n\n Press any key to continue....')
 mydb.commit()
def monthly_report():
 mycur.execute('use project')
 today = date.today()
 sql = 'select tid,dot,amount,type,acno from transaction t where month(dot)="' + str(today).split('-')[1]+'";'
 mycur.execute(sql)
 records = mycur.fetchall()
 print('-'*120)
 q,w,i,k,a='Transaction id','date of transaction','Amount','Type','Account number'
 print(q.center(20),end='')
 print(w.center(20),end='')
 print(i.center(20),end='')
 print(k.center(20),end='')
 print(a.center(20))
 print()
 for record in records:

  print(str(record[0]).center(20),end='')
  print(str(record[1]).center(20),end='')
  print(str(record[2]).center(20),end='')
  print(str(record[3]).center(20),end='')
  print(str(record[4]).center(20),end='')
  print()
  print('-'*120)
 mydb.commit()
 wait = input('\n\n\n Press any key to continue....')
def account_details():
 acno = input('Enter account no :')
 mycur.execute('use project')
 sql ='select * from customer where acno ='+acno+';'
 sql1 = 'select tid,dot,amount,type from transaction t where t.acno='+acno+';'
 mycur.execute(sql)
 result = mycur.fetchone()
 print('\t\t\tAccount Details')
 print('-'*120)
 print('\tAccount No :',result[0])
 print('\tCustomer Name :',result[1])
 print('\tAddress :',result[2])
 print('\tPhone NO :',result[3])
 print('\tEmail ID :',result[4])
 print('\tAadhar No :',result[5])
 print('\tAccount Type :',result[6])
 print('\tAccount Status :',result[7])
 print('\tCurrent Balance :',result[8])
 print('-'*120)
 mycur.execute(sql1)
 results = mycur.fetchall()
 for result in results:
  print(result[0], result[1], result[2], result[3])
 mydb.commit()
 wait=input('\n\n\nPress any key to continue.....')
def account_status(acno):
 mycur.execute('use project')
 sql ="select status,balance from customer where acno ='"+acno+"'"
 result = mycur.execute(sql)
 result = mycur.fetchone()
 mydb.commit()
 return result
def deposit_amount():
 mycur.execute('use project')
 acno = input('Enter account No :')

 amount = input('Enter amount :')
 x=input('Enter your pin')
 y=[(int(x),)]
 sql = 'select pin from customer where acno="'+ str(acno)+'";'
 mycur.execute(sql)
 records = mycur.fetchall()
 if y==records:
  today = date.today()
  result = account_status(acno)
  if result [0]== 'active':
   sql1 ="update customer set balance = balance+"+amount + ' where acno = '+acno+' and status="active";'
   sql2 = 'insert into transaction(amount,type,acno,dot) values(' + amount +',"deposit",'+acno+',"'+str(today)+'");'
   mycur.execute(sql2)
   mycur.execute(sql1)
   mydb.commit()
   print('\n\namount deposited')
 
  else:
   print('\n\nClosed or Suspended Account....')
 else:
  print('Invalid pin')
  wait= input('\n\n\n Press any key to continue....')
def withdraw_amount():
 mycur.execute('use project')
 acno = input('Enter account No :')
 amount = input('Enter amount :')
 x=input('Enter your pin')
 y=[(int(x),)]
 sql = 'select pin from customer where acno="'+ str(acno)+'";'
 mycur.execute(sql)
 records = mycur.fetchall()
 if y==records:
  today = date.today()
  result = account_status(acno)
  if result[0] == 'active' and int(result[1])>=int(amount):
   sql1 = "update customer set balance = balance-" + amount + ' where acno = '+acno+' and status="active";'
   sql2 = 'insert into transaction(amount,type,acno,dot) values(' + amount + ',"withdraw",'+acno+',"'+str(today)+'");'
   mycur.execute(sql2)
   mycur.execute(sql1)
   mydb.commit()
   print('\n\namount Withdrawn')

  else:
   print('\n\nClosed or Suspended Account.Or Insufficient amount')
 else:
  print('Invalid pin')
  wait = input('\n\n\n Press any key to continue....')
def transaction_menu():
 while True:
  print(' Trasaction Menu')
  print("\n1. Deposit Amount")
  print('\n2. WithDraw Amount')
  print('\n3. Back to Main Menu')
  print('\n\n')
  choice = int(input('Enter your choice ...: '))
  if choice == 1:
   deposit_amount()
  if choice == 2:
   withdraw_amount()
  if choice == 3:
   break
def search_menu():
 mycur.execute('use project')
 while True:
  print(' Search Menu')
  print("\n1. Account No")
  print('\n2. Aadhar Card')
  print('\n3. Phone No')
  print('\n4. Email')
  print('\n5. Names')
  print('\n6. Back to Main Menu')
  choice = int(input('Enter your choice ...: '))
  field_name=''
 
  if choice == 1:
   field_name ='acno'
 
  if choice == 2:
   field_name ='aadhar_no'
 
  if choice == 3:
   field_name = 'phone'
  
  if choice == 4:
   field_name = 'email'
  if choice == 5:
   field_name = 'name'
 
  if choice == 6:
 
   break
  msg ='Enter '+field_name+': '
  value = input(msg)
  if field_name=='acno':
    sql = 'select * from customer where '+field_name + ' = '+value+';'
  else:
    sql = 'select * from customer where '+field_name +' like "%'+value+'%";'
  mycur.execute(sql)
  records = mycur.fetchall()
  n = len(records)
  print('Search Result for ', field_name, ' ',value)
  print('-'*80)
  for record in records:
    print(' Account number\t',' : ',record[0],'\n', 'Name\t\t',' : ',record[1],'\n', 'address\t',' : ',record[3],'\n','Phone number\t',' : ',record[4],'\n', 'Email\t\t',' : ',record[5],'\n', 'Aadhar number\t',' : ',record[6],'\n','Account type\t',' : ', record[7],'\n', 'Account status\t',' : ',record[8],'\n', 'Account balance',' : ',record[9],'\n')
  if(n <= 0):
    print(field_name, ' ', value, ' does not exist')
  wait = input('\n\n\n Press any key to continue....')
  mydb.commit()
#create()
main_menu()

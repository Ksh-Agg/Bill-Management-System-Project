import pickle
import os

def append():
  f=open("project.dat","ab")
  l1=[]
  ch='y'
  while ch=='y':
    icode=int(input("Enter item code - "))
    iname=input("Enter item name - ")
    qty=int(input("Enter the quantity - "))
    price=int(input("Enter the price - "))
    bill=qty*price
    rec=[icode,iname,qty,price,bill]
    l1.append(rec)
    ch=input("Do u want to add more records - ")
  pickle.dump(l1,f)
  f.close()


def displayall():
  f=open("project.dat","rb")  
  try:
    while True:
      data=pickle.load(f)
      for i in data:
        print(i)
  except EOFError:
    f.close()


def search():
  f=open("project.dat","rb")
  found=0
  a=int(input("Enter code to search - "))
  try:
    while True:
      data=pickle.load(f)
      for i in data:
        if i[0]==a:
          print(i)
          found=1
    if found==0:
      print("Record does not exists")
  except EOFError:
      f.close()


def modify():    
    f=open('project.dat',"rb+")
    found=0
    price=int(input("Enter modified price - "))
    qty=int(input("Enter modified quantity - "))
    code=int(input("Enter itemcode whose price you want to change - "))
    try:
        while True:
            pos=f.tell()
            res=pickle.load(f)
            for i in res:
                if i[0]==code:
                    i[2]=qty
                    i[3]=price
                    i[4]=qty*price
                    found=1
                    f.seek(pos,0)
                    pickle.dump(res,f)
        if found==0:
            print("Record does not exists")
    except EOFError:
        f.close()


def delete():
  f1=open('temp.dat',"wb")
  found=False
  f=open('project.dat',"rb+")
  code=int(input("Enter itemcode which you want to delete - "))
  try:
    while True:
      res=pickle.load(f)
      for i in res:
        if i[0]!=code:
          pickle.dump(i,f1)
        else:
          found=True
  except EOFError:
    if found==True:   
      print("Record deleted successfully")
      f1.close()
      f.close()
      os.remove('project.dat')
      os.rename('temp.dat','project.dat')
    else:
      print("Record not found")

             
x="A1B2C3D4" 
password=input("Enter the password - ")
if password==x:
  print("\t\t\t\tWELCOME TO OUR PROJECT")
  print("\t\t\t\t MAIN  MENU")
  print("\t\t\t 1. Addition of a new record")
  print("\t\t\t 2. Display all")
  print("\t\t\t 3. Searching on the basis of code")
  print("\t\t\t 4. Modify a record on the basis of code")
  print("\t\t\t 5. Delete a record")
  Ch='y'
  while Ch=='y' or Ch=='Y':
    
    choice=int(input("Enter your choice of operation - "))
    if choice==1:
      append()
    elif choice==2:
      displayall()
    elif choice==3:
      search()
    elif choice==4:
      modify()
    elif choice==5:
      delete()
    Ch=input("Do u want to continue working on the file - ")
else:
  print("Wrong password")

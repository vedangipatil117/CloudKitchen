
from flask import Flask, render_template, request, session, abort
from flask_mysqldb import MySQL
import MySQLdb.cursors
import mysql.connector


app = Flask(__name__)
app.secret_key="cloudkitchen"


app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='kitchen'
mysql = MySQL(app)
  

@app.route('/')

@app.route('/login_valid', methods=['GET','POST'])
def login_valid():
      if request.method=='POST' and 'username' in request.form and 'password' in request.form:
          username=request.form['username']
          password=request.form['password']
          if username=="admin" and password=="pass":
             return render_template('dashboard.html')
          else:   
           cursor= mysql.connection.cursor(MySQLdb.cursors.DictCursor)
           
           cursor.execute('SELECT * FROM login WHERE username = %s AND password = %s',(username,password,))
           r=cursor.fetchone()
          
          if r:
               session['loggedin'] = True
               session['id'] = r['id']
               session['username'] = r['username']
               session['password'] = r['password']
               return render_template ('worker.html')   
                        
      else:
            #abort(401)
            error="invalid username or password"
            return render_template('login.html',error=error)

      return render_template('login.html')
 

@app.route('/emp', methods=['GET','POST'])
def emp():
   if request.method=='POST' :
  
      cursor= mysql.connection.cursor()
      
      number=int(request.form['number'])
      bname=request.form['bname']
      blocation=request.form['blocation']
      month=request.form['month']
      order=int(request.form['order'])
      takeout=int(request.form['takeout'])
      profit=int(request.form['profit'])
      expense=int(request.form['expense'])
      cursor.execute('INSERT INTO branch (number,bname,blocation,month,`order`,takeout,profit,expense)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',(number,bname,blocation,month,order,takeout,profit,expense))
      
      if bname=="brancha":
         dish=request.form['dish']
         rating=request.form['rating']
         delivery=int(request.form['delivery'])
         dinein=request.form['dinein']
         month=month
         cursor.execute('INSERT INTO branch1 (dish,rating,delivery,dinein,month)VALUES(%s,%s,%s,%s,%s)',(dish,rating,delivery,dinein,month))
      
      if bname=="branchb":
         dish=request.form['dish']
         rating=request.form['rating']
         delivery=int(request.form['delivery'])
         dinein=request.form['dinein']
         month=month
         cursor.execute('INSERT INTO branch2 (dish,rating,delivery,dinein,month)VALUES(%s,%s,%s,%s,%s)',(dish,rating,delivery,dinein,month))
         
      if bname=="branchc":
         dish=request.form['dish']
         rating=request.form['rating']
         delivery=int(request.form['delivery'])
         dinein=request.form['dinein']
         month=month
         cursor.execute('INSERT INTO branch3 (dish,rating,delivery,dinein,month)VALUES(%s,%s,%s,%s,%s)',(dish,rating,delivery,dinein,month))
       
      if bname=="branchd":
         dish=request.form['dish']
         rating=request.form['rating']
         delivery=int(request.form['delivery'])
         dinein=request.form['dinein']
         month=month
         cursor.execute('INSERT INTO branch4 (dish,rating,delivery,dinein,month)VALUES(%s,%s,%s,%s,%s)',(dish,rating,delivery,dinein,month)) 
          
      mysql.connection.commit()
      cursor.close()
   
      return "Your response has been submitted"
   else:
      abort(404)

      
   
   

@app.route('/expense')
def expense():
    cursor= mysql.connection.cursor()
    cursor.execute("SELECT * FROM branch")
    data = cursor.fetchall()
    mysql.connection.commit()
    return render_template('index.html',data=data)

@app.route('/b1')
def b1():
    cursor= mysql.connection.cursor()
    cursor.execute("SELECT * FROM branch1")
    data = cursor.fetchall()
    mysql.connection.commit()
    return render_template('b1.html',data=data)

@app.route('/b2')
def b2():
    cursor= mysql.connection.cursor()
    cursor.execute("SELECT * FROM branch2")
    data = cursor.fetchall()
    mysql.connection.commit()
    return render_template('b2.html',data=data)

@app.route('/b3')
def b3():
    cursor= mysql.connection.cursor()
    cursor.execute("SELECT * FROM branch3")
    data = cursor.fetchall()
    mysql.connection.commit()
    return render_template('b3.html',data=data)

@app.route('/b4')
def b4():
    cursor= mysql.connection.cursor()
    cursor.execute("SELECT * FROM branch4")
    data = cursor.fetchall()
    mysql.connection.commit()
    return render_template('b4.html',data=data)


   
 
@app.route('/menu')
def menu():
   return render_template('menu.html')

@app.route('/ckhr')
def ckhr():
   return render_template('ckhr.html')

@app.route('/bd')
def bd():
   return render_template('bd.html')

@app.route('/l1')
def l1():
   return render_template('l1.html')
@app.route('/l2')
def l2():
   return render_template('l2.html')
@app.route('/l3')
def l3():
   return render_template('l3.html')
@app.route('/l4')
def l4():
   return render_template('l4.html')

@app.route('/logout')
def logout():
   return render_template('login.html')


   

              
if __name__ =='__main__':
    app.run(debug=True, port=5000)
   
    

                
    
            
    
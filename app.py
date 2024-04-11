from flask import Flask, render_template, request, session, url_for, redirect, jsonify,make_response
import pymysql
import random
import smtplib
import string
import math, random
from werkzeug.utils import secure_filename
import os
from datetime import datetime, timedelta
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.pdfgen import canvas
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
import calendar


app = Flask(__name__)

app.config['IMAGE_UPLOADS'] = 'static/menuimages/'
app.config['IMAGE_UPLOADS_UPDATE'] = 'static/menuimages1/'
app.config['GRAPH_UPLOADS'] = 'static/graphs/'

app.secret_key = 'any random string'

def dbConnection():
    connection = pymysql.connect(host="localhost", user="root", password="pwd", database="restaurant", port=3306)
    return connection


def dbClose():
    try:
        dbConnection().close()
    except:
        print("Something went wrong in Close DB Connection")
        
        
                
con = dbConnection()
cursor = con.cursor()


@app.route('/index')
def index():
    return render_template('index.html') 

@app.route('/addemployee')
def addemployee():
    return render_template('addemployee.html') 

@app.route('/')
def login():
    return render_template('login.html') 

@app.route('/homepage')
def homepage():
    return render_template('homepage.html') 

@app.route('/mainpage')
def mainpage():
    return render_template('mainpage.html')


@app.route('/addmenu')
def addmenu():
    return render_template('addmenu.html')

@app.route('/empindex')
def empindex():
    return render_template('empindex.html')

@app.route('/addsupplier')
def addsupplier():
    return render_template('addsupplier.html')

@app.route('/viewmenu')
def viewmenu():
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM addmenu')
    view_details = cursor.fetchall() 
    print(view_details)
    return render_template('viewmenu.html', view_details=view_details)




    
@app.route('/empregistration',methods=['POST','GET'])
def empregistration():
    if request.method == "POST":
        details = request.form
        name = details['name']
        
        
        user_id= details['user_id']
        password = details['password']
        person = details['person']
        
        sql2  = "INSERT INTO empregister(name,user_id,password,person) VALUES (%s, %s, %s, %s)"
        val2 = (str(name), str(user_id), str(password),str(person))
        cursor.execute(sql2,val2) 
        con.commit()
        print("username",name)
       
        
        return render_template('login.html')     
        
    

@app.route('/userlogin', methods=["GET","POST"])
def userlogin():
    msg = ''
    if request.method == "POST": 
        
          
            user_id = request.form["user_id"]
            print ("username",user_id)
            password = request.form["password"]
            person = request.form["person"]

            
            
            con = dbConnection()
            cursor = con.cursor()
            
            if person == "Owner":
                result_count=cursor.execute('SELECT * FROM ownerlogin WHERE user_id = %s AND password = %s AND person =%s' , (user_id, password, person))
                result = cursor.fetchone()
                if result_count>0:
                    session['user'] = result[0]
                    session['pass'] = result[1]
                    # return render_template('homepage.html')
                    return redirect(url_for('viewmenu'))
                else:
                    msg = 'Incorrect username/password!'
                    return msg
            
            elif person == "Manager":
                result_count=cursor.execute('SELECT * FROM managerlogin WHERE user_id = %s AND password = %s AND person =%s' , (user_id, password, person))
                result = cursor.fetchone()
                if result_count>0:
                    session['user'] = result[0]
                    session['pass'] = result[1]
                    
                    return redirect(url_for('manager_view_menu'))
                    
                
                
            elif person == "Employee":
                result_count=cursor.execute('SELECT * FROM empregister WHERE user_id = %s AND password = %s AND person =%s' , (user_id, password, person))
                result = cursor.fetchone()
                if result_count>0:
                    session['user1'] = result[1]
                    session['pass'] = result[2]
                     
                    return redirect(url_for('menu'))
                    
            msg = 'Incorrect username/password!'
            return msg
   
    return render_template('login.html')

@app.route('/manager_view_menu')
def manager_view_menu():
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM addmenu')
    m_view_details = cursor.fetchall() 
    print(m_view_details)
    return render_template('manager_view_menu.html', m_view_details=m_view_details)



@app.route('/manageraddmenu',methods=['POST','GET'])
def manageraddmenu():
    if request.method == "POST":
            f2 = request.files["choosefile1"]
            menuname = request.form["menuname"]
            
            price = request.form["price"]
            category = request.form["category"]
            print ("price",price)
            print ("category",category)
            print ("menuname",menuname)
           
            
            filename_secure = secure_filename(f2.filename)
            f2.save(os.path.join(app.config['IMAGE_UPLOADS'], filename_secure))
            filenamepath =os.path.join(app.config['IMAGE_UPLOADS'], filename_secure)          
            filename55 = filename_secure
            print("filenamepath",filenamepath)
            con = dbConnection()
            cursor = con.cursor()
            sql = "INSERT INTO addmenu (choosefile, menuname, price, category) VALUES (%s, %s, %s, %s)"
            val = (filenamepath, menuname, price, category)
            cursor.execute(sql, val)
            con.commit()
            return render_template('mainpage.html')
    
@app.route('/menu')
def menu():
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM addmenu')
    menu_items = cursor.fetchall() 
    print(menu_items)
    return render_template('menu.html', menu_items=menu_items)


@app.route('/manager_monthly_report')
def manager_monthly_report():
    try:
        # Connect to the database
        con = dbConnection()
        cursor = con.cursor()

        # Get the start and end of the current month
        current_date = datetime.now()
        current_year = current_date.year
        current_month = current_date.month

        # Initialize a dictionary to store monthly reports
        monthly_reports = {}

        # Iterate over each month of the current year
        for month in range(1, current_month + 1):
            start_of_month = datetime(current_year, month, 1)
            end_of_month = start_of_month + timedelta(days=31)  # Add 31 days to handle months with 31 days

            # Query the database to get sales data for the current month
            cursor.execute("SELECT item_name, COUNT(item_name) AS total_count FROM bills WHERE bill_datetime >= %s AND bill_datetime <= %s GROUP BY item_name ORDER BY total_count DESC LIMIT 1", (start_of_month, end_of_month))
            most_sold_product = cursor.fetchone()

            # Query the database to get sales data for the current month
            cursor.execute("SELECT item_name, item_price FROM bills WHERE bill_datetime >= %s AND bill_datetime <= %s", (start_of_month, end_of_month))
            sales_this_month = cursor.fetchall()

            # Calculate total sales price for the month
            total_sales_price = sum(float(sale[1]) for sale in sales_this_month)

            # Create a dictionary to store product names as keys and their total prices as values
            product_prices = {}
            for sale in sales_this_month:
                item_name = sale[0]
                item_price = float(sale[1])
                if item_name in product_prices:
                    product_prices[item_name] += item_price
                else:
                    product_prices[item_name] = item_price

            # Store the monthly report in the dictionary
            monthly_reports[start_of_month.strftime('%B %Y')] = {
                'most_sold_product': most_sold_product,
                'product_prices': product_prices,
                'total_sales_price': total_sales_price
            }

        # Close the database connection
        con.close()

        # Render the manager report HTML template with the monthly reports
        return render_template('manager_report.html', monthly_reports=monthly_reports)
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return HTTP 500 for internal server error

@app.route('/manager_daily_report')
def manager_daily_report():
    try:
        # Connect to the database
        con = dbConnection()
        cursor = con.cursor()

        # Get the start and end of the current day
        current_date = datetime.now()
        start_of_day = datetime(current_date.year, current_date.month, current_date.day, 0, 0, 0)
        end_of_day = datetime(current_date.year, current_date.month, current_date.day, 23, 59, 59)

        # Query the database to get sales data for the current day
        cursor.execute("SELECT item_name, COUNT(item_name) AS total_count FROM bills WHERE bill_datetime >= %s AND bill_datetime <= %s GROUP BY item_name ORDER BY total_count DESC LIMIT 1", (start_of_day, end_of_day))
        most_sold_product = cursor.fetchone()

        # Query the database to get sales data for the current day
        cursor.execute("SELECT item_name, item_price FROM bills WHERE bill_datetime >= %s AND bill_datetime <= %s", (start_of_day, end_of_day))
        sales_today = cursor.fetchall()

        # Calculate total sales price for today
        total_sales_price = 0
        product_prices = {}

        for sale in sales_today:
            item_name = sale[0]
            item_price = float(sale[1])
            total_sales_price += item_price

            if item_name in product_prices:
                product_prices[item_name] += item_price
            else:
                product_prices[item_name] = item_price

        # Close the database connection
        con.close()

        # Render the manager report HTML template with the most sold product, all products sold today, and total sales price
        return render_template('manager_day_report.html', most_sold_product=most_sold_product, product_prices=product_prices, total_sales_price=total_sales_price)
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return HTTP 500 for internal server error

@app.route('/start_shift', methods=['POST'])
def start_shift():
    global current_shift_start_time
    current_shift_start_time = datetime.now()
    return "Shift started"

@app.route('/stop_shift', methods=['POST'])
def stop_shift():
    global current_shift_start_time
    if current_shift_start_time:
        shift_start_time = current_shift_start_time
        current_shift_start_time = None
        shift_end_time = datetime.now()
        shift_duration = shift_end_time - shift_start_time

        # Get the logged-in employee's ID
        logged_in_employee_id = session.get('user1')

        # Insert shift information into the database
        con = dbConnection()
        cursor = con.cursor()
        insert_query = "INSERT INTO shifts (employee_id, start_time, end_time, duration) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (logged_in_employee_id, shift_start_time, shift_end_time, shift_duration))
        con.commit()
        con.close()

        return "Shift stopped. Shift duration: " + str(shift_duration)
    else:
        return "No active shift"



@app.route('/empreport')
def empreport():
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM shifts')
    shift_time = cursor.fetchall() 
    print(shift_time)
    return render_template('empreport.html', shift_time=shift_time)

@app.route("/updatemenu/<string:id>",methods=['POST','GET'])
def updatecourse(id):
    print ("ID",id)
    con = dbConnection()
    cursor = con.cursor()
    
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM addmenu WHERE id = %s ', (id))
   
    result = cursor.fetchone()
    res=result
   
    print ("spotreateddata",res)
    return render_template('editmenu.html',res=res,productid=res[4])

@app.route('/editmenu', methods=["GET","POST"])
def editcourse():
    if request.method == "POST":
        f2 = request.files["choosefile1"]
        print ("choosefile1",f2)
        menuname = request.form.get("menuname")
        print ("menuname",menuname)
        price = request.form.get("price")
        category = request.form.get("category")
        productid = request.form.get("productid")
        
            
        filename_secure = secure_filename(f2.filename)
        f2.save(os.path.join(app.config['IMAGE_UPLOADS_UPDATE'], filename_secure))
        filenamepath = os.path.join(app.config['IMAGE_UPLOADS_UPDATE'], filename_secure)          
        filename55 = filename_secure
        print ("filenamepath",filenamepath)
        print ("menuname",menuname)
        print ("price",price)
        print ("category",category)
        print ("productid",productid)
        
        
        con = dbConnection()
        cursor = con.cursor()
        sql2 = "UPDATE addmenu SET choosefile = %s, price = %s, category = %s, menuname = %s WHERE id = %s;"
        val2 = (filenamepath, price, category, str(menuname), productid)
        cursor.execute(sql2,val2)
        con.commit()
        return render_template('index.html')
        
@app.route('/manageraddsupplier',methods=['POST','GET'])
def manageraddsupplier():
    if request.method == "POST":
            f2 = request.files["file1"]
            suppliername = request.form["suppliername"]
            
            stype = request.form["stype"]
            mobileno = request.form["mobileno"]
            print ("suppliername",suppliername)
            print ("stype",stype)
            print ("mobileno",mobileno)
           
            
            filename_secure = secure_filename(f2.filename)
            f2.save(os.path.join(app.config['IMAGE_UPLOADS'], filename_secure))
            filenamepath =os.path.join(app.config['IMAGE_UPLOADS'], filename_secure)          
            filename55 = filename_secure
            print("filenamepath",filenamepath)
            con = dbConnection()
            cursor = con.cursor()
            sql = "INSERT INTO addsupplier (image_file, suppliername, stype, mobileno) VALUES (%s, %s, %s, %s)"
            val = (filenamepath, suppliername, stype, mobileno)
            cursor.execute(sql, val)
            con.commit()
            return render_template('mainpage.html')
        
@app.route('/supplier')
def supplier():
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM addsupplier')
    supplier_details = cursor.fetchall() 
    print(supplier_details)
    return render_template('supplier.html', supplier_details=supplier_details)     

@app.route('/save_bill', methods=['POST'])
def save_bill():
    # Extract bill data from the request
    bill_data = request.json
   
    try:
        con = dbConnection()
        cursor = con.cursor()
        # Ensure that the bill_data contains 'item_name' and 'item_price' keys
        item_name = bill_data.get('item_name')
        item_price = bill_data.get('item_price')
        if item_name is not None and item_price is not None:
            # Get current date and time
            current_datetime = datetime.now()

            # Insert bill data along with the current date and time into the database
            cursor.execute("INSERT INTO bills (item_name, item_price, bill_datetime) VALUES (%s, %s, %s)", (item_name, item_price, current_datetime))
            con.commit()
            con.close()
            return jsonify({'message': 'Bill saved successfully'})
        else:
            return jsonify({'error': 'Missing item_name or item_price in request'}), 400  # Return HTTP 400 for bad request
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return HTTP 500 for internal server error

    

        
@app.route('/download_bill_pdf', methods=['POST'])
def download_bill_pdf():
    # Receive selected items from the request
    selected_items = request.json
    
    # Create PDF canvas
    pdf_buffer = create_bill_pdf(selected_items)
    
    # Prepare response with PDF file for download
    response = make_response(pdf_buffer)
    response.headers['Content-Disposition'] = 'attachment; filename=bill_receipt.pdf'
    response.headers['Content-Type'] = 'application/pdf'
    
    return response

def create_bill_pdf(selected_items):
    # Create PDF canvas
    pdf_buffer = BytesIO()
    pdf = canvas.Canvas(pdf_buffer, pagesize=letter)
    
    # Set font and size for the bill receipt
    pdf.setFont("Helvetica", 12)
    
    # Add title of the restaurant
    pdf.drawString(100, 750, "Restaurant BOT")  # Adjust Y-coordinate
    
    # Add bill receipt content
    pdf.drawString(100, 730, "Bill Receipt")  # Adjust Y-coordinate
    pdf.drawString(100, 720, "--------------------------------------------")
    
    # Add date and time
    now = datetime.now()
    date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    pdf.setFont("Helvetica", 10)  # Adjust font size for date and time
    pdf.setFillColor(colors.black)  # Set text color
    pdf.drawString(100, 700, f"Date and Time: {date_time_str}")  # Adjust Y-coordinate
    
    # Create data for the table
    table_data = [["Item", "Price"]]
    total = 0
    for item in selected_items:
        name = item['name']
        price = item['price']
        table_data.append([name, f"€ {price:.2f}"])
        total += price
    
    # Create the table
    table = Table(table_data, colWidths=[300, 100], rowHeights=30)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    
    # Draw the table on the canvas
    table.wrapOn(pdf, 0, 0)
    table.drawOn(pdf, 100, 650 - len(selected_items) * 30)  # Adjust Y-coordinate
    
    # Add total to the PDF
    total_y = 650 - (len(selected_items) + 1) * 30  # Adjust Y-coordinate for total
    pdf.setFont("Helvetica-Bold", 12)  # Set font and size for total
    pdf.setFillColor(colors.black)  # Set text color for total
    pdf.drawString(100, total_y, f"Total: € {total:.2f}")  # Adjust Y-coordinate
    
    # Design the total
    pdf.line(100, total_y - 5, 400, total_y - 5)  # Draw a line under the total
    
    # Save the PDF canvas
    pdf.save()
    
    # Get the PDF content from the buffer
    pdf_buffer.seek(0)
    return pdf_buffer

# Route to display the graph
@app.route('/graph')
def display_graph():
    # Connect to the database
    con = dbConnection()
    # Fetch data from the bills table
    cursor = con.cursor()
    cursor.execute("SELECT item_name, SUM(item_price) AS Total_Sales, COUNT(*) AS Sales_Count FROM bills GROUP BY item_name")
    rows = cursor.fetchall()
    con.close()

    # Convert the data to a DataFrame for easier manipulation
    df = pd.DataFrame(rows, columns=['Item Name', 'Total Sales', 'Sales Count'])

    # Sort the DataFrame by total sales count in descending order
    df = df.sort_values(by='Sales Count', ascending=False)

    # Plot the graph
    plt.figure(figsize=(6, 6))
    plt.bar(df['Item Name'], df['Sales Count'], color='skyblue')
    plt.xlabel('Item Name')
    plt.ylabel('Total Sales Count')
    plt.title('Most Sold Products')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Define the path to save the graph
    graph_dir = app.config['GRAPH_UPLOADS']
    os.makedirs(graph_dir, exist_ok=True)
    graph_file = os.path.join(graph_dir, 'graph.png')

    # Save the plot to the specified directory
    plt.savefig(graph_file)

    # Close the plot to free up memory
    plt.close()

    # Render the template with the graph file path
    return render_template('graph.html', graph_file=graph_file)
 
if __name__ == "__main__":
    app.run("0.0.0.0")
    app.run(debug=True)
   


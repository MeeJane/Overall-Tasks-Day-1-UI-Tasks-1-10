from flask import Flask, request
import mysql.connector

app11 = Flask(__name__)


try:
    db11 = mysql.connector.connect(host="localhost", user="root", password="qaz123!@#")

    cursor11 = db11.cursor()
    print("Connected successfully!")
    # cursor11.execute("CREATE DATABASE testdb")
    # print("Database created")
    # cursor11 = db11.cursor()
    # cursor11.execute("SHOW DATABASES")
    # print(cursor11.fetchall())
    cursor11.execute("USE testdb")
    """ Table Creation"""
    """tasks 11-20 """
    #     cursor11.execute(
    #         """
    # CREATE TABLE IF NOT EXISTS users11 (
    #     id INT AUTO_INCREMENT PRIMARY KEY,
    #     name VARCHAR(100),
    #     email VARCHAR(100)
    # )
    # """
    #     )

    #     cursor11.execute(
    #         """
    # CREATE TABLE IF NOT EXISTS users12 (
    #     id INT AUTO_INCREMENT PRIMARY KEY,
    #     username VARCHAR(100),
    #     password VARCHAR(100)
    # )
    # """
    #     )

    #     cursor11.execute(
    #         """
    # CREATE TABLE IF NOT EXISTS students13 (
    #     id INT AUTO_INCREMENT PRIMARY KEY,
    #     name VARCHAR(100),
    #     age INT
    # )
    # """
    #     )

    #     cursor11.execute(
    #         """
    # CREATE TABLE IF NOT EXISTS feedback19 (
    #     id INT AUTO_INCREMENT PRIMARY KEY,
    #     message TEXT
    # )
    # """
    #     )

    #     cursor11.execute(
    #         """
    # CREATE TABLE IF NOT EXISTS contact20 (
    #     id INT AUTO_INCREMENT PRIMARY KEY,
    #     name VARCHAR(100),
    #     email VARCHAR(100)
    # )
    # """
    #     )

    #     db11.commit()

    """  Tasks 21-30"""

    #     cursor11.execute(
    #         """
    # CREATE TABLE IF NOT EXISTS products21 (
    #     id INT AUTO_INCREMENT PRIMARY KEY,
    #     name VARCHAR(100),
    #     price DECIMAL(10,2)
    # )
    # """
    #     )

    #     cursor11.execute(
    #         """
    # CREATE TABLE IF NOT EXISTS employees22 (
    #     id INT AUTO_INCREMENT PRIMARY KEY,
    #     name VARCHAR(100),
    #     department VARCHAR(100),
    #     salary DECIMAL(10,2),
    #     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    # )
    # """
    #     )

    #     db11.commit()
    #     print("Task 21-30 tables ready!")

    """Tasks 41-50"""
    cursor11.execute(
        """
CREATE TABLE IF NOT EXISTS products21 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2),
    image VARCHAR(255)
)
"""
    )

    cursor11.execute(
        """
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user VARCHAR(100),
    product_id INT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products21(id)
    ON DELETE CASCADE
)
"""
    )

    db11.commit()

except mysql.connector.Error as err:
    print("Error:", err)


# # ============Task-11==================
# print("11.Create a simple Python program that stores form data into a MySQL database.")


# @app11.route("/task11", methods=["GET", "POST"])
# def task11():
#     if request.method == "POST":
#         name11 = request.form["name11"]
#         email11 = request.form["email11"]
#         cursor11.execute(
#             "INSERT INTO users11(name,email) VALUES(%s,%s)", (name11, email11)
#         )
#         db11.commit()
#         return "Inserted Successfully Task11"
#     return """
#     <form method="post">
#     <input name="name11" placeholder="Name">
#     <input name="email11" placeholder="Email">
#     <button>Submit</button>
#     </form>
#     """


# print("*" * 100)


# # ============Task-12==================
# print(
#     "12.Build a login system with username & password validation using Python and MySQL."
# )


# @app11.route("/task12", methods=["GET", "POST"])
# def task12():
#     if request.method == "POST":
#         username12 = request.form["username12"]
#         password12 = request.form["password12"]
#         cursor11.execute(
#             "SELECT * FROM users12 WHERE username=%s AND password=%s",
#             (username12, password12),
#         )
#         user12 = cursor11.fetchone()
#         return "Login Success Task12" if user12 else "Invalid Credentials"
#     return """
#     <form method="post">
#     <input name="username12" placeholder="Username">
#     <input type="password" name="password12" placeholder="Password">
#     <button>Login</button>
#     </form>
#     """


# print("*" * 100)


# # ============Task-13==================
# print("13.Create a student registration system that inserts records into database.")
# # Create tables automatically if not exists

# cursor11.execute(
#     """
# CREATE TABLE IF NOT EXISTS users11 (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100),
#     email VARCHAR(100)
# )
# """
# )

# cursor11.execute(
#     """
# CREATE TABLE IF NOT EXISTS users12 (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     username VARCHAR(100),
#     password VARCHAR(100)
# )
# """
# )

# cursor11.execute(
#     """
# CREATE TABLE IF NOT EXISTS students13 (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100),
#     age INT
# )
# """
# )

# cursor11.execute(
#     """
# CREATE TABLE IF NOT EXISTS feedback19 (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     message TEXT
# )
# """
# )

# cursor11.execute(
#     """
# CREATE TABLE IF NOT EXISTS contact20 (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100),
#     email VARCHAR(100)
# )
# """
# )

# db11.commit()
# print("All tables ready!")


# @app11.route("/task13", methods=["GET", "POST"])
# def task13():
#     if request.method == "POST":
#         student13 = request.form["student13"]
#         age13 = request.form["age13"]
#         cursor11.execute(
#             "INSERT INTO students13(name,age) VALUES(%s,%s)",
#             (student13, age13),
#         )
#         db11.commit()
#         return "Student Added Task13"
#     return """
#     <form method="post">
#     <input name="student13" placeholder="Name">
#     <input name="age13" placeholder="Age">
#     <button>Add</button>
#     </form>
#     """


# print("*" * 100)


# # ============Task-14==================
# print("14.Build a page to display student list from database in a Bootstrap table.")


# @app11.route("/task14")
# def task14():
#     cursor11.execute("SELECT * FROM students13")
#     data14 = cursor11.fetchall()

#     table14 = ""
#     for row14 in data14:
#         table14 += f"""
#         <tr>
#             <td>{row14[0]}</td>
#             <td>{row14[1]}</td>
#             <td>{row14[2]}</td>
#         </tr>
#         """

#     return f"""
#     <link rel="stylesheet"
#     href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">

#     <div class="container mt-4">
#         <h2 class="mb-3">Student List</h2>
#         <table class="table table-bordered table-striped">
#             <tr>
#                 <th>ID</th>
#                 <th>Name</th>
#                 <th>Age</th>
#             </tr>
#             {table14}
#         </table>
#     </div>
#     """


# print("*" * 100)


# # ============Task-15==================
# print("15.Add edit functionality to update student details.")


# @app11.route("/task15/<int:id15>", methods=["GET", "POST"])
# def task15(id15):

#     if request.method == "POST":
#         name15 = request.form["name15"]
#         age15 = request.form["age15"]

#         cursor11.execute(
#             "UPDATE students13 SET name=%s, age=%s WHERE id=%s",
#             (name15, age15, id15),
#         )
#         db11.commit()

#         return "Student Updated Successfully!"

#     # GET METHOD → Fetch existing data
#     cursor11.execute("SELECT name, age FROM students13 WHERE id=%s", (id15,))
#     student15 = cursor11.fetchone()

#     return f"""
#     <form method="post">
#         <input name="name15" value="{student15[0]}" required>
#         <input name="age15" value="{student15[1]}" required>
#         <button>Update</button>
#     </form>
#     """


# # ============Task-16==================
# print("16.Add delete functionality with confirmation modal.")


# @app11.route("/task16/<int:id16>")
# def task16(id16):
#     cursor11.execute("DELETE FROM students13 WHERE id=%s", (id16,))
#     db11.commit()
#     return "Deleted Task16"


# print("*" * 100)


# # ============Task-17==================
# print("17.Implement search functionality from MySQL using Python backend.")


# @app11.route("/task17", methods=["GET", "POST"])
# def task17():
#     result17 = ""
#     if request.method == "POST":
#         search17 = request.form["search17"]
#         cursor11.execute(
#             "SELECT * FROM students13 WHERE name LIKE %s",
#             ("%" + search17 + "%",),
#         )
#         rows17 = cursor11.fetchall()
#         for r17 in rows17:
#             result17 += f"<p>{r17}</p>"
#     return (
#         """
#     <form method="post">
#     <input name="search17" placeholder="Search Name">
#     <button>Search</button>
#     </form>
#     """
#         + result17
#     )


# print("*" * 100)


# # ============Task-18==================
# print("18.Add pagination for student records.")


# @app11.route("/task18/<int:page18>")
# def task18(page18):
#     limit18 = 5
#     offset18 = (page18 - 1) * limit18
#     cursor11.execute(
#         "SELECT * FROM students13 LIMIT %s OFFSET %s",
#         (limit18, offset18),
#     )
#     data18 = cursor11.fetchall()
#     return str(data18)


# print("*" * 100)


# # ============Task-19==================
# print("19.Build a feedback form that stores responses in database.")


# @app11.route("/task19", methods=["GET", "POST"])
# def task19():
#     if request.method == "POST":
#         feedback19 = request.form["feedback19"]
#         cursor11.execute(
#             "INSERT INTO feedback19(message) VALUES(%s)",
#             (feedback19,),
#         )
#         db11.commit()
#         return "Feedback Stored Task19"
#     return """
#     <form method="post">
#     <textarea name="feedback19"></textarea>
#     <button>Submit</button>
#     </form>
#     """


# print("*" * 100)


# # ============Task-20==================
# print("20.Create a contact form that sends data to backend and stores in MySQL.")


# @app11.route("/task20", methods=["GET", "POST"])
# def task20():
#     if request.method == "POST":
#         name20 = request.form["name20"]
#         email20 = request.form["email20"]
#         cursor11.execute(
#             "INSERT INTO contact20(name,email) VALUES(%s,%s)",
#             (name20, email20),
#         )
#         db11.commit()
#         return "Contact Stored Task20"
#     return """
#     <form method="post">
#     <input name="name20">
#     <input name="email20">
#     <button>Submit</button>
#     </form>
#     """


# print("*" * 100)
# # ================= TASK 21 =================
# print("21. Build a product management system (Add / View / Edit / Delete products).")


# @app11.route("/task21")
# def task21():
#     return """
#     <h2>Product Management</h2>
#     <a href="/task21/add">Add</a> |
#     <a href="/task21/view">View</a>
#     """


# @app11.route("/task21/add", methods=["GET", "POST"])
# def task21_add():
#     if request.method == "POST":
#         name = request.form["name"]
#         price = request.form["price"]
#         cursor11.execute(
#             "INSERT INTO products21(name,price) VALUES(%s,%s)", (name, price)
#         )
#         db11.commit()
#         return "Added <br><a href='/task21'>Back</a>"
#     return """
#     <form method="post">
#     <input name="name" placeholder="Name">
#     <input name="price" placeholder="Price">
#     <button>Add</button>
#     </form>
#     """


# @app11.route("/task21/view")
# def task21_view():
#     cursor11.execute("SELECT * FROM products21")
#     data = cursor11.fetchall()
#     result = ""
#     for row in data:
#         result += f"{row[1]} - ₹{row[2]} <a href='/task21/edit/{row[0]}'>Edit</a> <a href='/task21/delete/{row[0]}'>Delete</a><br>"
#     return result


# @app11.route("/task21/edit/<int:id>", methods=["GET", "POST"])
# def task21_edit(id):
#     if request.method == "POST":
#         name = request.form["name"]
#         price = request.form["price"]
#         cursor11.execute(
#             "UPDATE products21 SET name=%s,price=%s WHERE id=%s", (name, price, id)
#         )
#         db11.commit()
#         return "Updated <br><a href='/task21/view'>Back</a>"
#     cursor11.execute("SELECT name,price FROM products21 WHERE id=%s", (id,))
#     data = cursor11.fetchone()
#     return f"""
#     <form method="post">
#     <input name="name" value="{data[0]}">
#     <input name="price" value="{data[1]}">
#     <button>Update</button>
#     </form>
#     """


# @app11.route("/task21/delete/<int:id>")
# def task21_delete(id):
#     cursor11.execute("DELETE FROM products21 WHERE id=%s", (id,))
#     db11.commit()
#     return "Deleted <br><a href='/task21/view'>Back</a>"


# # ================= TASK 22 =================
# print("22. Create employee management system with salary field.")


# @app11.route("/task22")
# def task22():
#     cursor11.execute("SELECT * FROM employees22")
#     data = cursor11.fetchall()

#     result = "<h2>Employee Management</h2>"
#     result += "<a href='/task22/add'>Add Employee</a><br><br>"

#     for row in data:
#         result += f"""
#         {row[1]} | {row[2]} | ₹{row[3]}
#         <a href='/task22/edit/{row[0]}'>Edit</a>
#         <a href='/task22/delete/{row[0]}'>Delete</a>
#         <br>
#         """
#     return result


# @app11.route("/task22/add", methods=["GET", "POST"])
# def task22_add():
#     if request.method == "POST":
#         name = request.form["name"]
#         dept = request.form["department"]
#         salary = request.form["salary"]

#         cursor11.execute(
#             "INSERT INTO employees22(name,department,salary) VALUES(%s,%s,%s)",
#             (name, dept, salary),
#         )
#         db11.commit()
#         return "Employee Added <br><a href='/task22'>Back</a>"

#     return """
#     <form method="post">
#     <input name="name" placeholder="Name"><br>
#     <input name="department" placeholder="Department"><br>
#     <input name="salary" placeholder="Salary"><br>
#     <button>Add</button>
#     </form>
#     """


# @app11.route("/task22/edit/<int:id>", methods=["GET", "POST"])
# def task22_edit(id):
#     if request.method == "POST":
#         name = request.form["name"]
#         dept = request.form["department"]
#         salary = request.form["salary"]

#         cursor11.execute(
#             "UPDATE employees22 SET name=%s,department=%s,salary=%s WHERE id=%s",
#             (name, dept, salary, id),
#         )
#         db11.commit()
#         return "Updated <br><a href='/task22'>Back</a>"

#     cursor11.execute(
#         "SELECT name,department,salary FROM employees22 WHERE id=%s", (id,)
#     )
#     data = cursor11.fetchone()

#     return f"""
#     <form method="post">
#     <input name="name" value="{data[0]}"><br>
#     <input name="department" value="{data[1]}"><br>
#     <input name="salary" value="{data[2]}"><br>
#     <button>Update</button>
#     </form>
#     """


# @app11.route("/task22/delete/<int:id>")
# def task22_delete(id):
#     cursor11.execute("DELETE FROM employees22 WHERE id=%s", (id,))
#     db11.commit()
#     return "Deleted <br><a href='/task22'>Back</a>"


# # ================= TASK 23 =================
# print("23. Add filter employees by department (backend query).")


# @app11.route("/task23")
# def task23():
#     dept = request.args.get("dept")

#     result = """
#     <form>
#     <input name="dept" placeholder="Enter Department">
#     <button>Filter</button>
#     </form><br>
#     """

#     if dept:
#         cursor11.execute(
#             "SELECT * FROM employees22 WHERE department=%s",
#             (dept,),
#         )
#         data = cursor11.fetchall()
#         for row in data:
#             result += f"{row[1]} - {row[2]} - ₹{row[3]}<br>"

#     return result


# # ================= TASK 24 =================
# print("24. Display total employee count from database on dashboard.")


# @app11.route("/task24")
# def task24():
#     cursor11.execute("SELECT COUNT(*) FROM employees22")
#     total = cursor11.fetchone()[0]
#     return f"<h3>Total Employees: {total}</h3>"


# # ================= TASK 25 =================
# print("25. Show highest salary employee on dashboard using SQL query.")


# @app11.route("/task25")
# def task25():
#     cursor11.execute("SELECT name,salary FROM employees22 ORDER BY salary DESC LIMIT 1")
#     data = cursor11.fetchone()
#     return f"<h3>Highest Salary: {data[0]} - ₹{data[1]}</h3>"


# # ================= TASK 26 =================
# print("26. Add sorting by salary using backend query.")


# @app11.route("/task26")
# def task26():
#     cursor11.execute("SELECT * FROM employees22 ORDER BY salary DESC")
#     data = cursor11.fetchall()

#     result = "<h3>Sorted by Salary (High to Low)</h3>"
#     for row in data:
#         result += f"{row[1]} - ₹{row[3]}<br>"
#     return result


# # ================= TASK 27 =================
# print("27. Implement search by name using LIKE query.")


# @app11.route("/task27")
# def task27():
#     name = request.args.get("name")

#     result = """
#     <form>
#     <input name="name" placeholder="Search Name">
#     <button>Search</button>
#     </form><br>
#     """

#     if name:
#         cursor11.execute(
#             "SELECT * FROM employees22 WHERE name LIKE %s",
#             ("%" + name + "%",),
#         )
#         data = cursor11.fetchall()
#         for row in data:
#             result += f"{row[1]} - {row[2]} - ₹{row[3]}<br>"

#     return result


# # ================= TASK 28 =================
# print("28. Show monthly registration statistics in table format.")


# @app11.route("/task28")
# def task28():
#     cursor11.execute(
#         """
#         SELECT YEAR(created_at), MONTH(created_at), COUNT(*)
#         FROM employees22
#         GROUP BY YEAR(created_at), MONTH(created_at)
#     """
#     )
#     data = cursor11.fetchall()

#     result = "<table border=1><tr><th>Year</th><th>Month</th><th>Total</th></tr>"
#     for row in data:
#         result += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>"
#     result += "</table>"

#     return result


# # ================= TASK 29 =================
# print("29. Display data grouped by department.")


# @app11.route("/task29")
# def task29():
#     cursor11.execute(
#         """
#         SELECT department, COUNT(*), AVG(salary)
#         FROM employees22
#         GROUP BY department
#     """
#     )
#     data = cursor11.fetchall()

#     result = "<table border=1><tr><th>Dept</th><th>Total</th><th>Avg Salary</th></tr>"
#     for row in data:
#         result += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>"
#     result += "</table>"

#     return result


# # ================= TASK 30 =================
# print("30. Implement bulk delete option using checkboxes.")


# @app11.route("/task30", methods=["GET", "POST"])
# def task30():

#     if request.method == "POST":
#         ids = request.form.getlist("emp_ids")

#         if ids:
#             format_strings = ",".join(["%s"] * len(ids))
#             query = f"DELETE FROM employees WHERE id IN ({format_strings})"
#             cursor11.execute(query, tuple(ids))
#             db11.commit()

#         return "Selected Employees Deleted <br><a href='/task30'>Back</a>"

#     # GET METHOD → Show table with checkboxes
#     cursor11.execute("SELECT * FROM employees")
#     data = cursor11.fetchall()

#     table = """
#     <h2>Bulk Delete Employees</h2>
#     <form method="post">
#     <table border="1" cellpadding="8">
#     <tr>
#         <th>Select</th>
#         <th>ID</th>
#         <th>Name</th>
#         <th>Department</th>
#         <th>Salary</th>
#     </tr>
#     """

#     for row in data:
#         table += f"""
#         <tr>
#             <td>
#                 <input type="checkbox" name="emp_ids" value="{row[0]}">
#             </td>
#             <td>{row[0]}</td>
#             <td>{row[1]}</td>
#             <td>{row[2]}</td>
#             <td>{row[3]}</td>
#         </tr>
#         """

#     table += """
#     </table>
#     <br>
#     <button type="submit">Delete Selected</button>
#     </form>
#     """

#     return table

# # ================= ADVANCED TASKS 31 - 40 =================


# from flask import session
# import hashlib
# import csv

# app11.secret_key = "secretkey123"

# # ================= TASK 31 =================
# print("31. Add login session handling using Python.")


# @app11.route("/task31/login", methods=["GET", "POST"])
# def task31_login():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]

#         cursor11.execute(
#             "SELECT * FROM users12 WHERE username=%s AND password=%s",
#             (username, password),
#         )
#         user = cursor11.fetchone()

#         if user:
#             session["user"] = username
#             return "Login Success <a href='/task31/dashboard'>Dashboard</a>"
#         return "Invalid Login"

#     return """
#     <form method="post">
#         <input name="username" placeholder="Username"><br>
#         <input type="password" name="password" placeholder="Password"><br>
#         <button>Login</button>
#     </form>
#     """


# @app11.route("/task31/dashboard")
# def task31_dashboard():
#     if "user" in session:
#         return f"Welcome {session['user']} - Logged In"
#     return "Please Login First"


# # ================= TASK 32 =================
# print("32. Restrict dashboard access without login.")


# @app11.route("/task32")
# def task32():
#     if "user" not in session:
#         return "Access Denied! Login Required"
#     return "Secure Dashboard Content"


# # ================= TASK 33 =================
# print("33. Add password hashing before storing in database.")


# @app11.route("/task33/register", methods=["GET", "POST"])
# def task33_register():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]

#         hashed = hashlib.sha256(password.encode()).hexdigest()

#         cursor11.execute(
#             "INSERT INTO users12(username,password) VALUES(%s,%s)",
#             (username, hashed),
#         )
#         db11.commit()

#         return "User Registered with Hashed Password"

#     return """
#     <form method="post">
#         <input name="username" placeholder="Username"><br>
#         <input type="password" name="password" placeholder="Password"><br>
#         <button>Register</button>
#     </form>
#     """


# # ================= TASK 34 =================
# print("34. Implement role-based access (Admin/User).")


# @app11.route("/task34")
# def task34():
#     role = request.args.get("role")

#     if role == "admin":
#         return "Admin Access Granted"
#     elif role == "user":
#         return "User Access Granted"
#     return "Invalid Role"


# # ================= TASK 35 =================
# print("35. Add profile update page for logged-in user.")


# @app11.route("/task35/profile", methods=["GET", "POST"])
# def task35_profile():
#     if "user" not in session:
#         return "Login Required"

#     if request.method == "POST":
#         new_password = request.form["password"]
#         hashed = hashlib.sha256(new_password.encode()).hexdigest()

#         cursor11.execute(
#             "UPDATE users12 SET password=%s WHERE username=%s",
#             (hashed, session["user"]),
#         )
#         db11.commit()

#         return "Profile Updated Successfully"

#     return """
#     <form method="post">
#         <input type="password" name="password" placeholder="New Password">
#         <button>Update</button>
#     </form>
#     """


# # ================= TASK 36 =================
# print("36. Show total number of records using aggregate functions.")


# @app11.route("/task36")
# def task36():
#     cursor11.execute("SELECT COUNT(*) FROM employees_22")
#     total = cursor11.fetchone()[0]

#     return f"""
#     <link rel="stylesheet"
#     href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">

#     <div class="container mt-4">
#         <div class="card p-4 shadow">
#             <h3>Total Employees (employees_22)</h3>
#             <h1 class="text-primary">{total}</h1>
#         </div>
#     </div>
#     """


# # ================= TASK 37 =================
# print("37. Add validation both client-side and server-side.")


# @app11.route("/task37", methods=["GET", "POST"])
# def task37():
#     if request.method == "POST":
#         name = request.form["name"]
#         if len(name) < 3:
#             return "Name too short!"

#         return "Valid Data"

#     return """
#     <form method="post">
#         <input name="name" required minlength="3">
#         <button>Submit</button>
#     </form>
#     """


# # ================= TASK 38 =================
# print("38. Implement search + filter combination.")


# @app11.route("/task38")
# def task38():
#     dept = request.args.get("dept")
#     min_salary = request.args.get("min")

#     query = "SELECT * FROM employees_22 WHERE 1=1"
#     params = []

#     if dept:
#         query += " AND department=%s"
#         params.append(dept)

#     if min_salary:
#         query += " AND salary >= %s"
#         params.append(min_salary)

#     cursor11.execute(query, tuple(params))
#     data = cursor11.fetchall()

#     result = ""
#     for row in data:
#         result += f"{row[1]} - {row[2]} - ₹{row[3]}<br>"

#     return (
#         """
#     <form>
#         <input name="dept" placeholder="Department">
#         <input name="min" placeholder="Min Salary">
#         <button>Filter</button>
#     </form>
#     <br>
#     """
#         + result
#     )


# # ================= TASK 39 =================
# print("39. Add export to CSV functionality.")


# @app11.route("/task39/export")
# def task39_export():
#     cursor11.execute("SELECT * FROM employees_22")
#     data = cursor11.fetchall()

#     with open("employees_report.csv", "w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["ID", "Name", "Department", "Salary", "Created"])
#         writer.writerows(data)

#     return "CSV File Generated Successfully!"


# # ================= TASK 40 =================
# print("40. Create responsive reports page using Bootstrap cards.")


# @app11.route("/task40")
# def task40():
#     cursor11.execute("SELECT COUNT(*) FROM employees_22")
#     total = cursor11.fetchone()[0]

#     return f"""
#     <link rel="stylesheet"
#     href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">

#     <div class="container mt-4">
#         <div class="row">
#             <div class="col-md-4">
#                 <div class="card p-4 bg-primary text-white">
#                     <h4>Total Employees</h4>
#                     <h2>{total}</h2>
#                 </div>
#             </div>
#         </div>
#     </div>
#     """

# ================= REAL TIME MINI PROJECT 41 - 50 =================
from flask import session, redirect
import os

app11.secret_key = "supersecretkey"

# ================= TASK 41 =================
print("41. Mini E-commerce Product Listing")


@app11.route("/task41")
def task41():
    cursor11.execute("SELECT * FROM products21")
    products = cursor11.fetchall()

    result = "<h2>Product Listing</h2>"

    for p in products:
        result += f"""
        <div style='border:1px solid black;padding:10px;margin:10px;'>
        <b>{p[1]}</b><br>
        ₹{p[2]}<br>
        <a href="/task42/add/{p[0]}">Add to Cart</a>
        </div>
        """

    return result


# ================= TASK 42 =================
print("42. Shopping Cart (Session)")


@app11.route("/task42/add/<int:pid>")
def task42_add(pid):
    if "cart" not in session:
        session["cart"] = []

    session["cart"].append(pid)
    session.modified = True

    return redirect("/task43")


# ================= TASK 43 =================
print("43. Order Summary Page")


@app11.route("/task43")
def task43():
    cart = session.get("cart", [])
    total = 0
    result = "<h2>Cart Items</h2>"

    if not cart:
        return "Cart Empty"

    format_strings = ",".join(["%s"] * len(cart))
    cursor11.execute(
        f"SELECT * FROM products21 WHERE id IN ({format_strings})", tuple(cart)
    )
    products = cursor11.fetchall()

    for p in products:
        total += float(p[2])
        result += f"{p[1]} - ₹{p[2]}<br>"

    result += f"<h3>Total: ₹{total}</h3>"
    result += "<a href='/task44'>Confirm Order</a>"

    return result


# ================= TASK 44 =================
print("44. Store Orders in MySQL")


@app11.route("/task44")
def task44():
    cart = session.get("cart", [])

    if not cart:
        return "Cart Empty"

    for pid in cart:
        cursor11.execute(
            "INSERT INTO orders(user,product_id) VALUES(%s,%s)",
            ("guest", pid),
        )

    db11.commit()
    session.pop("cart", None)

    return "Order Placed Successfully!"


# ================= TASK 45 =================
print("45. Display Order History")


@app11.route("/task45")
def task45():
    cursor11.execute("SELECT * FROM orders")
    orders = cursor11.fetchall()

    result = "<h2>Order History</h2>"

    for o in orders:
        result += f"Order ID: {o[0]} | Product ID: {o[2]} | User: {o[1]}<br>"

    return result


# ================= TASK 46 =================
print("46. Admin Dashboard Manage Products")


@app11.route("/task46")
def task46():
    cursor11.execute("SELECT * FROM products21")
    products = cursor11.fetchall()

    result = "<h2>Admin Product Management</h2>"

    for p in products:
        result += f"""
        {p[1]} - ₹{p[2]}
        <a href='/task21/edit/{p[0]}'>Edit</a>
        <a href='/task21/delete/{p[0]}'>Delete</a>
        <br>
        """

    return result


# ================= TASK 47 =================
print("47. Image Upload for Products")

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app11.route("/task47/upload/<int:pid>", methods=["GET", "POST"])
def task47_upload(pid):
    if request.method == "POST":
        file = request.files["image"]
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)

        cursor11.execute(
            "UPDATE products21 SET image=%s WHERE id=%s",
            (path, pid),
        )
        db11.commit()

        return "Image Uploaded"

    return """
    <form method="post" enctype="multipart/form-data">
    <input type="file" name="image">
    <button>Upload</button>
    </form>
    """


# ================= TASK 48 =================
print("48. Show Statistics Dashboard")


@app11.route("/task48")
def task48():

    cursor11.execute("SELECT COUNT(*) FROM users12")
    total_users = cursor11.fetchone()[0]

    cursor11.execute("SELECT COUNT(*) FROM products21")
    total_products = cursor11.fetchone()[0]

    cursor11.execute("SELECT COUNT(*) FROM orders")
    total_orders = cursor11.fetchone()[0]

    return f"""
    <h2>Statistics</h2>
    Total Users: {total_users}<br>
    Total Products: {total_products}<br>
    Total Orders: {total_orders}<br>
    """


# ================= TASK 49 =================
print("49. Logout (Session Destroy)")


@app11.route("/logout")
def logout():
    session.clear()
    return "Logged Out Successfully <a href='/task31/login'>Login</a>"


# ================= TASK 50 =================
print("50. Project Structure Guide")


@app11.route("/task50")
def task50():
    return """
    <h2>Recommended Folder Structure</h2>

    project/
    ├── app.py
    ├── templates/
    ├── static/
    │    └── uploads/
    ├── database/
    └── requirements.txt
    """


if __name__ == "__main__":
    app11.run(debug=True, use_reloader=False)

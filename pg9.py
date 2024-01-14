import mysql.connector
class MyDatabase:
    def __init__(self):
        self.db = mysql.connector.connect(host="192.0.0.10", user="abhishek", passwd="1234", database="employee",auth_plugin="mysql_native_password")
        self.cur = self.db.cursor()
        self.create_table()

    def create_table(self):
        query = "CREATE TABLE IF NOT EXISTS employee (sino INT PRIMARY KEY,name VARCHAR(255),address VARCHAR(25),empcode VARCHAR(10),dateofbirth DATE,age INT,mobile VARCHAR(15),status VARCHAR(20),designation VARCHAR(50))"
        self.cur.execute(query)
        self.db.commit()

    def insert(self, sino, name, address, empcode, dob, age, mobile, status, designation):
        query = "INSERT INTO employee (sino, name, address, empcode, dateofbirth, age, mobile, status, designation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (sino, name, address, empcode, dob, age, mobile, status, designation)
        self.cur.execute(query, values)
        self.db.commit()
        print("Record inserted successfully")

    def modify(self, sino, new_designation):
        query = "UPDATE employee SET designation = %s WHERE sino = %s"
        values = (new_designation, sino)
        self.cur.execute(query, values)
        self.db.commit()
        print("Record modified successfully")

    def display_all(self):
        self.cur.execute("SELECT * FROM employee")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)

    def delete(self, sino):
        query = """
        DELETE FROM employee
        WHERE sino = %s
        """
        values = (sino,)
        self.cur.execute(query, values)
        self.db.commit()
        print("Record deleted successfully")

# Create an instance of the database
database = MyDatabase()

while True:
    print("Menu:")
    print("1. Insert Record")
    print("2. Modify Record")
    print("3. Display All Records")
    print("4. Delete Record")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sino = int(input("Enter SINO: "))
        name = input("Enter Name: ")
        address = input("Enter Address: ")
        empcode = input("Enter EmpCode: ")
        dob = input("Enter Date of Birth (YYYY-MM-DD): ")
        age = int(input("Enter Age: "))
        mobile = input("Enter Mobile: ")
        status = input("Enter Status: ")
        designation = input("Enter Designation: ")
        database.insert(sino, name, address, empcode, dob, age, mobile, status, designation)

    elif choice == "2":
        sino = int(input("Enter SINO of the record to modify: "))
        new_designation = input("Enter new Designation: ")
        database.modify(sino, new_designation)

    elif choice == "3":
        database.display_all()

    elif choice == "4":
        sino = int(input("Enter SINO of the record to delete: "))
        database.delete(sino)

    elif choice == "5":
        break

    else:
        print("Invalid choice. Please try again.")



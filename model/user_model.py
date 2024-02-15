import pyodbc
import json
from flask import make_response

class user_model():

    def  __init__(self):
        try:
            self.cnxn = pyodbc.connect("Driver={SQL Server};"
                        "Server=LAPTOP-K9QFULHI\SQLEXPRESS;"
                        "Database=RPA;"
                        "Trusted_Connection=yes;")
            # self.cursor = self.cnxn.cursor(dictionary=True)
            self.cursor = self.cnxn.cursor()
        except Exception as exp:
            print(exp)


    def enp_data(self):
        """ This method use to Fetch all data from [emp_details] table """
        try:
            result = self.cursor.execute('select * from emp_details;').fetchall()
            insertObject = []
            columnNames = [column[0] for column in self.cursor.description]
            if len(result) > 0:
                for record in result:
                    insertObject.append( dict( zip( columnNames , record ) ) )

                print(insertObject)
                # return json.dumps(insertObject)
                # return {'payload':insertObject}
                return make_response({'payload':insertObject}, 200)
            else:
                # return "No data found"
                # return {'message':"No data found"}
                return make_response({'message':"No data found"},201)
        except Exception as exp:
            print(exp)
            # return exp
            return {'message':exp}
        

    def emp_add(self, data):
        """ This method use to Insert data in [emp_details] table """
        try:
            query = f"INSERT INTO emp_details (First_name,Last_name,Department,Age) VALUES ('{data['First_name']}','{data['Last_name']}','{data['Department']}','{data['Age']}');"
            print(query)
            self.cursor.execute(query)
            self.cursor.commit()
            # return "Add emp in data base"
            return {'message':"Add emp in data base"}
        except Exception as exp:
            return {'message':exp}
            # return exp


    def emp_update(self, data):
        """ This method use to Update data in [emp_details] table """
        try:
            query = f"update emp_details set Last_name = '{data['Last_name']}', Department= '{data['Department']}', Age = '{data['Age']}' where First_name = '{data['First_name']}';"
            self.cursor.execute(query)
            self.cursor.commit()
            if self.cursor.rowcount > 0:
                return {'message':"Update Emp data Successfully"}
                # return "Update Emp data Successfully"
            else:
                return {'message':"Nothing to update"}
                # return "Nothing to update"
        except Exception as exp:
            return exp


    def emp_delete(self, name):
        query = f"delete from emp_details where First_name = '{name}';"
        self.cursor.execute(query)
        self.cursor.commit()
        if self.cursor.rowcount > 0:
            return {'message':"Delete Emp data Successfully"}
            # return "Delete Emp data Successfully"
        else:
            return {'message':"Nothing to delete"}
            # return "Nothing to delete"
        

    def emp_patch(self, data, name):
        query = f"update emp_details set "
        for key in data:
                query += f"{key} = '{data[key]}', "
        
        query = query[:-2]
        query = query + f" where  First_name = '{name}';"
        print(query)

        self.cursor.execute(query)
        self.cursor.commit()
        if self.cursor.rowcount > 0:
            return make_response({'message':"Update Emp data Successfully"}, 200)
            # return "Update Emp data Successfully"
        else:
            return {'message':"Nothing to update"}
            # return "Nothing to update"
        # return make_response({"message":"This is emp_patch"}, 200)

    def emp_pagination(self,limit,page_no):
        start = (int(page_no) * int(limit)) - int(limit)
        return make_response({'limit':limit,'start':start},200)
        


    def user_signup_model(self):
        return " Hello Ashish This user_signup_model"
    
    
        
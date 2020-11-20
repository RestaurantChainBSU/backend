from flask import request
from flask_restplus import Namespace, Resource, fields
from src.database.SQLConnector import SQLConnector
import json

api = Namespace("users", description="Users info part")
sql_conn = SQLConnector()

new_user = api.model("new_user",
{
        "id" : fields.Integer(required=True, description="User Id"),
     "login" : fields.String(required=True, description="User login"),
      "pass" : fields.String(required=True, description="User password"),
     "email" : fields.String(required=True, description="User email"),
"first_name" : fields.String(required=True, description="User first name"),
 "role_type" : fields.Integer(required=True, description="User role")
})

login_user = api.model("login_user",
{
     "login" : fields.String(required=True, description="User login"),
      "pass" : fields.String(required=True, description="User password")
})

@api.route('/')
class User(Resource):
    @api.doc("add_user", responses={400: "Missed required fields"})
    @api.expect(new_user)
    def post(self):
        """
        Inserts user in database
        """
        json_data = request.json

        required_fields = ['login', 'pass', 'email', 'first_name']
        check = set(required_fields).issubset({*json_data})
        print(check)
        if not check:
            return {'reason': 'not all the fields are provided'}, 400

        query = "INSERT into APP_USER (login, pass, email, first_name, role_type) values (" + \
                "'" + json_data["login"] + "'," + \
                "'" + json_data["pass"] + "'," + \
                "'" + json_data["email"] + "'," + \
                "'" + json_data["first_name"] + "'," + \
                "'" + "0" + "'" + \
                ")"
        res = sql_conn.execute_insert_update(query)
        return {'result': 'Successfully inserted'}


@api.route('/<login>/<passw>')
@api.param('login', 'User login')
@api.param('passw', 'User pass')
class User(Resource):
    @api.doc('check_user',  responses={404: 'No user with such login', 400: 'Wrong password'})
    @api.response(code=200, description="Success")
    def get(self, login, passw):
        """
        Check User login info
        """ 

        query = "SELECT * FROM APP_USER WHERE login='" + str(login) + "'" 
        res = sql_conn.execute_query(query)
        res = list(res)
        if res:
            res = res[0]
            if str(passw) == res[2]:
                return {'result': 'Successfully login'}
        return {'result': "False"}, 404


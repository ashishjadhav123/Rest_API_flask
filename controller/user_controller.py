from app import app
from model.user_model import user_model
from flask import request


obj = user_model()

# @app.route("/user/signup")
# def user_signup_controller():
#     return obj.user_signup_model()

@app.route("/user/emp_data")
def user_get_all_controller():
    return obj.enp_data()

@app.route("/user/add_data", methods=["POST"])
def uder_add():
    # print(request.form)
    return obj.emp_add(request.form)

@app.route("/user/update_data", methods=["PUT"])
def user_update():
    # print(request.form)
    return obj.emp_update(request.form)

@app.route("/user/delete_data/<name>", methods=["DELETE"])
def user_delete(name):
    return obj.emp_delete(name)

@app.route("/user/patch/<name>", methods=["PATCH"])
def user_patch_patch(name):
    return obj.emp_patch(request.form, name)

@app.route("/user/emp_data/limit/<limit>/page/<page_no>", methods=["GET"])
def user_pagination_controller(limit,page_no):
    return obj.emp_pagination(limit,page_no)
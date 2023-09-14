from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route("/ninjas")
def create_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template("ninja.html", all_dojos = dojos)



@app.route("/new_ninja", methods=['POST'])
def create_ninja_func():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo_list"]
    }

    Ninja.create_ninja(data)

    return redirect(f'/dojos/{request.form["dojo_list"]}')
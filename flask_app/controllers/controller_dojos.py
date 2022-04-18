from flask import render_template, request, redirect, session
from flask_app import app


from flask_app.models.model_dojos import Dojo


@app.route('/dojo', methods=['POST'])
def create_a_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/dojo')


@app.route('/dojo')
def dojo_result():
    get_all_dojos = Dojo.get_all_dojos_db()
    return render_template("dojos.html", all_dojos=get_all_dojos)


@app.route('/dojo/<int:id>')
def show_one_dojo(id):
    dojo_data = {
        "id": id
    }
    get_one_dojo = Dojo.get_dojo_with_ninjas(dojo_data)
    return render_template("dojo_show.html", one_dojo=get_one_dojo)

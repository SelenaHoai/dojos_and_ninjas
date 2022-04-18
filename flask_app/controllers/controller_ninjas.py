from flask import render_template, request, redirect, session
from flask_app import app


from flask_app.models.model_ninjas import Ninja
from flask_app.models.model_dojos import Dojo


@app.route('/ninja')
def create_ninja():
    get_all_dojos = Dojo.get_all_dojos_db()
    return render_template("new_ninja.html", all_dojos=get_all_dojos)


# @app.route('/ninja/<int:id>')
# def ninja_all_results():
#     show_ninjas = Ninja.create_all_ninja()
#     return render_template("dojo_show.html", all_ninjas=show_ninjas)

@app.route('/create', methods=['POST'])
def add_ninja_to_dojo():
    dojo_data = {
        "dojo_id": request.form["dojo_name_id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"]
    }
    Ninja.save(dojo_data)
    return redirect("/dojo")

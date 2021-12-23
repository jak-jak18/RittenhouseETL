from flaskr import get_model, model_mysql
from flask import Blueprint, request, render_template, current_app
from . import retl

crud = Blueprint('crud', __name__)

# create method that will insert data into preferred database
# used id to toggle between initial layout and actually creating entry
@crud.route('/create', methods=['GET', 'POST'])
def create():
    """CRUD create function. Initial function for app and used to create entries.
    Will add entry to db based on POST method.

    :return: returns template
    :rtype:
    """
    if request.method == 'POST':
        data = request.form.to_dict(flat=True)
        get_model().create(tuple(data.values()))

    return render_template("list.html")


# read method that will return all entries
@crud.route('/read')
def read():
    """CRUD read function. Retruns all entries.

    :return:
    :rtype:
    """
    books = get_model().read()
    return render_template("list.html", books=books)


# update method that will update entry based on id and new data
# author is provided first and then entry is updated
@crud.route('/update', methods=['GET', 'POST'])
def update():
    """CRUD update function. Updates entry. First input is book id then fields can be updated.

    :return: fields to update once author has been provided.
    :rtype:
    """
    if request.method == 'POST':
        data = request.form.to_dict(flat=True)
        if len(data) == 1:
            books = get_model().read('auth', data['id'])
            return render_template("list.html",
                                   update=books[0])
        else:
            get_model().update(tuple(data.values()))

    return render_template("list.html")


# delete method that will delete entry based on id
@crud.route('/delete', methods=['GET', 'POST'])
def delete():
    """CRUD delete function. Deletes entry based on id provided.

    :return:
    :rtype:
    """
    if request.method == 'POST':
        data = request.form.to_dict(flat=True)
        get_model().delete(data['id'])
    return render_template("list.html")


# etl method that returns table based on etl transform
@crud.route('/etl', methods=['GET', 'POST'])
def etl():
    """ETL function that manipulates data from db.

    :return: populates list.html with ordered data based on author
    :rtype:
    """
    # return render_template("list.html", etl=get_model().extract())
    return render_template("list.html", etl=retl.extract())

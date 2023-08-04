from flask import Flask, render_template, flash, redirect, url_for, request
from flask_mysqldb import MySQL
from wtforms import Form, validators, StringField, FloatField, IntegerField, DateField, SelectField
from datetime import datetime
import MySQLdb
import urllib
import requests

# Create instance of flask app
app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_DB'] = 'librarydb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Initialise MYSQL
mysql = MySQL(app)


# Homepage
@app.route('/')
def index():
    return render_template('home.html')


# Members
@app.route('/members')
def members():
    # Create MySQLCursor
    cur = mysql.connection.cursor()

    # Execute SQL Query
    result = cur.execute("SELECT * FROM members")
    members = cur.fetchall()

    # Render Template
    if result > 0:
        return render_template('members.html', members=members)
    else:
        msg = 'No Members Found'
        return render_template('members.html', warning=msg)

    # Close DB Connection
    cur.close()


# View Details of Member by ID
@app.route('/member/<string:id>')
def viewMember(id):
    # Create MySQLCursor
    cur = mysql.connection.cursor()

    # Execute SQL Query
    result = cur.execute("SELECT * FROM members WHERE id=%s", [id])
    member = cur.fetchone()

    # Render Template
    if result > 0:
        return render_template('view_member_details.html', member=member)
    else:
        msg = 'This Member Does Not Exist'
        return render_template('view_member_details.html', warning=msg)

    # Close DB Connection
    cur.close()


# Define Add-Member-Form
class AddMember(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    email = StringField('Email', [validators.length(min=6, max=50)])


# Add Member
@app.route('/add_member', methods=['GET', 'POST'])
def add_member():
    # Get form data from request
    form = AddMember(request.form)

    # To handle POST request to route
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data

        # Create MySQLCursor
        cur = mysql.connection.cursor()

        # Execute SQL Query
        cur.execute(
            "INSERT INTO members (name, email) VALUES (%s, %s)", (name, email))

        # Commit to DB
        mysql.connection.commit()

        # Close DB Connection
        cur.close()

        # Flash Success Message
        flash("New Member Added", "success")

        # Redirect to show all members
        return redirect(url_for('members'))

    # To handle GET request to route
    return render_template('add_member.html', form=form)


# Edit Member by ID
@app.route('/edit_member/<string:id>', methods=['GET', 'POST'])
def edit_member(id):
    # Get form data from request
    form = AddMember(request.form)

    # To handle POST request to route
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data

        # Create MySQLCursor
        cur = mysql.connection.cursor()

        # Execute SQL Query
        cur.execute(
            "UPDATE members SET name=%s, email=%s WHERE id=%s", (name, email, id))

        # Commit to DB
        mysql.connection.commit()

        # Close DB Connection
        cur.close()

        # Flash Success Message
        flash("Member Updated", "success")

        # Redirect to show all members
        return redirect(url_for('members'))

    # To handle GET request to route

    # To get existing field values of selected member
    cur2 = mysql.connection.cursor()
    result = cur2.execute("SELECT name,email FROM members WHERE id=%s", [id])
    member = cur2.fetchone()
    # To render edit member form
    return render_template('edit_member.html', form=form, member=member)


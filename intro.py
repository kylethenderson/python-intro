#lets start the python tutorial
print("Hello, world!")

#lets set some variables
myNum = 5
yourNum = 2

# basic conditional with print
if myNum > yourNum:
    print("This is from a true conditional")


#fizzbuzz in python

def fizzBuzz(num):
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)

fizzBuzz(15)
fizzBuzz(5)
fizzBuzz(3)
fizzBuzz(4)


# testing with flask

from flask import Flask
from flask import render_template

import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(host="localhost", database="python_intro")
cur = conn.cursor()

@app.route('/<id>')
def homePage(id):
    callback = 'Hail Caesar!'
    quietCallback = 'dressing'
    cur.execute('SELECT * FROM names WHERE id=%s;', (id))
    user = cur.fetchone()
    name = user[1]
    isAwesome = user[2]
    return render_template('index.html', callback=callback, second=quietCallback, name=name, isAwesome=isAwesome)

@app.route('/about')
def aboutPage():
    return render_template('about.html')


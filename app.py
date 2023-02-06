# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "alex"
    age = "12"

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
def father():

    name = "Mark"
    age = "40"

    return render_template('index.html' , name = name , age = age)


# define the route to mother webpage
def mother():

    name = "erica"
    age = "37"

    return render_template('index.html' , name = name , age = age)

# define the route to friends webpage
def friend():

    name = "victor"
    age = "12"

    return render_template('index.html' , name = name , age = age)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)

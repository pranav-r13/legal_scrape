
# # from distutils.log import debug
# # from flask import Flask,render_template, request, url_for
# # import time

# app = Flask(__name__)


# @app.route('/', methods=['POST','GET'])
# def index():
#     if request.method == 'POST':
#         name = request.form['name']
#         year_num = request.form['year']
#         try :
#             get_details(name,year_num)
#         except :
#             print("There was an error")

#     else:
#         return render_template('index.html')


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask,request,jsonify
from flask_graphql import GraphQLView

from models import db_session
from schema import schema

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)
# @app.route('/')
# def hello_world():
#     print("customers: ", d.query.all() )
#     return jsonify([d.query.all()])
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run()



# @app.route('/')
# def hello_world():
#     return 'Hello World!'
# db_user ={  "user":"santosh",
#     "password":"oracle",
#     "connectionString":"localhost:1521/xe"}
# @app.route('/')
# def index():
#     import ipdb
#     ipdb.set_trace()
#     connection = cx_Oracle.connect(db_user['user'],
#                                     db_user['password'],
#                                     db_user['connectionString'])
#     cur = connection.cursor()
#     cur.execute("select * from demo_customers")
#     col = cur.fetchone()
#     cur.close()
#     connection.close()
#     return "Hi"

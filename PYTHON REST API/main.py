from flask import Flask
from flask_restful import Api,Resource

app=Flask(__name__)
api=Api(app)

author={"shyam":{"age":69,"gender":"M"},
       "shy":{"age":59,"gender":"M"},
       "yam":{"age":21,"gender":"F"}}
book={"rich dad poor dad":{"author_name":"shyam","prize":566},
      "rich dad dad":{"author_name":"shy","prize":66}}

class Book(Resource):
    def get(self,name):
        return book[name]
    def put(self,book_name,author,prize):
        book[book_name]={"author_name": author,"prize": prize}

api.add_resource(Book,"/book/<string:name>")

if __name__== "__main__":
    app.run(debug=True)
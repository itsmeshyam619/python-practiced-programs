import requests

BASE = "http://127.0.0.1:5000/"
#book_name=input("name:")
data={key:author for key,author in input("enter book details :").split(',')}
#response=requests.post(BASE+"book/"+book_name,data)
#response=requests.get(f"{BASE}book/{book_name}")


#print(response.json())


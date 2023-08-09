from fastapi import FastAPI,Body


app= FastAPI()


books=[
    {'title': 'Cloud Computing','author':'Yazn Zamel','Category':'science'},
    {'title': ' Computing','author':' Zamel','Category':'IT'}
]

@app.get("/book")
async def first_api():
    return books


#static path parameter
@app.get("/book/book1")
async def sec():
    return books[1]

#dynamic path parameters
@app.get("/book/{dp}")
async def dp(dp):
    for i in books:
        if i['title']==dp:
            return i


@app.get("/allbooks")
async def all():
    return books


#POST method
@app.post("/book/create_book")
async def create(book=Body()):
    books.append(book)


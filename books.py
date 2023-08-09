from fastapi import FastAPI,Body


app= FastAPI()


books=[
    {'title': 'Cloud Computing','author':'Yazn Zamel','Category':'science'},
    {'title': ' Computing','author':' Zamel','Category':'IT'},
    {'title': ' grid Computing','author':'Yazn Zamel','Category':'science'}
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


@app.get("/book/getauth/{author}")
async def get_author(author:str):
    authorsbook=[]
    for i in books:
        if i.get('author').casefold() == author.casefold():
            authorsbook.append(i)
    return authorsbook
    
    


#POST method
@app.post("/book/create_book")
async def create(book=Body()):
    books.append(book)





#PUT 

@app.put("/book/update")
async def update_book(update=Body()):
    for i in range(len(books)):
        if books[i] .get('title').casefold() == update.get("title").casefold():
            books[i]= update


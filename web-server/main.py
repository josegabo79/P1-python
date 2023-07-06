import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return[1,2,3,4,5]


@app.get("/name")           # Para verlo en la web ----->  localhost:8080/contact
def get_list():
    return{"name": "José Gabriel Blandón"}


@app.get("/contact", response_class=HTMLResponse)
def get_list():
    return """
        <h1>Hola Soy una página web hecha por José Gabriel Blandón</h1> 
        <p>"Este es el parrafo"</p>  
    """


def run():
    store.get_categories()

if __name__ == '__main__':
    run()

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return [{'data': {'student': {'name': 'burak', 'age': 29}}}]

@app.get('/about')
def about():
    return {'data':{'About page'}}
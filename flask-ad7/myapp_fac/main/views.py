from myapp_fac.main import main

@main.route('/')
def index():
    return '<h1>Hello World from app factory!</h1>'
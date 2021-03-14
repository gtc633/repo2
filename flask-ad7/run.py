from myapp import app
from myapp_fac import create_app
import config

app1 = create_app('config')

# app.run(host='0.0.0.0', debug=True)
app1.run(host='0.0.0.0', debug=True)
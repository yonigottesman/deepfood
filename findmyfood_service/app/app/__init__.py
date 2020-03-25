from starlette.applications import Starlette

app = Starlette(debug=True)

from app import routes

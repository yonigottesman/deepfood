from starlette.applications import Starlette
#from urllib import request

# Download models from s3
#request.urlretrieve("https://deepfood.s3-us-west-2.amazonaws.com/saved_model.pt", "app/models/model.pt")
#request.urlretrieve("https://deepfood.s3-us-west-2.amazonaws.com/index.ann", "app/models/index.ann")

app = Starlette(debug=True)

from app import routes

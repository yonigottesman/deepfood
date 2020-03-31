from app import app
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from starlette.responses import PlainTextResponse, RedirectResponse,JSONResponse
from PIL import Image
import io
import base64


templates = Jinja2Templates(directory='app/templates')

@app.route('/',methods=['GET'])
async def homepage(request):
    return templates.TemplateResponse('index.html', {'request': request,
                                                     'categorizer':'Product'})

  
@app.route('/product/search',methods=['GET','POST'])
async def search(request):
    data = await request.form()
    
    content = data['image'].split(';')[1]
    image_encoded = content.split(',')[1]
    image_bytes = base64.decodebytes(image_encoded.encode('utf-8'))
    image = Image.open(io.BytesIO(image_bytes))

    # get image features
    # get similar images
    
    result = {'urls':['https://deepfood.s3-us-west-2.amazonaws.com/ifood/train_120206.jpg',
                      'https://deepfood.s3-us-west-2.amazonaws.com/ifood/train_120206.jpg',
                      'https://deepfood.s3-us-west-2.amazonaws.com/ifood/train_120206.jpg',
                      'https://deepfood.s3-us-west-2.amazonaws.com/ifood/train_120206.jpg',
                      'https://deepfood.s3-us-west-2.amazonaws.com/ifood/train_120206.jpg',
                      'https://deepfood.s3-us-west-2.amazonaws.com/ifood/train_120206.jpg']}

    return JSONResponse(result)


@app.exception_handler(404)
async def not_found(request, exc):
    """
    Return an HTTP 404 page.
    """
    template = "404.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context, status_code=404)    


@app.exception_handler(500)
async def server_error(request, exc):
    """
    Return an HTTP 500 page.
    """
    template = "500.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context, status_code=500)


from app import app
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from starlette.responses import PlainTextResponse, RedirectResponse,JSONResponse
from PIL import Image
import io
import base64
from app.extractor import extractor, ann_index
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles


templates = Jinja2Templates(directory='app/templates')
app.mount('/static', StaticFiles(directory='app/static'), name='static')

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
    embedding = extractor.get_embeddings(image)
    result_ids = ann_index.get_nns_by_vector(embedding, 9)
    urls = [f'https://deepfood.s3-us-west-2.amazonaws.com/ifood/{i}.jpg' for i in result_ids]
    
    result = {'urls':urls}

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



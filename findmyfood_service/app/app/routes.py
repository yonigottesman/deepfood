from app import app
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from starlette.responses import PlainTextResponse, RedirectResponse,JSONResponse

templates = Jinja2Templates(directory='app/templates')

@app.route('/',methods=['GET'])
async def homepage(request):
    return templates.TemplateResponse('index.html', {'request': request,
                                                     'categorizer':'Product'})
    
@app.route('/product/search',methods=['GET'])
async def search(request):
    pass
"""     domain = request.query_params.get('domain')
    domain = '' if domain is None else domain
    description = request.query_params.get('description')
    description = '' if description is None else description
    result = product_classifier.predict(domain, description)
    return JSONResponse(result)
 """



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


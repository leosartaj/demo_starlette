from starlette.applications import Starlette
from starlette.responses import PlainTextResponse, JSONResponse
import uvicorn
from datetime import datetime


app = Starlette(debug=True)


@app.route('/')
async def homepage(request):
    return PlainTextResponse('Hello World!')


@app.route('/echo/{text}')
async def echo(request):
    text = request.path_params['text']
    rtext = {'ECHO': text,
             'date': '{}'.format(datetime.now())}
    return JSONResponse(rtext)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

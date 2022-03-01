from aiohttp import web

# HTTP server

# Server Responses 
todos = [
    {"id":"1","title":"Insert Server's response to Client here."},
]

# Handler Function to send Responses 
async def handle(request):
    return web.json_response(todos)  # send a command

# Initilization Web Application 
app = web.Application()

# Set up routes with listeners
app.add_routes([web.get('/', handle),
        web.get('/todos', handle)])

# Starting the server
if __name__ == '__main__':
    web.run_app(app)
    
# Type 'python server.py' in command line to spin up server



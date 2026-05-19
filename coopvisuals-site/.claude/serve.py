import os, http.server, functools

port = int(os.environ.get('PORT', 3456))
directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=directory)
print(f"Serving {directory} on port {port}")
http.server.HTTPServer(('', port), handler).serve_forever()

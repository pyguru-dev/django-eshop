import json

from rest_framework import renderers

class UserRenderer(renderers.JSONRenderer):
    charset = 'utf-8'
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        if 'ErrorDetail' in str(data):
            response = json.dumps({'errors' : data})
        else:
            response = json.dumps(data)
        
        return response
    
class JPEGRenderer(renderers.BaseRenderer):
    media_type = 'image/jpeg'
    format = 'jpg'
    charset = None
    render_style = 'binary'
    
    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data
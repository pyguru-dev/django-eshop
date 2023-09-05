from apps.core.models import IPAddress
from utils.utils import get_ip_address


class SaveUserIPAddressMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    
    def __call__(self, request):
        
        ip = get_ip_address(request)
        
        try:
            ip_address = IPAddress.objects.get(ip_address=ip)
        except IPAddress.DoesNotExist:
            ip_address = IPAddress(ip_address=ip)
            ip_address.save()
        
        request.user.ip_address = ip_address
        
        response = self.get_response(request)
        
        return response
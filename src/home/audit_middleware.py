from django.contrib.auth import get_user_model
from django.utils import timezone

from .models import LoginLogoutLog

User = get_user_model()

class AuditMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self,request):
        if isinstance(request.user, User):
            LoginLogoutLog.objects.create(
                user=request.user,
                event_type="login" if request.user.is_authenticated else "logout",
                event_time=timezone.now(),
                ip_address=request.META.get('REMOTE_ADDR',''),
                user_agent=request.META.get('HTTP_USER_AGENT','')
            )
        
        response = self.get_response(request)
        return response
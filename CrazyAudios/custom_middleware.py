import logging

logger = logging.getLogger(__name__)

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("middleware executed")

        logger.info(f"Incoming request: {request.method} {request.path}")
        
            
        # Code to be executed for each request before the view (the view here is get_response)
        response = self.get_response(request)
        

        # Code to be executed for each response before returning to the client
        return response
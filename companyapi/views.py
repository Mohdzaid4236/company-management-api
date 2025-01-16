from django.http import HttpResponse

def home_page(request):
    print("Home page Requested ")
    return HttpResponse("This is Homepage")
from django.http import HttpResponse

def simpleserver(request):
    HttpResponseText="<form action=\"mycmd\" method=\"get\">LinuxShell command:<input type=\"text\" name=\"cmd\"><br /><input type=\"submit\" value=\"Submit\" /></form>"
    return HttpResponse(HttpResponseText)

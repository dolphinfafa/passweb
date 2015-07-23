#import from python

# #import from django
from django.http import HttpResponse
from django.shortcuts import render_to_response

#import from myproject


def main(request):
    return render_to_response('main.html')


def code(request):
    if 'plaintext' in request.GET and request.GET['plaintext'] and 'key' in request.GET and request.GET['key']:
        plaintext = request.GET['plaintext']
        key = request.GET['key']
        password = {}
        for i in range(len(plaintext)):
            password[i]=chr(ord(plaintext[i])+ord(key[i%len(key)])%5)
        message = ''.join(password.get(c) for c in password)
    else:
        message = 'plaintext and key cant be none'
    return HttpResponse(message)


def decode(request):
    if 'password' in request.GET and request.GET['password'] and 'key' in request.GET and request.GET['key']:
        password = request.GET['password']
        key = request.GET['key']
        plaintext = {}
        for i in range(len(password)):
            plaintext[i]=chr(ord(password[i])-ord(key[i%len(key)])%5)
        message = ''.join(plaintext.get(c) for c in plaintext)
    else:
        message = 'password and key cant be none'
    return HttpResponse(message)

# Create your views here.

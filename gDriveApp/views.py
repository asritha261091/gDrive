from django.shortcuts import render
from django.http import HttpResponse
'''from bs4 import BeautifulSoup'''
'''import numpy'''
import urllib.request as url
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

def fileUpload(filePath):
    try :
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None

    SCOPES = 'https://www.googleapis.com/auth/drive.file'
    store = file.Storage('../storage.json')
    print("##########")
    print(store)
    creds = store.get()

    if not creds or creds.invalid:
        print("make new storage data file ")
        flow = client.flow_from_clientsecrets('../client_secrets.json', SCOPES)
        if flags:
            creds = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            creds = tools.run(flow, store)

    DRIVE = build('drive', 'v3', http=creds.authorize(Http()))

    FILES = (
        ('marearts.png'),
    )

    for file_title in FILES :
        file_name = file_title
        metadata = {'name': file_name,'mimeType': None}

        res = DRIVE.files().create(body=metadata, media_body=file_name).execute()
        if res:
            print('Uploaded "%s" (%s)' % (file_name, res['mimeType']))
    return "success"

def getFilePath(request):
    if request.method == "POST":
        filePath = request.POST['textline']
        Message=fileUpload(filePath)
        Context = {
            'msg': Message
        }
    return render(request,'gDriveApp/Context.html',Context)

def index(request):
    return render(request,'gDriveApp/template.html')

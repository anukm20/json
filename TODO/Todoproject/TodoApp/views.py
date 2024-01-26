from django.shortcuts import render
import requests
# Create your views here.
def Home(request):
    urls='https://jsonplaceholder.typicode.com/posts'
    res=requests.get(urls)
    if res.status_code==200:
        data=res.json()
    return render(request,'index.html',{'data':data})



def Click(request,id):

    urls='https://jsonplaceholder.typicode.com/posts/'+str(id)
    res=requests.get(urls)
    if res.status_code==200:
        data=res.json()
    return render(request,'click.html',{'data':data})


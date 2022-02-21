from django.shortcuts import render


def home(request):
    return render(request, 'backendroot/test.html')

def test(request):
    if request.method=='POST':
        print(f'printing the request -> {request.POST["first_name"]}')
        return render(request, 'backendroot/test.html')
    elif request.method=='GET':
        return render(request, 'backendroot/test.html')

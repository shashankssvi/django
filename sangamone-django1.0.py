import os

dproject=input("Enter the django project name: ")
dapp=input("Enter the django app name: ")
try:
    assert f'{dapp}' in os.listdir(f'{dproject}') and f'{dproject}' in os.listdir('./')
    os.chdir(dproject)
    os.chdir(f"./{dproject}")
    f1=open("settings.py","r+")
    info1=f1.read()
    if f"{dapp}'," not in info1:
        a=info1.replace("'django.contrib.staticfiles',",f"'django.contrib.staticfiles',\n\t'{dapp}',")
        f1.seek(0)
        f1.write(a)
    f1.close()

    f1=open("urls.py","r+")
    info1=f1.read()
    if f"{dapp}.urls" not in info1 and "from django.urls import path,include" not in info1:
        any1=info1.replace("path('admin/', admin.site.urls),",f"""path('admin/', admin.site.urls),\n\tpath("{dapp}/" ,include("{dapp}.urls")),""").replace("from django.urls import path","from django.urls import path,include")
        f1.seek(0)
        f1.write(any1)
    else:
        if f"""include("{dapp}.urls")""" not in info1:
            any1=info1.replace("path('admin/', admin.site.urls),",f"""path('admin/', admin.site.urls),\n\tpath("{dapp}/" ,include("{dapp}.urls")),""")
            f1.seek(0)
            f1.write(any1)
        else:
            pass
    f1.close()
    
    os.chdir(f"../{dapp}")
    f1=open("views.py","w")
    any="""from django.shortcuts import render
def home(request):
    return render(request,'"""+dapp+"""/index.html',{'param1':"hello world"})"""
    f1.write(any)
    f1.close()

    open('urls.py','w')
    f1=open("urls.py","r+")
    if "urlpatterns = [" not in f1.read():
        f1.write(f"from django.urls import path\nfrom {dapp}.views import home\nurlpatterns = [\n\tpath('', home),]")
    else:
        a=f1.read().replace("urlpatterns = [",f"urlpatterns = [\n\tpath('', home),").replace("from django.urls import path",f"from django.urls import path\nfrom {dapp}.views import home")
        f1.seek(0)
        f1.write(a)
    # else:
    #     for i in range(1,100,1):
    #         if f"/{i}" in f1.read():
    #             continue
    #         else:
    #             a=f1.read().replace("urlpatterns = [",f"urlpatterns = [\n\tpath('{i}', home),").replace("from django.urls import path",f"from django.urls import path\nfrom {dapp}.views import home")
    #             f1.seek(0)
    #             f1.write(a)
    #             break
    f1.close()
    
    if not os.path.exists(f"templates/{dapp}"):
        os.makedirs(f"templates/{dapp}")
    os.chdir(f"templates/{dapp}")
    f1=open("index.html","w")
    f1.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p>Hello World</p>
    <p>{{param1}}</p>
</body>
</html>
""")
    f1.close()
except AssertionError:
    list1 = os.listdir(f'{dproject}')
    list1.remove('db.sqlite3')
    list1.remove('manage.py')
    list1.remove(f'{dproject}')
    print(f'You have {list1} apps in your project')
    print("App not created or check wether the app is created inside the project")
    print(f"run command 'django-admin startapp {dapp}'")

except FileNotFoundError:
        print(f"project name '{dproject}' not found")


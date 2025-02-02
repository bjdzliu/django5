from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse as HTTPResponse
import os

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return redirect('/static/error.html')

def blog(request,id):
    if id == 0:
        return redirect('/static/error.html')
    else:
        return HTTPResponse('博客的id是：%s' % id)

def blog2(request,year,month,day,id):
    return HTTPResponse(str(year)+'/'+str(month)+'/'+str(day)+'/'+' id是' +str(id)+"的博客")

def download_file1(request):
    current_path = os.path.abspath(os.path.dirname(__file__))
    parent_path = os.path.dirname(current_path)

    file = open(f'{parent_path}/files/file1.txt', 'rb')
    response = HTTPResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="test.txt"'
    return response

def get_info(request):
    print(request.GET)
    print(request.GET.get('name'))
    response_html=f"<html><h1>姓名：{request.GET.get('name')}</h1></html>"
    return HTTPResponse(response_html)


def update_info(request):
    print(request.POST)
    print("user name is ",request.POST.get('username'))
    print(request.POST.get('password'))
    return HTTPResponse('更新信息')


def tologin(request):
    return render(request,'login.html')


def login(request):
    username=request.POST.get('username')
    print("request.session.session_key:",request.session.session_key)
    #判断session中是否有登录信息
    if request.session.get('current_user') == 'liudz':
        print("登录信息已经存在，有session")
        return render(request,'main.html')
    #判断用户名和密码是否正确
    if username == 'liudz' and request.POST.get('password') == '123456':
        #在用户端生成了一个session id,并且保存在了浏览器的cookie中
        #服务器将session id和session数据保存在了服务器端，具体位置在django_session表中
        request.session['current_user'] = username
        #add a cookie to the response
        
        context_dict = {'username':username}
        response=render(request,'main.html')
        response.set_cookie('username_add_cookie2',username)
        return response
    else:
        context_dict = {'login_result':"username or password is wrong"}
        return render(request,'login.html',context_dict)

def upload(request):
    if request.method == 'POST':
        #获取文件对象
        file_obj = request.FILES.get('file')
        #获取文件名
        file_name = file_obj.name
        #获取文件内容
        file_content = file_obj.read()
        #将文件内容写入到文件中
        with open(file_name,'wb') as f:
            f.write(file_content)
        return HTTPResponse('上传成功')
    return render(request,'upload.html')
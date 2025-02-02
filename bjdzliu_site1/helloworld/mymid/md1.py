from django.utils.deprecation import MiddlewareMixin

#自定义中间件
#在请求views之前和之后做一些操作
class Md1(MiddlewareMixin):
    def process_request(self,request):
        print('request请求来了')

    def process_response(self,request,response):
        print('请求处理完毕，将页面返回')
        return response
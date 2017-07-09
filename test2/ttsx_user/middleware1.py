
class UrlPathMiddleware():
    def process_view(self,request, view_func, view_args, view_kwargs):
        if request.path not in ['/info/','/order/','/site/']:
            request.session['url_path']=request.get_full_path()

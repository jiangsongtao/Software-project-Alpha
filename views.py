from django.shortcuts import render
from imgupload.models import IMG


def uploadImg(request):
    """
    图片上传
    :param request:
    :return:
    """
    if request.method == 'POST':
        new_img = IMG(
            img=request.FILES.get('img'),
            name=request.FILES.get('img').name
        )
        new_img.save()
    return render(request, 'app1/uploading.html')


def showImg(request):
    """
    图片显示
    :param request:
    :return:
    """
    imgs = IMG.objects.all()
    content = {
        'imgs': imgs,
    }
    for i in imgs:
        print(i.img.url)
    return render(request, 'app1/showing.html', content)

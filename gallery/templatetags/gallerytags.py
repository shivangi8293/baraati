from django import template
from gallery.models import ImageFilterDtl,ImageGallery
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

register=template.Library()

@register.simple_tag
def getImageFilter():
    imageFilter=ImageFilterDtl.objects.filter(filter_id__active_flag=1).select_related().order_by('filter_id__filter_order')
    return imageFilter

@register.simple_tag
def getImageFromPage(lists):
    images=list(lists)[0]
    return images

@register.simple_tag
def getPage(lists):
    page=list(lists)[1]
    return page

@register.simple_tag()
def getImageFromTags(image_tag,request):
    image=ImageGallery.objects.filter(filter_id__filter_id__filter_tag__exact=str(image_tag)).select_related()
    print image
    if len(image) > 0:
        print 'insode'
        pagination_list=[]
        paginator=Paginator(image,1)
        page=int(request.GET.get('page','1'))

        try:
            images=paginator.page(page)
        except PageNotAnInteger:
            images=paginator.page(1)
        except EmptyPage:
            images=paginator.page(paginator.num_pages)
        pagination_list.append(images)
        pagination_list.append(page)
        return pagination_list
    else:
        return None


from django import template
from homepage.models import NavMenuDtls,PanelDtl, RecentEventsCardDtl

register=template.Library()

@register.simple_tag
def getChildMenu(parentId):
    childMenu = NavMenuDtls.objects.filter(navMenuId__parentNavMenu=str(parentId)).select_related().order_by('navMenuId__navOrder')
    if len(childMenu)>0:
        return childMenu
    else:
        return None

@register.simple_tag
def getNavigationMenus():
    navigation_menus = NavMenuDtls.objects.filter(navMenuId__activeFlag=1).select_related().order_by('navMenuId__navOrder')
    return  navigation_menus

@register.simple_tag
def getPanels(panel_key):
    panel_list=PanelDtl.objects.filter(panel_id__panel_key__exact=str(panel_key)).filter(panel_id__activeFlag=1).select_related().order_by('panel_id__panel_order')
    return panel_list

@register.simple_tag
def getEventCards(event_key):
    event_list=RecentEventsCardDtl.objects.filter(recent_events_card_id__event_key=str(event_key)).filter(recent_events_card_id__activeFlag=1).select_related().order_by('recent_events_card_id__card_order')
    return event_list
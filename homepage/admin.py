# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import NavMenuMst,NavMenuDtls,PanelDtl,PanelMst, RecentEventsCardMst, RecentEventsCardDtl

admin.site.register(NavMenuMst)
admin.site.register(NavMenuDtls)
admin.site.register(PanelDtl)
admin.site.register(PanelMst)
admin.site.register(RecentEventsCardMst)
admin.site.register(RecentEventsCardDtl)
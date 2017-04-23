# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField

class NavMenuMst(models.Model):
    parentNavMenu=models.IntegerField(default=-1)
    navOrder=models.IntegerField(default=0)
    activeFlag=models.IntegerField(default=1)
    urlPageName=models.CharField(max_length=250,blank=True)

    def __unicode__(self):
        return str(self.pk)


class NavMenuDtls(models.Model):
    navMenuId=models.ForeignKey(NavMenuMst)
    navMenuName = models.CharField(max_length=250)
    navMenuTooltip=models.CharField(max_length=250)
    langId=models.IntegerField(default=1)

    def __unicode__(self):
        return self.navMenuName


class PanelMst(models.Model):
    panel_key=models.CharField(max_length=250)
    panel_order=models.IntegerField(default=0)
    activeFlag = models.IntegerField(default=1)
    panel_width=models.IntegerField(default=4)
    panel_offset=models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.pk)

class PanelDtl(models.Model):
    panel_id=models.ForeignKey(PanelMst)
    panel_header=models.CharField(max_length=250)
    panel_body= RichTextField()
    panel_footer=models.CharField(max_length=250,blank=True)
    langId = models.IntegerField(default=1)

    def __unicode__(self):
        return self.panel_header

class RecentEventsCardMst(models.Model):
    event_key=models.CharField(max_length=250)
    card_order = models.IntegerField(default=0)
    activeFlag = models.IntegerField(default=1)
    card_width = models.IntegerField(default=3)
    card_offset = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.pk)

class RecentEventsCardDtl(models.Model):
    recent_events_card_id = models.ForeignKey(RecentEventsCardMst)
    event_image_path = models.ImageField(null=True)
    image_name = models.CharField(max_length=250)
    profile_image_path = models.ImageField(null=True)
    profile_image_name = models.CharField(max_length=250,null=True)
    event_title= models.CharField(max_length=250)
    event_body = RichTextField()
    event_body_back = RichTextField(null=True)
    event_footer = models.CharField(max_length=250, blank=True)
    langId = models.IntegerField(default=1)

    def __unicode__(self):
        return str(self.pk)
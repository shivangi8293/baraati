# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class ImageFilterMst(models.Model):
    filter_tag=models.CharField(max_length=250,default="")
    filter_order=models.IntegerField(default=0)
    active_flag=models.IntegerField(default=1)

    def __unicode__(self):
        return str(self.pk)


class ImageFilterDtl(models.Model):
    filter_id=models.ForeignKey(ImageFilterMst)
    filter_name=models.CharField(max_length=250)
    filter_tooltip=models.CharField(max_length=250,blank=True)
    lang_id=models.IntegerField(default=1)

    def __unicode__(self):
        return str(self.filter_name)


class ImageGallery(models.Model):
    filter_id=models.ForeignKey(ImageFilterDtl)
    image_name=models.CharField(max_length=250)
    image_path=models.ImageField()

    def __unicode__(self):
        return str(self.image_name)
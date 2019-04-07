#!/usr/bin/env python3
#
#
# Copyright (c) 2019, Daiki Matsui.
# All rights reserved.
# 
# $Id: $
# 

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

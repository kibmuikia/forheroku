# -*- coding: utf-8 -*-
from __future__ import unicode_literals

	# import generic views
from django.views.generic import View, TemplateView

from django.shortcuts import render, redirect, HttpResponse

class indexView( View ):

	def get( self, request, *args, **kwargs ):
		return HttpResponse( 'Karibu kwenye mtandao wa web development. subiri upate mlo' )
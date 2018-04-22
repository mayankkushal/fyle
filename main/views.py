from django.shortcuts import render

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse

from .models import *
# Create your views here.

class IFSCView(APIView):
	"""
	Endpoint accepts POST request with `ifsc`.
	"""
	parser_classes = (JSONParser,)

	def post(self, request, format=None):
		ifsc = request.data.get('ifsc')

		branch = Branch.objects.get(ifsc=ifsc)

		content = {
			'ifsc': branch.ifsc,
			'bank': branch.bank.name,
			'branch': branch.branch,
			'address': branch.address,
			'city': branch.city,
			'discrict': branch.district,
			'state': branch.state,
		}
		return Response(content)


class NameView(APIView):
	"""
	Endpoint accepts POST request with name and city.
	"""
	parser_classes = (JSONParser,)

	def post(self, request, format=None):
		name = request.data.get('name')
		city = request.data.get('city')

		bank = Bank.objects.get(name=name)
		branches = Branch.objects.filter(bank=bank, city=city)

		details = []
		for branch in branches:
			details.append({
				'ifsc': branch.ifsc,
				'bank': branch.bank.name,
				'branch': branch.branch,
				'address': branch.address,
				'city': branch.city,
				'discrict': branch.district,
				'state': branch.state,
				})

		content = {
			'details':details,
		}
		return Response(content)
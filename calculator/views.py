from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
class Addview(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1+n2
        return Response({"msg":res})


class Subview(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1-n2
        return Response({"msg":res})


class Productview(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1*n2
        return Response({"msg":res})


class Squareview(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        n1=request.data.get("num1")
        res=n1*n1
        return Response({"msg":res})


class Cubeview(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        n2=request.data.get("num2")
        res=n2*n2*n2
        return Response({"msg":res})
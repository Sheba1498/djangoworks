from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime

class GoodNight(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"Good Night"})

class GoodMorning(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"Good Morning"})


class GoodAfternoon(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"Good Afternoon"})





class Greetings(APIView):
    def get(self,request,*args,**kwargs):
        cur_date=datetime.now()
        c_hour=cur_date.hour
        greetings=""
        if c_hour<12:
            greetings="Good Morning"
        elif c_hour<18:
            greetings="Good Afternoon"
        elif c_hour<24:
            greetings="Good Evening"
        return Response({"msg":greetings})

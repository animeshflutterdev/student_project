import io

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Student
from .serializers import StudentSerializer


@method_decorator(csrf_exempt, name="dispatch")
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        # print(f"stream --> {stream}")
        pyData = JSONParser().parse(stream)
        # print(f"PYDATA --> {pyData}")
        _id = pyData.get("id", None)
        # print(f"_id --> {_id}")
        if _id is not None:
            stu = Student.objects.get(id=_id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type="application/json")
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type="application/json")

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pyData = JSONParser().parse(stream)
        # print(f"PyData = {pyData}")
        serializer = StudentSerializer(data=pyData)
        # print(f"StudentSerializer = {serializer}")
        if serializer.is_valid():
            serializer.save()
            res = {"msg": f"Data saved as `{serializer.data['name']}`"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pyData = JSONParser().parse(stream)
        # print(f"PyData = {pyData}")
        _id = pyData.get("id")
        stu = Student.objects.get(id=_id)
        # print(f"Student.objects = {stu}")
        '''
        partial=True --- you can update partially, not required all data
        partial=False(Default) --- you have to update the full Model class
        '''
        serializer = StudentSerializer(stu, data=pyData, partial=True)
        print(f"StudentSerializer = {serializer}")
        if serializer.is_valid():
            serializer.save()
            res = {"msg": f"Data updated as `{serializer.data['name']}`"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pyData = JSONParser().parse(stream)
        # print(f"PyData = {pyData}")
        _id = pyData.get("id")
        stu = Student.objects.get(id=_id)
        # print(f"Student.objects = {stu}")
        ''' Hard Delete of User '''
        stu.delete()
        res = {"msg": f"Data Deleted !!"}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type="application/json")

# def student_detail(request, stuID):
#     if request.method == "GET":
#         stu = Student.objects.get(id=stuID)
#         serializer = StudentSerializer(stu)
#         # json_data = JSONRenderer().render(serializer.data)
#         # return HttpResponse(json_data, content_type="application/json")
#         return JsonResponse(serializer.data)
#
#
# def all_student(request):
#     if request.method == "GET":
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         # json_data = JSONRenderer().render(serializer.data)
#         # return HttpResponse(json_data, content_type="application/json")
#         return JsonResponse(serializer.data, safe=False)
#
#
# @csrf_exempt
# def create_student(request):
#     if request.method == "POST":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pyData = JSONParser().parse(stream)
#         print(f"PyData = {pyData}")
#         serializer = StudentSerializer(data=pyData)
#         print(f"StudentSerializer = {serializer}")
#         if serializer.is_valid():
#             serializer.save()
#             res = {"msg": f"Data saved {serializer.data}"}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type="application/json")
#         else:
#             json_data = JSONRenderer().render(serializer.errors)
#             return HttpResponse(json_data, content_type="application/json")
#     else:
#         res = {"msg": f"This is not {request.method}"}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type="application/json")
#
#
# @csrf_exempt
# def student_api(request):
#     if request.method == "GET":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         print(f"stream --> {stream}")
#         pyData = JSONParser().parse(stream)
#         print(f"PYDATA --> {pyData}")
#         _id = pyData.get("id", None)
#         print(f"_id --> {_id}")
#         if _id is not None:
#             stu = Student.objects.get(id=_id)
#             serializer = StudentSerializer(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type="application/json")
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type="application/json")
#
#     if request.method == "POST":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pyData = JSONParser().parse(stream)
#         print(f"PyData = {pyData}")
#         serializer = StudentSerializer(data=pyData)
#         print(f"StudentSerializer = {serializer}")
#         if serializer.is_valid():
#             serializer.save()
#             res = {"msg": f"Data saved as `{serializer.data['name']}`"}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type="application/json")
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type="application/json")
#
#     if request.method == "PUT":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pyData = JSONParser().parse(stream)
#         print(f"PyData = {pyData}")
#         _id = pyData.get("id")
#         stu = Student.objects.get(id=_id)
#         print(f"Student.objects = {stu}")
#         '''
#         partial=True --- you can update partially, not required all data
#         partial=False(Default) --- you have to update the full Model class
#         '''
#         serializer = StudentSerializer(stu, data=pyData, partial=True)
#         print(f"StudentSerializer = {serializer}")
#         if serializer.is_valid():
#             serializer.save()
#             res = {"msg": f"Data updated of `{serializer.data['name']}`"}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type="application/json")
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type="application/json")
#
#     if request.method == "DELETE":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pyData = JSONParser().parse(stream)
#         print(f"PyData = {pyData}")
#         _id = pyData.get("id")
#         stu = Student.objects.get(id=_id)
#         print(f"Student.objects = {stu}")
#         ''' Hard Delete of User '''
#         stu.delete()
#         res = {"msg": f"Data Deleted !!"}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type="application/json")

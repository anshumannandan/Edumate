from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import *
from account.models import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from teacher.views import return_user
from datetime import date

# 1- API for viewing the own profile (student profile)


class SProfileDetails(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = return_user(request)
        student = get_object_or_404(Student, user=user)
        data = StudentProfileSerializer(student, many=False).data
        data.update(EmailSerializer(user, many=False).data)
        return Response(data)

    def put(self, request):
        user = return_user(request)
        student = get_object_or_404(Student, user=user)
        serializer = StudentProfileSerializer(student, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # Updating the name in User Model
        name = serializer.validated_data.get('name')
        user.name = name
        user.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

# 2- API for giving feedback to the teacher


class TeacherFeedbackView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = return_user(request)
        student = get_object_or_404(Student, user=user)
        feedbacks = request.data
        for feedback in feedbacks:
            teacher = get_object_or_404(Teacher, userID=feedback["userID"])
            thisfeedback = TeacherFeedback.objects.filter(
                teacher=teacher, student=student)
            if thisfeedback.exists():
                thisfeedback = thisfeedback[0]
                thisfeedback.feed = feedback["feed"]
                thisfeedback.save()
            else:
                TeacherFeedback(teacher=teacher, student=student,
                                feed=feedback["feed"]).save()
        return Response({'msg': 'Feedback Submitted Successfully !!'}, status=status.HTTP_200_OK)


TIME_SLOTS = ['8:30 - 9:20', '9:20 - 10:10',
              '11:00 - 11:50', '11:50 - 12:40', '1:30 - 2:20']
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']


# 3- API for getting the details of his/her class TimeTable
class TimeTable(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = return_user(request)
        student = get_object_or_404(Student, user=user)
        pk = student.class_id.id
        list = []
        for i in TIME_SLOTS:
            for j in DAYS:
                time = AssignTime.objects.filter(
                    period=i, day=j, assign__class_id=pk)

                if time.exists():
                    time = time[0]
                    dict = {}
                    dict = {"class": time.assign.class_id.id, "subject": time.assign.subject.name,
                            "teacher": time.assign.teacher.name, "period": i, "day": j}
                else:
                    dict = {}
                    dict = {"class": pk, "subject": "",
                            "teacher": "", "period": i, "day": j}
                list.append(dict)
        return Response(list,  status=status.HTTP_200_OK)

# 4- API for getting Overall attendance of student


class StudentOverallAttendance(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = return_user(request)
        student = get_object_or_404(Student, user=user)
        class_id = student.class_id
        subjects = AssignClass.objects.filter(class_id=class_id)
        list = []
        for subject in subjects:
            subject_name = subject.subject.name
            subject_code = subject.subject.code

            total_classes = StudentAttendance.objects.filter(classattendance__assign__class_id=class_id,
                                                             subject__code=subject_code,
                                                             classattendance__status=True,
                                                             student__userID=student.userID).count()

            attended_classes = StudentAttendance.objects.filter(classattendance__assign__class_id=class_id,
                                                                subject__code=subject_code,
                                                                classattendance__status=True,
                                                                student__userID=student.userID,
                                                                is_present=True).count()

            if total_classes == 0:
                attendance_percent = 0
            else:
                attendance_percent = round(
                    attended_classes / total_classes * 100, 1)
            dict = {}
            dict = {
                "subject_code": subject_code,
                "subject_name": subject_name,
                "attended_classes": attended_classes,
                "total_classes": total_classes,
                "attendance_percent": attendance_percent
            }
            list.append(dict)
        return Response(list, status=status.HTTP_200_OK)

# 5- API for fetching attendance of a particular subject of a student


class StudentSubjectAttendance(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, subject_code, month):
        user = return_user(request)
        student = get_object_or_404(Student, user=user)
        attendances = StudentAttendance.objects.filter(subject__code=subject_code,
                                                       student=student,
                                                       classattendance__date__month=month,
                                                       classattendance__date__year=date.today().year,
                                                       classattendance__status=True)
        list = []
        for attendance in attendances:
            dict = {}
            dict = {
                "date": attendance.classattendance.date,
                "day": attendance.classattendance.assign.day,
                "period": attendance.classattendance.assign.period,
                "is_present": attendance.is_present
            }
            list.append(dict)
        return Response(list, status=status.HTTP_200_OK)

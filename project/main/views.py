from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'main/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'main/course_detail.html', {'course': course})

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'main/lesson_detail.html', {'lesson': lesson})

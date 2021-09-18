
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from .models import Student
from .forms import StudentForm

# 这个文件主要是定义视图
def index(request):
	students = Student.objects.all()
	# 通过post提交的方式
	if request.method == 'POST':
		form = StudentForm(request.POST)
		# 如果表单存在值的情况下
		if form.is_valid():
			cleaned_data = form.cleaned_data
			student = Student()
			student.name = cleaned_data['name']
			student.sex = cleaned_data['sex']
			student.email = cleaned_data['email']
			student.profession = cleaned_data['profession']
			student.qq = cleaned_data['qq']
			student.phone = cleaned_data['phone']
			student.save()
			# 返回http请求展示在index上（index就是主页）
			return HttpResponseRedirect(reverse('index'))
	else:
		# 如果表单没有有效的值不提交
		form = StudentForm()

	context = {
		'students': students,
		'form': form,
	}
	return render(request, 'index.html', context=context)
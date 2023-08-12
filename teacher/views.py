from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher, Comment
from .forms import TeacherForm, CommentForm
from django.urls import reverse

# Create your views here.

def t_main(request):
    teachers = Teacher.objects.all()
    content = {'teachers':teachers}
    return render(request, 't_main.html', content)

def t_c(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.user = request.user
            teacher.save()
            return redirect('t_r', pk=teacher.pk)
        
    else:
        form = TeacherForm()
    content = {'form': form}
    return render(request, 't_c.html', content)



def t_r(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user == teacher.user:
               teacher.delete()
               return redirect('t_main')
        return redirect('t_main')
    else:
        commentform = CommentForm()
        comment = teacher.comment_set.all
        content = {'teacher': teacher, 'commentform':commentform, 'comment':comment}
        return render(request, 't_r.html', content)
    

def t_u(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.user == teacher.user:
        if request.method == 'POST':
            form = CommentForm(request.POST, request.FILES, instance=teacher)
            if form.is_valid():
                form.save()
                return redirect('t_r', pk=teacher.pk)
        else:
            form = TeacherForm(instance=teacher)
        content = {'teacher': teacher, 'form': form, }
        return render(request, 't_u.html', content)
    else:
        return redirect('t_main')


def comment_create(request,pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.teacher = teacher
            comment.user = request.user
            comment.save()
        return redirect('t_r', teacher.pk)



def comment_delete(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        teacher_pk = comment.teacher_id  # 댓글이 연결된 teacher의 pk 값
        comment.delete()
    return redirect(reverse('t_r', kwargs={'pk': teacher_pk}))
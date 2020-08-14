from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Project, UserProfile
from .forms import ProjectForm
from django.contrib.auth.models import User
# Create your views here.


def homePage(request):

    if not request.user.is_authenticated:
        user = User.objects.get(username='Anonymous')
        userProfile = user.userprofile
    else:
        userProfile = request.user.userprofile

    projects = Project.objects.filter(userProfile=userProfile)
    return render(request, 'homePage.html', {'projects': projects, 'userProfile': userProfile})


def detailPage(request, project_id):
    if not request.user.is_authenticated:
        user = User.objects.get(username='Anonymous')
        userProfile = user.userprofile
    else:
        userProfile = request.user.userprofile

    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'detailPage.html', {'project': project, 'userProfile': userProfile})


def createPage(request):
    if not request.user.is_authenticated:
        user = User.objects.get(username='Anonymous')
        userProfile = user.userprofile
    else:
        userProfile = request.user.userprofile

    createForm = ProjectForm()
    if request.method == 'POST':
        createForm = ProjectForm(request.POST, request.FILES)
        if createForm.is_valid():
            temp = createForm.save(commit=False)
            temp.userProfile = request.user.userprofile
            temp.save()  # assign userProfile to the project
            print("create successful")
            return redirect('homePage')
        else:
            print("invalid form, fill in again...")
    return render(request, 'createPage.html', {'createForm': createForm, 'userProfile': userProfile})


def editPage(request, project_id):
    if not request.user.is_authenticated:
        user = User.objects.get(username='Anonymous')
        userProfile = user.userprofile
    else:
        userProfile = request.user.userprofile

    project = get_object_or_404(Project, pk=project_id)
    editForm = ProjectForm(instance=project)
    if request.method == 'POST':
        editForm = ProjectForm(request.POST, request.FILES, instance=project)
        if editForm.is_valid():
            editForm.save()
            print("edit successful")
            return redirect('homePage')
        else:
            print("invalid form, fill in again...")
    return render(request, 'editPage.html', {'editForm': editForm, 'userProfile': userProfile})


def deleteProject(request, project_id):
    if not request.user.is_authenticated:
        user = User.objects.get(username='Anonymous')
        userProfile = user.userprofile
    else:
        userProfile = request.user.userprofile

    Project.objects.get(pk=project_id).delete()
    return redirect('homePage')

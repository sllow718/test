from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from .models import addresources, addmatchingresources, editresources, Technologies
from .models import generate_adjacency_map, traverse
from .forms import addresourcesForm, addmatchingresourcesForm, editresourcesForm, TechnologiesForm, UserForm
from django.db.models import Q

from django import forms
from addresources.models import addresources


def create_addresources(request):
    form = addresourcesForm(request.POST or None)

    if form.is_valid():
        inputresource = addresources.objects.all()
        for i in inputresource:
            if i.HS_Code == form.cleaned_data.get("HS_Code"):
                context = {
                    'form': form,
                    'error_message': str(i.Name_of_Resource) + ' has already been added!',
                }
                return render(request, 'addresources/addresources.html', context)

        add_resources = form.save(commit=False)
        context = {
        'add_resources':add_resources,
        }
        add_resources.save()
        return render(request, 'webapp/details.html', context)
    return render(request, 'addresources/addresources.html', {'form':form})


def addmatchingresourcesCreate(request, addresources_id):
    form = addmatchingresourcesForm(request.POST or None)
    add_resources = get_object_or_404(addresources, pk=addresources_id)
    if form.is_valid():
        matches = add_resources.addmatchingresources_set.all()
        for m in matches:
            if m.Matching_HS_Code == form.cleaned_data.get("Matching_HS_Code"):
                context = {
                    'add_resources': add_resources,
                    'form': form,
                    'error_message': str(m.Name_of_Matching_Resource) + ' has already been added!',
                }
                return render(request, 'addresources/addmatchingresources_form.html', context)
        addmatches = form.save(commit=False)
        inputresource = addresources.objects.all()
        for i in inputresource:
            if i.HS_Code == form.cleaned_data.get("Matching_HS_Code"):
                addmatches.add_resources = add_resources
                context = {
                'add_resources': add_resources,
                }
                addmatches.save()
                return render(request, 'webapp/details.html', context)

        a = addresources(Name_of_Resource=form.cleaned_data.get("Name_of_Matching_Resource"), HS_Code=form.cleaned_data.get("Matching_HS_Code"))
        a.save()
        addmatches.add_resources = add_resources
        context = {
        'add_resources': add_resources,
        }
        addmatches.save()
        return render(request, 'webapp/details.html', context)
    context = {
        'form': form,
        'add_resources': add_resources,
    }
    return render(request, 'addresources/addmatchingresources_form.html', context)


def editresourcesCreate(request):
    form = editresourcesForm(request.POST or None)

    if form.is_valid():
        input_resources = addresources.objects.all()
        for i in input_resources:
            if i.HS_Code == form.cleaned_data.get("HS_Code"):
                context = {
                    'add_resources':i,
                }
                return render(request, 'webapp/details.html', context)

        context = {
            'form': form,
            'error_message': 'The resource is not found! Please try again!',
        }
        return render(request, 'addresources/editresources_form.html', context)
    return render(request, 'addresources/editresources_form.html', {'form':form})

def details(request, addresources_id):
    add_resources = get_object_or_404(addresources, pk=addresources_id)
    return render(request, 'webapp/details.html', {'add_resources':add_resources})

def visitor(request, addresources_id):
    add_resources = get_object_or_404(addresources, pk=addresources_id)
    return render(request, 'webapp/visitor.html', {'add_resources':add_resources})


def addresources_update(request, addresources_id):
    add_resources = get_object_or_404(addresources, pk=addresources_id)
    form = addresourcesForm(request.POST or None, instance = add_resources)
    if form.is_valid():
        inputresource = addresources.objects.all()
        for i in inputresource:
            if i.HS_Code == form.cleaned_data.get("HS_Code"):
                context = {
                    'form': form,
                    'error_message': str(i.Name_of_Resource) + ' has already been added!',
                }
                return render(request, 'addresources/addresources_update.html', context)

        add_resources = form.save(commit=False)
        context = {
            'add_resources': add_resources,
        }
        add_resources.save()
        return render(request, 'webapp/details.html', context)
    context = {
        'add_resources': add_resources,
        'form': form,
    }
    return render(request, 'addresources/addresources_update.html', context)


def delete_addresources(request, addresources_id):
    resource = addresources.objects.get(pk=addresources_id)
    resource.delete()
    all_resources = addresources.objects.all()
    return render(request, 'webapp/database.html', {'all_resources': all_resources})


def delete_matches(request, addresources_id, addmatchingresources_id):
    add_resources = get_object_or_404(addresources, pk=addresources_id)
    add_matchingresources = addmatchingresources.objects.get(pk=addmatchingresources_id)
    add_matchingresources.delete()
    return render(request, 'webapp/details.html', {'add_resources': add_resources})


def technologyCreate(request, addresources_id, addmatchingresources_id):
    form = TechnologiesForm(request.POST or None)
    add_resources = get_object_or_404(addresources, pk=addresources_id)
    add_matchingresources = get_object_or_404(addmatchingresources, pk=addmatchingresources_id)
    technology = add_matchingresources.technologies_set.all()
    if technology:
        context = {
            'add_resources': add_resources,
            'add_matchingresources': add_matchingresources,
            'form': form,
            'error_message': 'Technology has already been added. To update, please click the edit button under "View Technology"',
        }
        return render(request, 'addresources/technology_form.html', context)
    if form.is_valid():
        addtechnology = form.save(commit=False)
        addtechnology.add_resources = add_resources
        addtechnology.add_matchingresources = add_matchingresources
        context = {
        'add_resources': add_resources,
        'add_matchingresources': add_matchingresources,
        }
        addtechnology.save()
        return render(request, 'addresources/technology_details.html', context)
    context = {
        'add_resources': add_resources,
        'add_matchingresources': add_matchingresources,
        'form': form,

    }
    return render(request, 'addresources/technology_form.html', context)

def technologyDetails(request, addresources_id, addmatchingresources_id):
    add_resources = get_object_or_404(addresources, pk=addresources_id)
    add_matchingresources = addmatchingresources.objects.get(pk=addmatchingresources_id)
    #add_matchingresources = get_object_or_404(addmatchingresources, pk=addmatchingresources_id)

    context = {
        'add_resources': add_resources,
        'add_matchingresources': add_matchingresources,
    }
    return render(request, 'addresources/technology_details.html', context)

def technology_update(request, addresources_id, addmatchingresources_id, technologies_id):
    add_resources = get_object_or_404(addresources, pk=addresources_id)
    add_matchingresources = addmatchingresources.objects.get(pk=addmatchingresources_id)
    #technology = add_matchingresources.technologies_set.all()
    technology = Technologies.objects.get(pk=technologies_id)
    form = TechnologiesForm(request.POST or None, instance = technology)
    if form.is_valid():
        addtechnology = form.save(commit=False)
        addtechnology.add_resources = add_resources
        addtechnology.add_matchingresources = add_matchingresources
        context = {
        'add_resources': add_resources,
        'add_matchingresources': add_matchingresources,
        }
        addtechnology.save()
        return render(request, 'addresources/technology_details.html', context)
    context = {
        'add_resources': add_resources,
        'add_matchingresources': add_matchingresources,
        'form': form,
    }
    return render(request, 'addresources/technology_form.html', context)

def dfs(request):
    query = request.GET.get("q")
    graph = generate_adjacency_map()
    final_path = []
    path = traverse(graph, query, final_path)
    print(path)
    context = {
        'query': query,
        'path': path,
    }
    return render(request, 'addresources/dfs.html', context)


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'webapp/home.html')
    context = {
        "form": form,
    }
    return render(request, 'addresources/register.html', context)


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'addresources/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'webapp/home.html')
            else:
                return render(request, 'addresources/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'addresources/login.html', {'error_message': 'Invalid login'})
    return render(request, 'addresources/login.html')

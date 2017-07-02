from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from .models import addresources, addmatchingresources, editresources, Technologies
from .models import generate_adjacency_map, traverse
from .forms import addresourcesForm, addmatchingresourcesForm, editresourcesForm, TechnologiesForm, UserForm
from django.db.models import Q

from django.http import HttpResponseBadRequest, HttpResponse,JsonResponse

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

class UploadFileForm(forms.Form):
    file = forms.FileField()

def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            return excel.make_response(filehandle.get_sheet(), "csv",
                                    file_name="download")

        else:
            form = UploadFileForm()
            return render(
                request,
                'upload_form.html',
                {
                'form': form,
                'title': 'Excel file upload and download example',
                'header': ('Please choose any excel file ' +
                'from your cloned repository:')
                })

def download(request, file_type):
    sheet = excel.pe.Sheet(data)
    return excel.make_response(sheet, file_type)


def download_as_attachment(request, file_type, file_name):
    return excel.make_response_from_array(
        data, file_type, file_name=file_name)

def export_data(request, atype):
    if atype == "sheet":
        return excel.make_response_from_a_table(
            Question, 'xls', file_name="sheet")
    elif atype == "book":
        return excel.make_response_from_tables(
            [Question, Choice], 'xls', file_name="book")
    elif atype == "custom":
        question = Question.objects.get(slug='ide')
        query_sets = Choice.objects.filter(question=question)
        column_names = ['choice_text', 'id', 'votes']
        return excel.make_response_from_query_sets(
            query_sets,
            column_names,
            'xls',
            file_name="custom"
        )
    else:
        return HttpResponseBadRequest(
            "Bad request. please put one of these " +
            "in your url suffix: sheet, book or custom")


def import_data(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)

        def choice_func(row):
            q = Question.objects.filter(slug=row[0])[0]
            row[0] = q
            return row
        if form.is_valid():
            request.FILES['file'].save_book_to_database(
                models=[Question, Choice],
                initializers=[None, choice_func],
                mapdicts=[
                    ['question_text', 'pub_date', 'slug'],
                    ['question', 'choice_text', 'votes']]
            )
            return HttpResponse("OK", status=200)
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {
            'form': form,
            'title': 'Import excel data into database example',
            'header': 'Please upload sample-data.xls:'
        })


def import_sheet(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)
        if form.is_valid():
            request.FILES['file'].save_to_database(
                name_columns_by_row=2,
                model=Question,
                mapdict=['question_text', 'pub_date', 'slug'])
            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {'form': form})


def exchange(request, file_type):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        filehandle = request.FILES['file']
        return excel.make_response(filehandle.get_sheet(), file_type)
    else:
        return HttpResponseBadRequest()


def parse(request, data_struct_type):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        filehandle = request.FILES['file']
        if data_struct_type == "array":
            return JsonResponse({"result": filehandle.get_array()})
        elif data_struct_type == "dict":
            return JsonResponse(filehandle.get_dict())
        elif data_struct_type == "records":
            return JsonResponse({"result": filehandle.get_records()})
        elif data_struct_type == "book":
            return JsonResponse(filehandle.get_book().to_dict())
        elif data_struct_type == "book_dict":
            return JsonResponse(filehandle.get_book_dict())
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()

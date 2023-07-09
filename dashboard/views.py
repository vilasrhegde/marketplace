from django.shortcuts import render,get_object_or_404,redirect

from item.models import Item, Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CategoryForm


@login_required
def index(request):
    items = Item.objects.filter(created_by = request.user)
    all_users = User.objects.all()
    categories = Category.objects.all()


    return render(request, 'dashboard/index.html',{
        'items':items,
        'all_users':all_users,
        'categories':categories,

    })

    
@login_required
def deleteUsers(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = get_object_or_404(User, id=user_id)
        user.delete()
    return redirect('dashboard:index')



@login_required
def promoteUser(request,pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return redirect('dashboard:index')  # Redirect to the desired page if user doesn't exist

    user.is_staff = not user.is_staff
    user.is_superuser = not user.is_superuser
    user.save()
    return redirect('dashboard:index')

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:index')
    else:
        form = CategoryForm()

    categories = Category.objects.all()
    return render(request, 'dashboard/add_category.html', {
        'form': form,
        'categories':categories,
        })
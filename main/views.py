from django.shortcuts import render

posts = [
    {'author':'Mohammad',
     'title': 'Title of Post 01',
     'content':'This is the content of post 01',
     'post_date':'January 27, 2021',
     'avatar':'#e83e8c'},
     {'author':'Ali',
     'title': 'Title of Post 02',
     'content':'This is the content of post 02',
     'post_date':'January 25, 2021',
     'avatar':'#6f42c1'},
]
def home(request):
    context = {'posts':posts}
    return render(request, 'index.html', context=context)

def about(request):
    return render(request, 'about.html', {'title':'About'})
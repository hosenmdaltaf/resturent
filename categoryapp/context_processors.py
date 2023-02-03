from categoryapp.models import Category

def get_category_to_context(request):
    categorys = Category.objects.all()
    return {
        'categorys': categorys
    }


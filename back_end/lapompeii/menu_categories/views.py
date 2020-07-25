from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from menu_categories.managers import MenuCategoriesManager

@api_view(['GET', 'POST'])
def categories(request):
    """
    Either returns a list of categories or creates new category for a specified Project.

    """
    if request.method == 'GET':
        return Response(MenuCategoriesManager.ReturnMenuCategories(), status=status.HTTP_200_OK)

    elif request.method == 'POST':
        success, result = MenuCategoriesManager.Create(request.data)
        if success:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','DELETE'])
def category(request, id):
    """
    Performs operations on a single category including viewing,
    editing and deleting.

    """
    if request.method == 'GET':
        found, result = MenuCategoriesManager.Find(id, serialize=True)
        if found:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        success, result = MenuCategoriesManager.Update(id, request.data)
        if result is None:
            print('Here?')
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        if success:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if MenuCategoriesManager.Delete(id):
            return Response(None, status=status.HTTP_200_OK)
        else:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
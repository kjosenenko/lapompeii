# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from menu_items.managers import MenuItemsManager

@api_view(['GET', 'POST'])
def items(request):
    """
    Either returns a list of items or creates new item for a specified Project.

    """
    if request.method == 'GET':
        return Response(MenuItemsManager.ReturnMenuItems(), status=status.HTTP_200_OK)

    elif request.method == 'POST':
        success, result = MenuItemsManager.Create(request.data)
        if success:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','DELETE'])
def item(request, id):
    """
    Performs operations on a single item including viewing,
    editing and deleting.

    """
    if request.method == 'GET':
        found, result = MenuItemsManager.Find(id, serialize=True)
        if found:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        print('I think I am posting something...')
        success, result = MenuItemsManager.Update(id, request.data)
        if result is None:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        if success:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if MenuItemsManager.Delete(id):
            return Response(None, status=status.HTTP_200_OK)
        else:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def itemsByCategory(request, menucategories_id):
    """
    Returns a list of items associated with a specified Category.

    """
    if request.method == 'GET':
        return Response(MenuItemsManager.ReturnMenuItemsByCategory(menucategories_id, True), status=status.HTTP_200_OK)

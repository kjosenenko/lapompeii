from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from menu_tags.managers import MenuTagsManager

@api_view(['GET', 'POST'])
def tags(request):
    """
    Either returns a list of categories or creates new category for a specified Project.

    """
    if request.method == 'GET':
        return Response(MenuTagsManager.ReturnMenuTags(), status=status.HTTP_200_OK)

    elif request.method == 'POST':
        success, result = MenuTags.Create(request.data)
        if success:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','DELETE'])
def tag(request, id):
    """
    Performs operations on a single category including viewing,
    editing and deleting.

    """
    if request.method == 'GET':
        found, result = MenuTagsManager.Find(id, serialize=True)
        if found:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        success, result = MenuTagsManager.Update(id, request.data)
        if result is None:
            print('Here?')
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        if success:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if MenuTagsManager.Delete(id):
            return Response(None, status=status.HTTP_200_OK)
        else:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
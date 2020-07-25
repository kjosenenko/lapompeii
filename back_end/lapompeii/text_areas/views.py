from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from text_areas.managers import TextAreasManager

@api_view(['GET', 'POST'])
def text_areas(request):
    """
    Either returns a list of text areas or creates new text area for a specified Project.

    """
    if request.method == 'GET':
        return Response(TextAreasManager.ReturnTextAreas(), status=status.HTTP_200_OK)

    elif request.method == 'POST':
        success, result = TextAreasManager.Create(request.data)
        if success:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','DELETE'])
def text_area(request, id):
    """
    Performs operations on a single text area including viewing,
    editing and deleting.

    """
    if request.method == 'GET':
        found, result = TextAreasManager.Find(id, serialize=True)
        if found:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        success, result = TextAreasManager.Update(id, request.data)
        if result is None:
            print('Here?')
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        if success:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if TextAreasManager.Delete(id):
            return Response(None, status=status.HTTP_200_OK)
        else:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

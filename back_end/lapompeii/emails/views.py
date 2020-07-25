from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from emails.managers import EmailsManager

@api_view(['GET', 'POST'])
def emails(request):
    """
    Either returns a list of emails or creates new email for a specified Project.

    """
    if request.method == 'GET':
        return Response(EmailsManager.ReturnEmails(), status=status.HTTP_200_OK)

    elif request.method == 'POST':
        success, result = EmailsManager.Create(request.data)
        if success:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','DELETE'])
def email(request, id):
    """
    Performs operations on a single email including viewing,
    editing and deleting.

    """
    if request.method == 'GET':
        found, result = EmailsManager.Find(id, serialize=True)
        if found:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        success, result = EmailsManager.Update(id, request.data)
        if result is None:
            print('Here?')
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        if success:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if EmailsManager.Delete(id):
            return Response(None, status=status.HTTP_200_OK)
        else:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
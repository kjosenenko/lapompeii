from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from schedule.managers import ScheduleManager


@api_view(['GET', 'POST'])
def schedule(request):
    """
    Either returns a list of events or creates new slot for a specified Project.

    """
    if request.method == 'GET':
        return Response(ScheduleManager.ReturnSchedule(), status=status.HTTP_200_OK)

    elif request.method == 'POST':
        success, result = ScheduleManager.Create(request.data)
        if success:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','DELETE'])
def event(request, id):
    """
    Performs operations on a single event including viewing,
    editing and deleting.

    """
    if request.method == 'GET':
        found, result = ScheduleManager.Find(id, serialize=True)
        if found:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        success, result = ScheduleManager.Update(id, request.data)
        if result is None:
            print('Here?')
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        if success:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if ScheduleManager.Delete(id):
            return Response(None, status=status.HTTP_200_OK)
        else:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
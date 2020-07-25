from django.db import models
from django.db import transaction

from schedule.models import Schedule
from schedule.serializers import ScheduleSerializer
from datetime import datetime, timedelta

import re

class ScheduleManager(models.Manager):

    @staticmethod
    def ReturnSchedule(serialize=True):
        """
        Retrieves "schedule" of upcoming events.

        """
        list = Schedule.objects.all().order_by('start_date') 
        if serialize:
            serializer = ScheduleSerializer(list, many=True)
            allEvents = serializer.data
            currentEvents = []
            yesterday = datetime.now() + timedelta(days=-1)
            for event in allEvents:
                add = False
                if event['end_date'] > yesterday.strftime("%Y-%m-%d"):
                    add = True
                if add:
                    currentEvents.append(event)
            return currentEvents
        else:
            return list

    @staticmethod
    def Create(createData):
        """
        Creates an event with specified data.

        """
        if 'label' in createData:
            createData['label'] = re.sub('<[^<]+?>', '', createData['label'])
                
        serializer = ScheduleSerializer(None, data=createData)
        if serializer.is_valid():
            created = ScheduleSerializer(serializer.save())
            return (True, created.data,)
        else:
            return (False, serializer.errors,)

    @staticmethod
    def Find(id, serialize=True):
        """
        Retrieves an event by its ID. 

        """
        try:
            a = Schedule.objects.get(id=id)
        except:
            return (False, None,)

        if serialize:
            serializer = ScheduleSerializer(a)
            event = serializer.data
            return (True, event,)
        else:
            return (True, a,)

    @staticmethod
    def Delete(id):
        """
        Deletes an event specified by its ID.

        """
        try:
            a = Schedule.objects.get(id=id)
        except:
            return False
        if a.delete():
            return True
        else:
            return False

    @staticmethod
    def Update(id, updateData):
        """
        Updates an event with specified data.

        """
        print(updateData)
        if 'label' in updateData:
            updateData['label'] = re.sub('<[^<]+?>', '', updateData['label'])        
        a = None
        try:
            a = Schedule.objects.get(id=id)
        except Exception as e: print(e)
            
        serializer = ScheduleSerializer(a, data=updateData)
        if serializer.is_valid():
            updated = ScheduleSerializer(serializer.save())
            return (True, updated.data,)
        else:
            return (False, serializer.errors,)
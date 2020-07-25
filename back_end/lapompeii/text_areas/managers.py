from django.db import models
from django.db import transaction

from text_areas.models import TextAreas
from text_areas.serializers import TextAreasSerializer
from datetime import datetime, timedelta

import re

class TextAreasManager(models.Manager):

    @staticmethod
    def ReturnTextAreas(serialize=True):
        """
        Retrieves all text areas in DB.

        """
        list = TextAreas.objects.all()
        if serialize:
            serializer = TextAreasSerializer(list, many=True)
            return serializer.data
        else:
            return list

    @staticmethod
    def Create(createData):
        """
        Creates a text area with specified data.

        """
        if 'label' in createData:
            createData['label'] = re.sub('<[^<]+?>', '', createData['label'])
                
        serializer = TextAreasSerializer(None, data=createData)
        if serializer.is_valid():
            created = TextAreasSerializer(serializer.save())
            return (True, created.data,)
        else:
            return (False, serializer.errors,)

    @staticmethod
    def Find(id, serialize=True):
        """
        Retrieves a text area by its ID. 

        """
        try:
            a = TextAreas.objects.get(id=id)
        except:
            return (False, None,)

        if serialize:
            serializer = TextAreasSerializer(a)
            event = serializer.data
            return (True, textArea,)
        else:
            return (True, a,)

    @staticmethod
    def Delete(id):
        """
        Deletes a text area specified by its ID.

        """
        try:
            a = TextAreas.objects.get(id=id)
        except:
            return False
        if a.delete():
            return True
        else:
            return False

    @staticmethod
    def Update(id, updateData):
        """
        Updates a text area with specified data.

        """
        print(updateData)
        if 'label' in updateData:
            updateData['label'] = re.sub('<[^<]+?>', '', updateData['label'])        
        a = None
        try:
            a = TextAreas.objects.get(id=id)
        except Exception as e: print(e)
            
        serializer = TextAreasSerializer(a, data=updateData)
        if serializer.is_valid():
            updated = TextAreasSerializer(serializer.save())
            return (True, updated.data,)
        else:
            return (False, serializer.errors,)    
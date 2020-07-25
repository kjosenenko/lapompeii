from django.db import models
from django.db import transaction

from menu_tags.models import MenuTags
from menu_tags.serializers import MenuTagsSerializer
from datetime import datetime, timedelta

import re

class MenuTagsManager(models.Manager):

    @staticmethod
    def ReturnMenuTags(serialize=True):
        """
        Retrieves all menu tags in DB.

        """
        list = MenuTags.objects.all()
        if serialize:
            serializer = MenuTagsSerializer(list, many=True)
            return serializer.data
        else:
            return list

    @staticmethod
    def Create(createData):
        """
        Creates a menu tag with specified data.

        """
        if 'label' in createData:
            createData['label'] = re.sub('<[^<]+?>', '', createData['label'])
                
        serializer = MenuTagsSerializer(None, data=createData)
        if serializer.is_valid():
            created = MenuTagsSerializer(serializer.save())
            return (True, created.data,)
        else:
            return (False, serializer.errors,)

    @staticmethod
    def Find(id, serialize=True):
        """
        Retrieves a menu tag by its ID. 

        """
        try:
            a = MenuTags.objects.get(id=id)
        except:
            return (False, None,)

        if serialize:
            serializer = MenuTagsSerializer(a)
            tag = serializer.data
            return (True, tag,)
        else:
            return (True, a,)

    @staticmethod
    def Delete(id):
        """
        Deletes a menu tag specified by its ID.

        """
        try:
            a = MenuTags.objects.get(id=id)
        except:
            return False
        if a.delete():
            return True
        else:
            return False

    @staticmethod
    def Update(id, updateData):
        """
        Updates a menu tag with specified data.

        """
        print(updateData)
        if 'label' in updateData:
            updateData['label'] = re.sub('<[^<]+?>', '', updateData['label'])        
        a = None
        try:
            a = MenuTags.objects.get(id=id)
        except Exception as e: print(e)
            
        serializer = MenuTagsSerializer(a, data=updateData)
        if serializer.is_valid():
            updated = MenuTagsSerializer(serializer.save())
            return (True, updated.data,)
        else:
            return (False, serializer.errors,)    
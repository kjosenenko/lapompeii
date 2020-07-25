from django.db import models
from django.db import transaction

from menu_categories.models import MenuCategories
from menu_categories.serializers import MenuCategoriesSerializer
from datetime import datetime, timedelta

import re

class MenuCategoriesManager(models.Manager):

    @staticmethod
    def ReturnMenuCategories(serialize=True):
        """
        Retrieves all menu categories in DB.

        """
        list = MenuCategories.objects.all()
        if serialize:
            serializer = MenuCategoriesSerializer(list, many=True)
            return serializer.data
        else:
            return list

    @staticmethod
    def Create(createData):
        """
        Creates a menu category with specified data.

        """
        if 'label' in createData:
            createData['label'] = re.sub('<[^<]+?>', '', createData['label'])
                
        serializer = MenuCategoriesSerializer(None, data=createData)
        if serializer.is_valid():
            created = MenuCategoriesSerializer(serializer.save())
            return (True, created.data,)
        else:
            return (False, serializer.errors,)

    @staticmethod
    def Find(id, serialize=True):
        """
        Retrieves a menu category by its ID. 

        """
        try:
            a = MenuCategories.objects.get(id=id)
        except:
            return (False, None,)

        if serialize:
            serializer = MenuCategoriesSerializer(a)
            category = serializer.data
            return (True, category,)
        else:
            return (True, a,)

    @staticmethod
    def Delete(id):
        """
        Deletes a menu category specified by its ID.

        """
        try:
            a = MenuCategories.objects.get(id=id)
        except:
            return False
        if a.delete():
            return True
        else:
            return False

    @staticmethod
    def Update(id, updateData):
        """
        Updates a menu category with specified data.

        """
        print(updateData)
        if 'label' in updateData:
            updateData['label'] = re.sub('<[^<]+?>', '', updateData['label'])        
        a = None
        try:
            a = MenuCategories.objects.get(id=id)
        except Exception as e: print(e)
            
        serializer = MenuCategoriesSerializer(a, data=updateData)
        if serializer.is_valid():
            updated = MenuCategoriesSerializer(serializer.save())
            return (True, updated.data,)
        else:
            return (False, serializer.errors,)    
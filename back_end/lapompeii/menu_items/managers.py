from django.db import models
from django.db import transaction

from menu_items.models import MenuItems
from menu_items.serializers import MenuItemsSerializer
from menu_tags.models import MenuTags
from menu_tags.serializers import MenuTagsSerializer
from datetime import datetime, timedelta

import re

# Create your models here.

class MenuItemsManager(models.Manager):

    @staticmethod
    def ReturnMenuItems(serialize=True):
        """
        Retrieves menu items.

        """
        list = MenuItems.objects.all()
        if serialize:
            serializer = MenuItemsSerializer(list, many=True)
            return serializer.data
        else:
            return list

    @staticmethod
    def ReturnMenuItemsByCategory(menucategories_id, serialize=True):
        """
        Retrieves menu items associated with a Menu Category.

        """
        list = MenuItems.objects.filter(category = menucategories_id)
        if serialize:
            serializer = MenuItemsSerializer(list, many=True)
            return serializer.data
        else:
            return list

    @staticmethod
    def Find(id, serialize=True):
        """
        Retrieves an item by its ID. 

        """
        try:
            a = MenuItems.objects.get(id=id)
        except:
            return (False, None,)

        if serialize:
            serializer = MenuItemsSerializer(a)
            item = serializer.data
            return (True, item,)
        else:
            return (True, a,)
        
    @staticmethod
    def Create(createData):
        """
        Creates an item with specified data.

        """
        if 'label' in createData:
            createData['label'] = re.sub('<[^<]+?>', '', createData['label'])
                
        serializer = MenuItemsSerializer(None, data=createData)
        if serializer.is_valid():
            created = MenuItemsSerializer(serializer.save())
            return (True, created.data,)
        else:
            return (False, serializer.errors,)
        
    @staticmethod
    def Delete(id):
        """
        Deletes an item specified by its ID.

        """
        try:
            a = MenuItems.objects.get(id=id)
        except:
            return False
        if a.delete():
            return True
        else:
            return False
        
    @staticmethod
    def Update(id, updateData):
        """
        Updates an item with specified data.

        """
        print(updateData)
        if 'label' in updateData:
            updateData['label'] = re.sub('<[^<]+?>', '', updateData['label'])        
        a = None
        try:
            a = MenuItems.objects.get(id=id)
        except Exception as e: print(e)
            
        serializer = MenuItemsSerializer(a, data=updateData)
        if serializer.is_valid():
            updated = MenuItemsSerializer(serializer.save())
            return (True, updated.data,)
        else:
            return (False, serializer.errors,)


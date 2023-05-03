from djongo import models
from django import forms

class Credential(models.Model):
    _id = models.ObjectIdField()
    email_id = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    fridgeList = models.JSONField(default = dict)
    noFridges = models.IntegerField(default = 0)

    def __str__(self):
        return self.email_id
    
    def addFridge(self, email):
        if Credential.objects.get(email_id = email):
            if email not in self.fridgeList.keys():
                self.fridgeList[email] = self.noFridges  
                self.noFridges += 1
                self.save()
                return True
            else:
                return False
        else:
            return False
       

    def removeFridge(self, email):
        if email in self.fridgeList.keys():
             self.fridgeList.pop(email)
             self.noFridges -=1
             self.save()
             return True
        else:
            return False



class Shelf(models.Model):
    primary_user = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    height = models.FloatField()
    width = models.FloatField()
    depth = models.FloatField()
    items_list = models.JSONField(default=dict)
    volumeFilled = models.FloatField(default=0)
    availableVolume = models.FloatField()

    def getVolumeFilled(self):
        return self.volumeFilled
    
    def addItem(self, name, itemHeight, itemWidth, itemDepth, quantity):
        itemVolume = int(itemHeight) * int(itemWidth) * int(itemDepth)
        requiredVolume = itemVolume * quantity
        if self.availableVolume >= requiredVolume:
            item = {'name': name, 'height': itemHeight, 'width': itemWidth, 'depth': itemDepth, 'quantity': quantity}
            self.items_list.append(item)
            self.volumeFilled += requiredVolume
            self.availableVolume -= requiredVolume
            self.save()
            return True
        else:
            return False
    
    def remove_item(self, name, quantity):
        for item in self.items_list:
            if item['name'] == name:
                if item['quantity'] <= quantity:
                    self.volumeFilled -= int(item['quantity']) * int(item['height']) * int(item['width']) * int(item['depth'])
                    self.availableVolume += int(item['quantity']) * int(item['height']) * int(item['width']) * int(item['depth'])
                    self.items_list.remove(item)
                    self.save()
                    return True
                else:
                    item['quantity'] -= quantity
                    self.volumeFilled -= quantity * int(item['height']) * int(item['width']) * int(item['depth'])
                    self.availableVolume += quantity * int(item['height']) * int(item['width']) * int(item['depth'])
                    self.save()
                    return True
        return False

class Refrigerator(models.Model):
    primary_user = models.EmailField(max_length=254)
    ref_height = models.IntegerField(default=0)
    ref_width = models.IntegerField(default=0)
    ref_depth = models.IntegerField(default=0)
    fridge_height = models.IntegerField(default=0)
    numberFridgeShelves = models.IntegerField(default=0)
    freezer_height = models.IntegerField(default=0)
    numberFreezerShelves = models.IntegerField(default=0)
    fridgevolume = models.FloatField(default=0)
    freezervolume = models.FloatField(default=0)
    availablefridgevolume = models.FloatField(default=0)
    availablefreezervolume = models.FloatField(default=0)
    userList = models.JSONField(default = dict)
    noUsers = models.IntegerField(default = 0)

    def addUser(self, email):
        if Credential.objects.all().filter(email_id = email):
            if email not in self.userList.keys():
                self.userList[email] = self.noUsers
                self.noUsers += 1 
                self.save()
                return True
            else:
                return False
        else:
            return False
        
    def removeUser(self, email):
        if email in self.userList.keys():
            self.userList.pop(email)
            self.noUsers -= 1
            self.save()
            return True
        else:
            return False

class Item(models.Model):
    name = models.CharField(max_length=255)
    height = models.FloatField()
    width = models.FloatField()
    depth = models.FloatField()
    expiration = models.DateField()
    email = models.EmailField(max_length=254)

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

    def getDepth(self):
        return self.depth

    def getName(self):
        return self.name

    def getExpiration(self):
        return self.expiration
    
    def resize(self):
        self.height = models.FloatField()
        self.width = models.FloatField()
        self.depth = models.FloatField()
    

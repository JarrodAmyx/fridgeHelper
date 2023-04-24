from djongo import models

class Credential(models.Model):
    _id = models.ObjectIdField()
    email_id = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    
    def __str__(self):
        return self.email_id


class Shelf(models.Model):
    name = models.CharField(max_length=50)
    height = models.FloatField()
    width = models.FloatField()
    depth = models.FloatField()
    items_list = models.JSONField(default=list)
    volumeFilled = models.FloatField(default=0)
    availableVolume = models.FloatField()

    def getVolumeFilled(self):
        return self.volumeFilled
    
    def addItem(self, name, itemHeight, itemWidth, itemDepth, quantity):
        itemVolume = itemHeight * itemWidth * itemDepth
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
                    self.volumeFilled -= item['quantity'] * item['height'] * item['width'] * item['depth']
                    self.availableVolume += item['quantity'] * item['height'] * item['width'] * item['depth']
                    self.items_list.remove(item)
                    self.save()
                    return True
                else:
                    item['quantity'] -= quantity
                    self.volumeFilled -= quantity * item['height'] * item['width'] * item['depth']
                    self.availableVolume += quantity * item['height'] * item['width'] * item['depth']
                    self.save()
                    return True
        return False

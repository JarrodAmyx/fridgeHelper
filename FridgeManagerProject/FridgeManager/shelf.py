class Shelf:
    def __init__(self, name, height, width, depth):
        self.name = name
        self.height = height
        self.width = width
        self.depth = depth
        self.items_list = []
        self.volumeFilled = 0
        self.availableVolume = height * width * depth
    
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
                    return True
                else:
                    item['quantity'] -= quantity
                    self.volumeFilled -= quantity * item['height'] * item['width'] * item['depth']
                    self.availableVolume += quantity * item['height'] * item['width'] * item['depth']
                    return True
        return False

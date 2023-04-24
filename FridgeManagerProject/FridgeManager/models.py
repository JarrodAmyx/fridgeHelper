from djongo import models

class Credential(models.Model):
    _id = models.ObjectIdField()
    email_id = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    
    def __str__(self):
        return self.email_id

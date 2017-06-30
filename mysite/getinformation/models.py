from django.db import models

class getinformation(models.Model):
    Search_by_HS_Code = models.IntegerField()
    Search_by_Name = models.CharField(max_length = 500)

    #def get_absolute_url(self):
        #return reverse('webapp:index', kwargs={'pk':self.pk})

    def __str__(self):
        return self.Search_by_Name + ' - ' + self.Search_by_HS_Code
    

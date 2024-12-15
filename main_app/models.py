from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class contactClass(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    message=models.TextField(max_length=500)    
    def __str__(self) -> str:
        return self.username
    
    
class staticContentClass(models.Model):
    key=models.CharField(max_length=10)
    text=RichTextField()
    title=models.CharField(max_length=100,null=True)
    def __str__(self) -> str:
        return self.title
    
    
class staticPhotoClass(models.Model):
    key=models.CharField(max_length=10)    
    photo=models.ImageField(upload_to="images/staticPhoto")
    title=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.title
    
    
class productClass(models.Model):
    name=models.CharField(max_length=100)
    description=RichTextField(null=True)
    def __str__(self) -> str:
        return self.name


class productImagesClass(models.Model):
    name=models.CharField(max_length=100)
    photo1=models.ImageField(upload_to="images/products")
    photo2=models.ImageField(upload_to="images/products")
    photo3=models.ImageField(upload_to="images/products")
    photo4=models.ImageField(upload_to="images/products")
    photo5=models.ImageField(upload_to="images/products",blank=True)
    photo6=models.ImageField(upload_to="images/products",blank=True)
    photo7=models.ImageField(upload_to="images/products",blank=True)
    photo8=models.ImageField(upload_to="images/products",blank=True)
    photoZ1=models.ImageField(upload_to="images/products/zoom",blank=True)
    photoZ2=models.ImageField(upload_to="images/products/zoom",blank=True)
    photoZ3=models.ImageField(upload_to="images/products/zoom",blank=True)
    photoZ4=models.ImageField(upload_to="images/products/zoom",blank=True)
    photoZ5=models.ImageField(upload_to="images/products/zoom",blank=True)
    photoZ6=models.ImageField(upload_to="images/products/zoom",blank=True)
    photoZ7=models.ImageField(upload_to="images/products/zoom",blank=True)
    photoZ8=models.ImageField(upload_to="images/products/zoom",blank=True)
    def __str__(self) -> str:
        return self.name
    
class categoryClass(models.Model):
    name=models.CharField(max_length=50)
    photo=models.ImageField(upload_to="images")
    text=RichTextField(null=True,blank=True)
    def __str__(self) -> str:
        return self.name       
    
    
class brandClass(models.Model):
    name=models.CharField(max_length=50) 
    def __str__(self) -> str:
        return self.name     
 
 
class colorClass(models.Model):
    name=models.CharField(max_length=50)
    hex_code=models.CharField(max_length=7,blank=True,null=True)
    photo=models.ImageField(upload_to="images",null=True)
    def __str__(self) -> str:
        return self.name
    

class sizeClass(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name


class productVariantClass(models.Model):
    product=models.ForeignKey(productClass,on_delete=models.CASCADE,related_name="products")
    photo=models.ImageField(upload_to="images",null=True)
    image=models.ForeignKey(productImagesClass,on_delete=models.CASCADE,related_name="images",null=True)
    category=models.ForeignKey(categoryClass,on_delete=models.CASCADE,related_name="categories",null=True)
    brand=models.ForeignKey(brandClass,on_delete=models.CASCADE,related_name="brands",null=True)
    color=models.ForeignKey(colorClass,on_delete=models.CASCADE,related_name="colors")
    size=models.ForeignKey(sizeClass,on_delete=models.CASCADE,related_name="sizes")
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField(default=0)
    def __str__(self) -> str:
        return f"{self.product.name}-{self.color.name}-{self.size.name}-{self.price}USD"        

     
    
    
class cityClass(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name
    
    
class agencyClass(models.Model):
    title=models.CharField(max_length=50)
    city=models.ForeignKey(cityClass,null=True,on_delete=models.CASCADE,related_name="ac")
    description=models.TextField(null=True,blank=True)
    address=models.TextField()
    phone=models.CharField(max_length=11,blank=True)  
    telephone=models.CharField(max_length=11,null=True,blank=True)  
    email=models.EmailField(max_length=50,blank=True)
    photo=models.ImageField(upload_to="images",blank=True)  
    def __str__(self) -> str:
        return self.title


class questionClass(models.Model):
    title=models.CharField(max_length=200)
    description=RichTextField()
    def __str__(self) -> str:
        return self.title


class questionBClass(models.Model):
    title=models.CharField(max_length=200)
    description=RichTextField()
    def __str__(self) -> str:
        return self.title
    
    
class questionCClass(models.Model):
    title=models.CharField(max_length=200)
    description=RichTextField()
    def __str__(self) -> str:
        return self.title
    
    
class questionDClass(models.Model):
    title=models.CharField(max_length=200)
    description=RichTextField()
    def __str__(self) -> str:
        return self.title    
            
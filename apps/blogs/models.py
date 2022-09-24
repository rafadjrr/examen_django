from django.db import models

# Create your models here.

class Author(models.Model):
    
    JOB_CHOICES =(
        ('0','ingeniero informatico'),
        ('1','ingeniero sistemas'),
        ('2','electronico'),
        ('3','administrador'),
        ('4','contador'),
        ('5','asistente'),
    )
    first_name = models.CharField('first name', max_length=60)
    last_name = models.CharField('last name', max_length=60)
    nick = models.CharField('nick', max_length=30, blank=True)
    birth = models.DateField('birth')
    avatar = models.ImageField('avatar', upload_to='img_author', height_field=None, width_field=None, max_length=None,null=True,blank=True)
    descripcion = models.CharField('description', max_length=120)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'blog authors'
        ordering = ['-id']
    def __str__(self):
        return self.first_name + " " + self.last_name 


class Blog(models.Model):
    
    JOB_CHOICES =(
        ('0','Enterprise'),
        ('1','Education'),
        ('2','Security'),
        ('3','Community'),
        ('4','Programing'),
    )
    author =  models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField('title', max_length=60)
    subtitle = models.CharField('subtitle', max_length=100)
    content = models.TextField('content', max_length=30, blank=True)
    publication_date = models.DateTimeField('publication date',auto_now_add=True,editable=False)
    image = models.ImageField('image', upload_to='img_blog', height_field=None, width_field=None, max_length=None,null=True,blank=True)
    category = models.CharField('category', max_length=1,choices=JOB_CHOICES)

    class Meta:
        
        verbose_name = 'Blog'
        verbose_name_plural = 'published Blog'
        ordering = ['-id']
    def __str__(self):
        
        return self.title + " - " + self.author

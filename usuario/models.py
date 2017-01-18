from django.db import models
import hashlib
# Create your models here.


class usuario (models.Model):
	STUDENT = 's'
	TEACHER = 't'
	GENDER_CHOICES = (
	(STUDENT,' student'),
	(TEACHER, 'teacher'))
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=64)
	email =  models.EmailField()
	first_name = models.CharField(max_length=30)
	last_name =models.CharField(max_length=30)
	dni =models.CharField(max_length=8)
	gender = models.CharField(choices=GENDER_CHOICES,default=STUDENT, max_length=128)
	'''
	tipo =models.CharField(max_length=16)
	''' 
	
	def crear(user,password):
		s = usuario()
		s.username = user
		s.password = hashlib.sha256(str(password).encode()).hexdigest()
		s.save()
		return s

	def verificar(user , password):
		try:
			ver =  usuario.objects.get(username=user)   
		except usuario.DoesNotExist:

			return False

		c=hashlib.sha256(str(password).encode()).hexdigest()
		if ver.password==c:            
			return True
		else:
			return False

	def verificacionEmail(email):
		try:
			veri = usuario.objects.get(email=email)

		except 	 usuario.DoesNotExist:
			return False   
	


'''
class UserProfile(models.Model):
	user = models.OneToOneField(usuario)
	activation_key = models.CharField(max_length=40,blank=True)
	key_expires = models.DateTimeField(default=datetime.date.today())

'''
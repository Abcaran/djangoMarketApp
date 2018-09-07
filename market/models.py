from django.db import models

class Product(models.Model):
	name = models.CharField (max_length=50)

	def __str__(self):
		return self.name

class Purchase(models.Model):
	product = models.ForeignKey (Product, on_delete=models.CASCADE)
	amount = models.PositiveIntegerField()
	total_price = models.DecimalField(max_digits=10, decimal_places=2)
	avrg_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

	def __str__(self):
		message = 'O produto comprado foi '+self.product.name+', com '+str(self.amount)+' unidade(s), tendo o valor total de '+str(self.total_price)+'.'
		return message





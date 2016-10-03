from django.db import models
from django.conf import settings

# Create your models here.



#não colocar logica na view e sim criar os metodos do modelo como manager
class CartItemManager(models.Manager):

	def add_item(self,cart_key,product):
		if self.filter(cart_key=cart_key, product=product).exists():
			created = False
			cart_item = self.get(cart_key=cart_key, product=product)
			cart_item.quantity = cart_item.quantity + 1
			cart_item.save()
		else:
		    created = True
		    cart_item = CartItem.objects.create(
		        cart_key=cart_key, product=product, price=product.price
		    )
		return cart_item, created

class CartItem(models.Model):
	#identificador do carrinho de compras
	cart_key = models.CharField('Chave do Carrinho',max_length=40,db_index=True)
	product = models.ForeignKey('catalog.Product',verbose_name='Produto')
	quantity = models.PositiveIntegerField('Quantidade',default=1)
	price = models.DecimalField('Preço',decimal_places=2,max_digits=8)

	#sobrescrita do manager
	objects = CartItemManager()

	class Meta:
		verbose_name = 'Item do Carrinho'
		verbose_name_plural = 'Itens do Carrinho'
		#no carrinho não sera possivel ter dois produtos no mesmo carrinho usar unique_together para criar os indices
		unique_together = (('cart_key','product'),)

	def __str__(self):
		return '{} [{}]'.format(self.product,self.quantity)


class OrderManager(models.Manager):

	def create_order(self,user,cart_itens):
		#cria o pedido
		order = self.create(user = user)
		for cart_item in cart_itens:
			order_item = OrderItem.objects.create(order = order,product=cart_item.product,quantity=cart_item.quantity,price=cart_item.price)
		return order

#pedido após finalizar o carrinho de compra
class Order(models.Model):

	PAYMENT_CHOICES = (
		('pagseguro','PagSeguro'),
		('deposito','Deposito'),
		('paypal','Paypal'),
	)

	STATUS_CHOICES = (
		(0,'Aguardando Pagamento'),
		(1,'Concluida'),
		(2,'Cancelada'),
	)

	user = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name = "Usuário")
	status = models.IntegerField('Situação',choices=STATUS_CHOICES,default=0,blank=True)
	payment_option = models.CharField('Opção pagamento',choices = PAYMENT_CHOICES,max_length=20,default='deposito')
	created = models.DateTimeField('Criado em',auto_now_add=True)
	modified = models.DateTimeField('Atualizado em',auto_now=True)

	objects = OrderManager()

	class Meta:
		verbose_name = 'Pedido'
		verbose_name_plural = 'Pedidos'

	def __str__(self):
		return 'Pedido #{}'.format(self.pk)

#itens do pedido
class OrderItem(models.Model):

	#related_name serve para referenciar a instancia de Order...Order.itens
	order = models.ForeignKey(Order,verbose_name='Pedido',related_name='itens')
	product = models.ForeignKey('catalog.Product',verbose_name='Produto')
	quantity = models.PositiveIntegerField('Quantidade',default=1)
	price = models.DecimalField('Preço',decimal_places=2,max_digits=8)

	class Meta:
		verbose_name = 'Item do Pedido'
		verbose_name_plural = 'Itens do Pedido'

	def __str__(self):
		return 'Pedido:{}, Produto:{}'.format(self.order,self.product)
	

def post_save_cart_item(instance,**kwargs):
	if instance.quantity < 1:
		instance.delete()


#utilizando o signals que serve como gatilho nesse exemplo se a quantidade for zero o item vai ser removido
models.signals.post_save.connect(post_save_cart_item,sender=CartItem,dispatch_uid='post_save_cart_item')

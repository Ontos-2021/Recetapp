# Tutorial relaciones de Django

Este es un apunte basado en el [tutorial de código facilito](https://youtu.be/oDeHM_SQNnM "YouTube")

El código que el maneja sería más o menos así

``` 
Class Cart(models.Model):
  products = models.ManyToManyField(Product, through='CartProduct')
  
Class CartProduct(models.Model):
  cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
  product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.IntegerField(default=1)
```

- `Product.objects.last()`
- `Product.objects.first()`
- `cart = Cart.objects.create()`
- `cart.products.add(Playera)`
- `cart.products`
- `cart.products.count()`
- Acceder al objeto `cart`
- Así podemos acceder a todos los productor del carro `cart.product.all()`
- `cart.cartproduct_set` y `cart.cartproduct_set.all()` para ver todos los objetos de tipo *cartproduct* relacionados al carrito.
- `cart.cartproduct_set.all().first().quantity`
- `cart.products.add(mochila, through_defaults={'quantity':10})`
- `cart_product = Cart.cartproduct_set.last()` y luego `cart_product.quantity`.
- `cart_product.cart_id` y `cart_product.producto_id`.

Otro ejemplo es así
```
from carts.models import CartProduct

cart_product = CartProduct.objects.last()
cart_product.quantity
10
cart_product.cart
<Cart: Cart object (1)>
add(through_defaults={'quantity': 2})
```

Probando me salió esto:

```
>>> ultimo_ingrediente
<Ingrediente: Masa de pizza>
>>> ultimo_ingrediente.tienda
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Ingrediente' object has no attribute 'tienda'
>>> ultimo_ingrediente.unidad
<Unidad: Unidad>
>>> ultimo_ingrediente.TiendaIngrediente
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Ingrediente' object has no attribute 'TiendaIngrediente'
>>> ultimo_ingrediente.tiendaingrediente_set.all()
<QuerySet [<TiendaIngrediente: Tienda: Chino | Ingrediente: Masa de pizza>]>
>>> Tienda.objects.all()
<QuerySet [<Tienda: Chino>, <Tienda: Verduleria>, <Tienda: Dietética>]>
>>> Tienda.objects.all().last()
<Tienda: Dietética>
>>> Tienda.objects.all().last().tiendaingrediente_set.all()
<QuerySet [<TiendaIngrediente: Tienda: Dietética | Ingrediente: Algas Nori>, <TiendaIngrediente: Tienda: Dietética | Ingrediente: Salmón>]>
>>>
```

Este es el comando para importar los modelos en la shell `>>> from Recetapp.Apps.Recetas.models import *`

---

## ¿Por qué no funciona?

```
<!-- Con este comando esta plantilla se integra en layout.html -->
{% extends 'layout.html' %}

<!-- Bloque para el título de la plantilla -->

{% block title %}

    Recetas

{% endblock %}

<!-- Contenido que irá al bloque de contenido del layout -->

{% block content %}

    {% for receta in recetas %}

        <div class="receta">

            <h2>{{ receta.nombre }}</h2>

                <p>Tiempo: {{ receta.tiempo }}</p>
                
                {% if receta.vegano == True %}
                    <p>Es vegano: Sí</p>
                 {% else %}
                    <p>Es vegano: No</p>
                {% endif %}

                {% for recetaingrediente in receta.recetaingrediente_set.all %}

                    {{ recetaingrediente }}

                [% endfor %}
        </div>

    {% endfor %}

{% endblock %}
```

Me dice esto el error

```
TemplateSyntaxError at /recetas
Invalid block tag on line 39: 'endblock', expected 'empty' or 'endfor'. Did you forget to register or load this tag?
```
  
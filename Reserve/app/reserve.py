def new_sale(request):
    if request.method == 'POST':
        products = ProductForm(request.POST)
        if products.is_valid():
            products.save()
            return redirect('home')
    products = Product.objects.filter(sold=False)
    context = {
        'products': products,
    }
    return render(request,'new_order.html',context)


{% extends 'templatepage.html' %}

{%block title %}
Главная страница
{%endblock%}

{%block content%}
<form method="POST">
    {% csrf_token %}
{% for product in products %}
      <tr>
          <td><input type="checkbox" name="sold" value="{{ product.sold }}"> </td>
          <td><input type="number" name="price" value="{{ product.price }}"></td>
           <td>{{ product.name }}</td>
           <td>{{ product.product_type }}</td>
           <td>{{ product.exp_date }}</td>
         </tr>
{% endfor %}
    <button type="submit" class="btn btn-success">Добавить товар</button>
</form>
{%endblock%}
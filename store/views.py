import openai
from django.shortcuts import render, redirect
from .models import Product
from django.conf import settings

openai.api_key = settings.OPENAI_KEY


def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})


def add_product(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')

        prompt = f"Generate 5 short comma separated tags for this product: {name}. Description: {description}"

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            generated_tags = response['choices'][0]['message']['content'].strip()

        except Exception as e:
            generated_tags = "electronics,gadget"

        Product.objects.create(
            name=name,
            description=description,
            price=price,
            tags=generated_tags
        )

        return redirect('product_list')

    return render(request, 'store/add_product.html')
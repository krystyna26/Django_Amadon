from django.shortcuts import render, HttpResponse, redirect

def index(request):
    products = [
            {"id":1, "name": "Dojo T-shirt", "price": 19.99},
            {"id":2, "name": "Dojo Sweater", "price": 29.99},
            {"id":3, "name": "Dojo Cup", "price": 4.99},
            {"id":4, "name": "Algorithm Book", "price": 49.99},
        ]
    context = {
        "productsList": products
        }
    print context
    return render(request, "store/index.html", context)

def processPurchase(request):
    if request.method == "POST":
        products = [
            {"id":1, "name": "Dojo T-shirt", "price": 19.99},
            {"id":2, "name": "Dojo Sweater", "price": 29.99},
            {"id":3, "name": "Dojo Cup", "price": 4.99},
            {"id":4, "name": "Algorithm Book", "price": 49.99},
        ]
        if not 'totalItem' in request.session:
            request.session['totalItem'] = int(request.POST['quantity'])
        else:
            request.session['totalItem'] += int(request.POST['quantity'])


        for item in products:
            if item["id"] == int(request.POST['product_id']):
                price = item["price"]
        request.session['currentPrice'] = price * int(request.POST['quantity'])



        if not 'totalPrice' in request.session:
            request.session['totalPrice'] = int(request.POST['quantity']) * price
        else:
            request.session['totalPrice'] += int(request.POST['quantity']) * price
        return redirect("/amadon/checkout")
    else:
        return redirect("/amadon/checkout")


def checkout(request):
    return render(request, "store/checkout.html")
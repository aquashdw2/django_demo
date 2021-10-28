from django.shortcuts import render, redirect


from shopping.models import Shop, Item


def shop_home(request, shop_id):
    shop = Shop.objects.get(id=shop_id)
    item_list = Item.objects.filter(shop=shop)
    context = {
        "shop": shop,
        "item_list": item_list,
    }
    return render(request, "shopping/shop-home.html", context)


def shop_item(request, shop_id, item_id):
    shop = Shop.objects.get(id=shop_id)
    item = Item.objects.get(id=item_id)
    context = {
        "shop": shop,
        "item": item,
    }
    return render(request, "shopping/shop-item.html", context)


def shop_admin(request, shop_id):
    shop = Shop.objects.get(id=shop_id)
    item_list = Item.objects.filter(shop=shop)
    context = {
        "shop": shop,
        "item_list": item_list
    }
    return render(request, "shopping/shop-admin.html", context)


def shop_admin_add_item(request, shop_id):
    shop = Shop.objects.get(id=shop_id)

    if request.method == "POST":
        new_item = Item()
        new_item.shop = shop
        new_item.name = request.POST["item_name"]
        new_item.price = int(request.POST["item_price"])
        new_item.save()

        return redirect("shop:admin", shop_id)

    context = {
        "shop": shop,
    }
    return render(request, "shopping/shop-admin-add.html", context)


def shop_admin_edit(request, shop_id, item_id):
    target_item = Item.objects.get(id=item_id)
    if request.method == "POST":
        target_item.name = request.POST["item_name"]
        target_item.price = int(request.POST["item_price"])
        target_item.save()
        return redirect("shop:admin", shop_id)

    shop = Shop.objects.get(id=shop_id)
    context = {
        "item": target_item,
        "shop": shop,
    }
    return render(request, "shopping/shop-admin-edit.html", context)

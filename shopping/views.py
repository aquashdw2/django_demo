from django.shortcuts import render


def shopping_home(request):
    return render(request, "shopping/shop-home.html")


def shopping_admin(request):
    return render(request, "shopping/shop-admin.html")


def shopping_item(request):
    return render(request, "shopping/shop-item.html")


# start here
def shop_home(request, shop_id):
    context = {

    }
    return render(request, "shopping/shop-home.html", context)


def shop_item(request, shop_id, item_id):
    context = {

    }
    return render(request, "shopping/shop-item.html", context)


def shop_admin(request, shop_id):
    context = {

    }
    return render(request, "shopping/shop-admin.html", context)


def shop_admin_add_item(request, shop_id):
    context = {

    }
    return render(request, "shopping/shop-admin-add.html", context)


def shop_admin_edit(request, shop_id, item_id):
    context = {

    }
    return render(request, "shopping/shop-admin-edit.html", context)

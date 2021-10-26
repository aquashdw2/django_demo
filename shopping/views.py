from django.shortcuts import render


def shopping_home(request):
    return render(request, "shopping/index.html")


def shopping_admin(request):
    return render(request, "shopping/admin.html")


def shopping_item(request):
    return render(request, "shopping/item.html")


# start here
def shop_home(request, shop_id):
    context = {

    }
    return render(request, "shopping/index.html", context)


def shop_item(request, shop_id, item_id):
    context = {

    }
    return render(request, "shopping/item.html", context)


def shop_admin(request, shop_id):
    context = {

    }
    return render(request, "shopping/admin.html", context)


def shop_admin_add_item(request, shop_id):
    context = {

    }
    return render(request, "shopping/admin-add.html", context)


def shop_admin_edit(request, shop_id, item_id):
    context = {

    }
    return render(request, "shopping/admin-edit.html", context)

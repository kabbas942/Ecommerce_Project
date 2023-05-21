from shoppingcart.models import Category,Product
def categories(request):
    categoryList= Category.objects.all()
    productCategories=[]
    for category in categoryList:
        productListByCategories = Product.objects.filter(productCategory= category.categoryId)[:10]
        if productListByCategories:
            productCategories.append(category.categoryName)
    return {'productCategories': productCategories}
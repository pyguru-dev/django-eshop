from apps.shop.models import Product


class Basket:
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def __len__(self):
        return sum(item['qty'] for item in self.basket.values())

    def __iter__(self):
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = item['price']
            item['total_price'] = item['price'] * item['qty']
            yield item

    def add(self, product, qty):
        product_id = product.id

        if product_id not in self.basket:
            self.basket[product_id] = {'price': str(product.price), 'qty': qty}
            self.save()


    def delete(self, product):
        product_id = product

        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def update(self, product, qty):
        product_id = product
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
            
        self.save()        
        
    def save(self):
        self.session.modified = True

    def get_total_price(self):
        return sum(item['price'] * item['qty'] for item in self.basket.values())

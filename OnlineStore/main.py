from product import ProductCatalogDB

db=ProductCatalogDB()

db.add_category("fashion")
db.add_product("Shirt",1,400,5)
db.add_product("Jeans",1,800,3)
#
db.update_product(1,600,11)
db.delete_product(2)
db.search_products(800)
db.low_stock_report(5)

db.show_products()

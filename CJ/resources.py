

class CJProduct:
    get_categories = "api/commodity/getCategory"
    view_category = "api/commodity/getCommodity"
    view_product = "api/commodity/detail"
    product_ships_from = "api/product/getAreaInventoryInfo"


class CJOrder:
    create_order = "api/order/createOrders"
    view_orders = "api/order/queryOrders"
    update_order = "api/order/upOrders"
    delete_order = "api/order/deleteOrders"
    search_order = "api/order/queryOrdersByCriteria"
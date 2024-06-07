from repository_pattern.repository import User, Order
from unit_of_work_pattern.unit_of_work import UnitOfWork

if __name__ == "__main__":
    with UnitOfWork() as transaction:

        # register repositories
        transaction.register_repository('user', User)
        transaction.register_repository('order', Order)

        # register new users
        _user = User(_id='', userId='', name='', email='')
        user1 = User(_id="U1", userId="user1", name="John Doe", email="john@example.com")
        user2 = User(_id="U2", userId="user2", name="Jane Doe", email="jane@example.com")
        transaction.register_new(user1, 'user')
        transaction.register_new(user2, 'user')

        # register new orders
        _order = Order(_id='', orderId='', product='', quantity=0)
        order1 = Order(_id="OD1", orderId="order1", product="Laptop", quantity=1)
        order2 = Order(_id="OD2", orderId="order2", product="Phone", quantity=2)
        transaction.register_new(order1, 'order')
        transaction.register_new(order2, 'order')

        # update a user
        user1.name = 'Jagdeep'
        transaction.register_update(user1, 'user')

        # remove a user
        transaction.register_removed(user2, 'user')

    print(_user.get_all())
    print(_order.get_all())

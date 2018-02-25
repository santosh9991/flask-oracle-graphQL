import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import *



class Customer(SQLAlchemyObjectType):
    class Meta:
        model = CustomerModel
        # interfaces = (relay.node,)

class Order(SQLAlchemyObjectType):
    class Meta:
        model = OrderModel
#         interfaces = (relay.node,)

class Query(graphene.ObjectType):
    # node = relay.Node.Field()
    # import ipdb; ipdb.set_trace()
    orders = graphene.List(Order)
    def resolve_orders(self, info):
        print(info)
        query = Order.get_query(info)  # SQLAlchemy query
        return query.all()


schema = graphene.Schema(query=Query)

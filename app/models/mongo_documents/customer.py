"""
Customer Model Module
"""
from mongoengine import Document, StringField, IntField
from app.database.safe_document_mixing import SafeDocumentMixin


class Customer(Document, SafeDocumentMixin):
    """
    Customer Model Class
    """
    name = StringField(required=True)
    age = IntField(required=True)

    meta = {
        'collection': 'clients_crud',
        'indexes': [
            'name'
        ]
    }

    def __init__(self, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)

    @classmethod
    def get_customer_by_name(cls, name):
        """
        :param name: Name of the customer
        :return: Customer
        """
        return Customer.objects_safe(name=name).first()

    @classmethod
    def get_all(cls):
        """
        :return: Customers
        """
        return Customer.objects.all()

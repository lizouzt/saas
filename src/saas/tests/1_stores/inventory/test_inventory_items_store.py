import unittest

from pyramid import testing

import string
import random
import uuid

class TestInventoryItemsStore(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()

        from saas.app.core.services.connection import ConnectionManager
        from saas.app.modules.inventory.stores.items import ItemsStore
        from saas.app.core.stores.client import ClientStore

        self.mgr = ConnectionManager({
            'app.config': '../../etc'
        })
        self.itemsStore = ItemsStore(self.mgr, 'default')
        self.clientStore = ClientStore(self.mgr, 'default')
        self.client = self.clientStore.getDefaultClient()

    def generate_random_str(self, length: int):
        allowed = string.ascii_lowercase + string.digits
        return ''.join(random.choice(allowed) for i in range(length))

    def test_item_add(self):
        random_str = self.generate_random_str(10)
        client_id = self.client[0]
        item_id = str(uuid.uuid4())
        try:
            self.itemsStore.add(
                {
                    'clientId': client_id,
                    'itemId': item_id,
                    'name': random_str,
                    'description': random_str,
                    'make': random_str,
                    'brand': random_str,
                    'model': random_str,
                    'version': random_str,
                    'sku': random_str,
                    'upc': random_str,
                    'length': 1,
                    "length_unit_id": 1,
                    'width': 1,
                    "width_unit_id": 1,
                    'height': 1,
                    "height_unit_id": 1,
                    'weight': 1,
                    "weight_unit_id": 1,
                    'perishable': True,
                    'hazardous': False
                }
            )
        except Exception as e:
            self.fail(e)

    def test_item_get(self):
        random_str = self.generate_random_str(10)
        client_id = self.client[0]
        item_id = str(uuid.uuid4())
        try:
            self.itemsStore.add(
                {
                    'clientId': client_id,
                    'itemId': item_id,
                    'name': random_str,
                    'description': random_str,
                    'make': random_str,
                    'brand': random_str,
                    'model': random_str,
                    'version': random_str,
                    'sku': random_str,
                    'upc': random_str,
                    'length': 1,
                    "length_unit_id": 1,
                    'width': 1,
                    "width_unit_id": 1,
                    'height': 1,
                    "height_unit_id": 1,
                    'weight': 1,
                    "weight_unit_id": 1,
                    'perishable': True,
                    'hazardous': False
                }
            )
            result = self.itemsStore.get(item_id)
            self.assertEqual(item_id, result[0], '{0}'.format(result))
        except Exception as e:
            self.fail(e)

    def test_item_update(self):
        random_str = self.generate_random_str(10)
        client_id = self.client[0]
        item_id = str(uuid.uuid4())
        try:
            self.itemsStore.add(
                {
                    'clientId': client_id,
                    'itemId': item_id,
                    'name': random_str,
                    'description': random_str,
                    'make': random_str,
                    'brand': random_str,
                    'model': random_str,
                    'version': random_str,
                    'sku': random_str,
                    'upc': random_str,
                    'length': 1,
                    "length_unit_id": 1,
                    'width': 1,
                    "width_unit_id": 1,
                    'height': 1,
                    "height_unit_id": 1,
                    'weight': 1,
                    "weight_unit_id": 1,
                    'perishable': True,
                    'hazardous': False
                }
            )

            self.itemsStore.update(
                {
                    'clientId': client_id,
                    'itemId': item_id,
                    'name': random_str,
                    'description': random_str,
                    'make': random_str,
                    'brand': random_str,
                    'model': random_str,
                    'version': random_str,
                    'sku': random_str,
                    'upc': random_str,
                    'length': 1,
                    "length_unit_id": 1,
                    'width': 1,
                    "width_unit_id": 1,
                    'height': 1,
                    "height_unit_id": 1,
                    'weight': 1,
                    "weight_unit_id": 1,
                    'perishable': True,
                    'hazardous': False
                }
            )
        except Exception as e:
            self.fail(e)

    def test_item_add_substitute(self):
        client_id = self.client[0]
        item_id1 = str(uuid.uuid4())
        item_id2 = str(uuid.uuid4())
        item_1 = self.generate_random_str(10)
        item_2 = self.generate_random_str(10)
        try:
            self.itemsStore.add(
                {
                    'clientId': client_id,
                    'itemId': item_id1,
                    'name': item_1,
                    'description': item_1,
                    'make': item_1,
                    'brand': item_1,
                    'model': item_1,
                    'version': item_1,
                    'sku': item_1,
                    'upc': item_1,
                    'length': 1,
                    "length_unit_id": 1,
                    'width': 1,
                    "width_unit_id": 1,
                    'height': 1,
                    "height_unit_id": 1,
                    'weight': 1,
                    "weight_unit_id": 1,
                    'perishable': True,
                    'hazardous': False
                }
            )
            self.itemsStore.add(
                {
                    'clientId': client_id,
                    'itemId': item_id2,
                    'name': item_2,
                    'description': item_2,
                    'make': item_2,
                    'brand': item_2,
                    'model': item_2,
                    'version': item_2,
                    'sku': item_2,
                    'upc': item_2,
                    'length': 1,
                    "length_unit_id": 1,
                    'width': 1,
                    "width_unit_id": 1,
                    'height': 1,
                    "height_unit_id": 1,
                    'weight': 1,
                    "weight_unit_id": 1,
                    'perishable': True,
                    'hazardous': False
                }
            )

            self.itemsStore.addSubstitute(client_id, item_id1, item_id2)
        except Exception as e:
            self.fail(e)

    def test_item_substitutes(self):
        client_id = self.client[0]
        item_id1 = str(uuid.uuid4())
        item_id2 = str(uuid.uuid4())
        item_1 = self.generate_random_str(10)
        item_2 = self.generate_random_str(10)
        try:
            self.itemsStore.add(
                {
                    'clientId': client_id,
                    'itemId': item_id1,
                    'name': item_1,
                    'description': item_1,
                    'make': item_1,
                    'brand': item_1,
                    'model': item_1,
                    'version': item_1,
                    'sku': item_1,
                    'upc': item_1,
                    'length': 1,
                    "length_unit_id": 1,
                    'width': 1,
                    "width_unit_id": 1,
                    'height': 1,
                    "height_unit_id": 1,
                    'weight': 1,
                    "weight_unit_id": 1,
                    'perishable': True,
                    'hazardous': False
                }
            )
            self.itemsStore.add(
                {
                    'clientId': client_id,
                    'itemId': item_id2,
                    'name': item_2,
                    'description': item_2,
                    'make': item_2,
                    'brand': item_2,
                    'model': item_2,
                    'version': item_2,
                    'sku': item_2,
                    'upc': item_2,
                    'length': 1,
                    "length_unit_id": 1,
                    'width': 1,
                    "width_unit_id": 1,
                    'height': 1,
                    "height_unit_id": 1,
                    'weight': 1,
                    "weight_unit_id": 1,
                    'perishable': True,
                    'hazardous': False
                }
            )

            self.itemsStore.addSubstitute(client_id, item_id1, item_id2)

            result = self.itemsStore.substitutes(client_id, item_id1)
            self.assertGreater(len(result), 0, '{0}'.format(result))
        except Exception as e:
            self.fail(e)

    def test_item_add_component(self):
        client_id = self.client[0]
        item_id1 = str(uuid.uuid4())
        item_id2 = str(uuid.uuid4())
        item_1 = self.generate_random_str(10)
        item_2 = self.generate_random_str(10)
        try:
            self.itemsStore.add(
                {
                    'clientId': client_id,
                    'itemId': item_id1,
                    'name': item_1,
                    'description': item_1,
                    'make': item_1,
                    'brand': item_1,
                    'model': item_1,
                    'version': item_1,
                    'sku': item_1,
                    'upc': item_1,
                    'length': 1,
                    "length_unit_id": 1,
                    'width': 1,
                    "width_unit_id": 1,
                    'height': 1,
                    "height_unit_id": 1,
                    'weight': 1,
                    "weight_unit_id": 1,
                    'perishable': True,
                    'hazardous': False
                }
            )
            self.itemsStore.add(
                {
                    'clientId': client_id,
                    'itemId': item_id2,
                    'name': item_2,
                    'description': item_2,
                    'make': item_2,
                    'brand': item_2,
                    'model': item_2,
                    'version': item_2,
                    'sku': item_2,
                    'upc': item_2,
                    'length': 1,
                    "length_unit_id": 1,
                    'width': 1,
                    "width_unit_id": 1,
                    'height': 1,
                    "height_unit_id": 1,
                    'weight': 1,
                    "weight_unit_id": 1,
                    'perishable': True,
                    'hazardous': False
                }
            )

            self.itemsStore.addComponent(client_id, item_id1, item_id2, 1, 1, 1)
        except Exception as e:
            self.fail(e)

    def test_unique_component(self):
        client_id = self.client[0]
        item_id1 = str(uuid.uuid4())
        item_id2 = str(uuid.uuid4())
        item_1 = self.generate_random_str(10)
        item_2 = self.generate_random_str(10)
        try:
            self.itemsStore.add(
                {
                    'clientId': client_id,
                    'itemId': item_id1,
                    'name': item_1,
                    'description': item_1,
                    'make': item_1,
                    'brand': item_1,
                    'model': item_1,
                    'version': item_1,
                    'sku': item_1,
                    'upc': item_1,
                    'length': 1,
                    "length_unit_id": 1,
                    'width': 1,
                    "width_unit_id": 1,
                    'height': 1,
                    "height_unit_id": 1,
                    'weight': 1,
                    "weight_unit_id": 1,
                    'perishable': True,
                    'hazardous': False
                }
            )
            self.itemsStore.add(
                {
                    'clientId': client_id,
                    'itemId': item_id2,
                    'name': item_2,
                    'description': item_2,
                    'make': item_2,
                    'brand': item_2,
                    'model': item_2,
                    'version': item_2,
                    'sku': item_2,
                    'upc': item_2,
                    'length': 1,
                    "length_unit_id": 1,
                    'width': 1,
                    "width_unit_id": 1,
                    'height': 1,
                    "height_unit_id": 1,
                    'weight': 1,
                    "weight_unit_id": 1,
                    'perishable': True,
                    'hazardous': False
                }
            )

            self.itemsStore.addComponent(client_id, item_id1, item_id2, 1, 1, 1)
            self.itemsStore.addComponent(client_id, item_id1, item_id2, 2, 1, 1)
        except Exception as e:
            self.fail(e)

    def test_item_components(self):
        client_id = self.client[0]
        item_id1 = str(uuid.uuid4())
        item_id2 = str(uuid.uuid4())
        item_1 = self.generate_random_str(10)
        item_2 = self.generate_random_str(10)
        try:
            self.itemsStore.add(
                {
                    'clientId': client_id,
                    'itemId': item_id1,
                    'name': item_1,
                    'description': item_1,
                    'make': item_1,
                    'brand': item_1,
                    'model': item_1,
                    'version': item_1,
                    'sku': item_1,
                    'upc': item_1,
                    'length': 1,
                    "length_unit_id": 1,
                    'width': 1,
                    "width_unit_id": 1,
                    'height': 1,
                    "height_unit_id": 1,
                    'weight': 1,
                    "weight_unit_id": 1,
                    'perishable': True,
                    'hazardous': False
                }
            )
            self.itemsStore.add(
                {
                    'clientId': client_id,
                    'itemId': item_id2,
                    'name': item_2,
                    'description': item_2,
                    'make': item_2,
                    'brand': item_2,
                    'model': item_2,
                    'version': item_2,
                    'sku': item_2,
                    'upc': item_2,
                    'length': 1,
                    "length_unit_id": 1,
                    'width': 1,
                    "width_unit_id": 1,
                    'height': 1,
                    "height_unit_id": 1,
                    'weight': 1,
                    "weight_unit_id": 1,
                    'perishable': True,
                    'hazardous': False
                }
            )

            self.itemsStore.addComponent(client_id, item_id1, item_id2, 1, 1, 1)
            result = self.itemsStore.components(client_id, item_id1)
            self.assertGreater(len(result), 0, '{0}'.format(result))
        except Exception as e:
            self.fail(e)

    def test_item_unique_component(self):
        client_id = self.client[0]
        item_id1 = str(uuid.uuid4())
        item_id2 = str(uuid.uuid4())
        item_1 = self.generate_random_str(10)
        item_2 = self.generate_random_str(10)
        try:
            self.itemsStore.add(
                {
                    'clientId': client_id,
                    'itemId': item_id1,
                    'name': item_1,
                    'description': item_1,
                    'make': item_1,
                    'brand': item_1,
                    'model': item_1,
                    'version': item_1,
                    'sku': item_1,
                    'upc': item_1,
                    'length': 1,
                    "length_unit_id": 1,
                    'width': 1,
                    "width_unit_id": 1,
                    'height': 1,
                    "height_unit_id": 1,
                    'weight': 1,
                    "weight_unit_id": 1,
                    'perishable': True,
                    'hazardous': False
                }
            )
            self.itemsStore.add(
                {
                    'clientId': client_id,
                    'itemId': item_id2,
                    'name': item_2,
                    'description': item_2,
                    'make': item_2,
                    'brand': item_2,
                    'model': item_2,
                    'version': item_2,
                    'sku': item_2,
                    'upc': item_2,
                    'length': 1,
                    "length_unit_id": 1,
                    'width': 1,
                    "width_unit_id": 1,
                    'height': 1,
                    "height_unit_id": 1,
                    'weight': 1,
                    "weight_unit_id": 1,
                    'perishable': True,
                    'hazardous': False
                }
            )

            self.itemsStore.addComponent(client_id, item_id1, item_id2, 1, 1, 1)
            self.itemsStore.addComponent(client_id, item_id1, item_id2, 2, 1, 1)
        except Exception as e:
            self.fail(e)
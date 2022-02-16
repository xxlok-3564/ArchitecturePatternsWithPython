from datetime import date
from unittest import TestCase

from chapter1.batch import Batch, OrderLine


class TestBatch(TestCase):

    def test_allocating_to_a_batch_reduces_the_available_quantity(self):
        """
        배치에 새로운 주문 라인을 추가하면 재고에서 사용할 수 있는 수량이 감소한다.
        :return:
        """
        batch = Batch('batch-001', "SMALL-TABLE", quantity=20, eta=date.today())
        line = OrderLine('order-ref', 'SMALL-TABLE', quantity=2)

        batch.allocate(line)

        self.assertTrue(batch.available_quantity == 18)

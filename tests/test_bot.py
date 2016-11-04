# coding: utf-8
from .suite import BaseSuite


class TestBot(BaseSuite):
    def test_action(self):
        rv = self.client.get('/bot/action')
        assert rv.status_code == 200

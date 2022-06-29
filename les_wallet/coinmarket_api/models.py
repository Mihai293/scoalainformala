from django.db import models

coin_choices = (
('btc', 'btc'), ('eth', 'eth'), ('usdt', 'usdt'), ('usdc', 'usdc'), ('bnb', 'bnb'), ('ada', 'ada'), ('xrp', 'xrp'),
('busd', 'busd'), ('sol', 'sol'), ('doge', 'doge'), ('dot', 'dot'), ('wbtc', 'wbtc'), ('trx', 'trx'), ('steth', 'steth'),
('eth', 'eth'), ('eth', 'eth'), ('avax', 'avax'), ('dai', 'dai'), ('shib', 'shib'), ('leo', 'leo'), ('cro', 'cro'),
('ltc', 'ltc'), ('matic', 'matic'), ('near', 'near'), ('ftt', 'ftt'), ('xmr', 'xmr'), ('bch', 'bch'), ('xlm', 'xlm'),
('link', 'link'), ('okb', 'okb'), ('etc', 'etc'), ('xcn', 'xcn'), ('atom', 'atom'), ('algo', 'algo'), ('flow', 'flow'),
('uni', 'uni'), ('icp', 'icp'), ('vet', 'vet'), ('hbar', 'hbar'), ('tfuel', 'tfuel'), ('ape', 'ape'), ('egld', 'egld'),
('xtz', 'xtz'), ('kcs', 'kcs'), ('sand', 'sand'), ('axs', 'axs'), ('fil', 'fil'), ('aave', 'aave'), ('mana', 'mana'),
('ceth', 'ceth'), ('eos', 'eos'), ('theta', 'theta'), ('cusdc', 'cusdc'), ('grt', 'grt'), ('hbtc', 'hbtc'), ('klay', 'klay'),
('zec', 'zec'), ('ht', 'ht'), ('dfi', 'dfi'), ('bsv', 'bsv'), ('mkr', 'mkr'), ('btt', 'btt'), ('miota', 'miota'),
('usdp', 'usdp'), ('hnt', 'hnt'), ('xec', 'xec'))


class Wallet(models.Model):
    coin_number = models.CharField(max_length=100)
    coin_type = models.CharField(max_length=100, choices=coin_choices)

    def __str__(self):
        return f' {self.coin_number}, {self.coin_type}'




class TradeInfo:
    def __init__(self, goods):
        self.total = 0
        self.trades = []

    def __map_to_trade(self, single):
        return dict(
            user_name=single.user.nickname,
            time=single.create_time.strftime('%Y-%m-%d'),
            id=single.id
        )

    def __parse(self, goods):
        pass







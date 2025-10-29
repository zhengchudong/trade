class Trade:
    """交易类，用于表示一笔交易记录"""
    
    def __init__(self, symbol, quantity, price, trade_type):
        """
        初始化交易对象
        
        Args:
            symbol (str): 交易品种代码
            quantity (float): 交易数量
            price (float): 交易价格
            trade_type (str): 交易类型 ('buy' 或 'sell')
        """
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.trade_type = trade_type
        self.trade_value = quantity * price
    
    def __str__(self):
        """返回交易的字符串表示"""
        return f"{self.trade_type.upper()} {self.quantity} {self.symbol} @ {self.price} = {self.trade_value}"


def create_trade(symbol, quantity, price, trade_type):
    """
    创建交易对象的工厂函数
    
    Args:
        symbol (str): 交易品种代码
        quantity (float): 交易数量
        price (float): 交易价格
        trade_type (str): 交易类型 ('buy' 或 'sell')
    
    Returns:
        Trade: 交易对象
    
    Raises:
        ValueError: 如果交易类型无效
    """
    if trade_type not in ['buy', 'sell']:
        raise ValueError("交易类型必须是 'buy' 或 'sell'")
    
    return Trade(symbol, quantity, price, trade_type)


# 示例使用
if __name__ == "__main__":
    # 创建一笔买入交易
    buy_trade = create_trade("BTC/USDT", 0.5, 45000.0, "buy")
    print(f"买入交易: {buy_trade}")
    
    # 创建一笔卖出交易
    sell_trade = create_trade("BTC/USDT", 0.5, 48000.0, "sell")
    print(f"卖出交易: {sell_trade}")
    
    # 计算盈亏
    profit = (sell_trade.trade_value - buy_trade.trade_value)
    print(f"盈亏: {profit} USDT")
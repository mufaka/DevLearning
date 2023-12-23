from helpers import lookup


class Portfolio:
    """
    I am hoping this satisfies the "Personal touch" portion of the requirement
    """

    def __init__(self, db):
        self._db = db 
            
    def get_portfolio(self, user_id):
        sql = """
        SELECT symbol, SUM(quantity) as total_quantity
        FROM transactions
        WHERE user_id = ?
        GROUP BY symbol
        HAVING total_quantity > 0
        ORDER BY symbol ASC
        """

        portfolio = self._db.execute(sql, user_id)

        # update to reflect current price
        for stock in portfolio:
            quote = lookup(stock["symbol"])
            stock["price"] = quote["price"]
            stock["name"] = quote["name"]
            stock["value"] = stock["price"] * stock["total_quantity"]

        return portfolio

    def get_cash(self, user_id):
        sql = """
        SELECT cash 
        FROM users 
        WHERE id = ?
        """

        return self._db.execute(sql, user_id)[0]["cash"]
    
    def update_cash(self, user_id, cash):
        sql = """
        UPDATE users
        SET cash = ?
        WHERE id = ?
        """

        self._db.execute(sql, cash, user_id)

    def buy(self, user_id, symbol, quantity):
        """
        Returns true if the buy was successful, otherwise
        false and a message
        """
        if not symbol:
            return False, "You must provide a symbol."
        
        if not quantity.isdigit():
            return False, "You must provide a quantity of shares."

        if int(quantity) <= 0:
            return False, "Quantity must be greater than zero."
        
        # get the current price
        quote = lookup(symbol)

        if quote is None:
            return False, f"{symbol} was not found."
        
        price = quote["price"]
        cost = int(quantity) * price 
        cash = self.get_cash(user_id)

        if cash < cost:
            return False, "Insufficient cash for this transaction."
        
        # it would be nice if we could wrap these two in a transaction
        self.update_cash(user_id, cash - cost)
        self.save_transaction(user_id, "Buy", symbol, quantity, price)

        return True, f"Successfully purchased {quantity} {symbol}"

    def sell(self, user_id, symbol, quantity):
        """
        Returns true if the sell was successful, otherwise
        false and a message
        """
        if not symbol:
            return False, "You must provide a symbol."
        
        if not quantity.isdigit():
            return False, "You must provide a quantity of shares."

        # ensure quantity is an int
        quantity = int(quantity)

        if quantity <= 0:
            return False, "Quantity must be greater than zero."

        # make sure the user has enough to sell
        portfolio = self.get_portfolio(user_id)
        stock = [s for s in portfolio if s["symbol"] == symbol][0]

        if not stock:
            return False, f"You do not own {symbol}"
        elif stock["total_quantity"] < quantity:
            return False, f"You only have {stock['total_quantity']} {symbol} to sell"

        # we can proceed with the sale; get the current price
        quote = lookup(symbol)

        if quote is None:
            return False, f"{symbol} was not found."

        price = quote["price"]
        total = price * quantity
        cash = self.get_cash(user_id)

        # this should probably be atomic
        self.update_cash(user_id, total + cash)

        self.save_transaction(user_id, "Sell", symbol, quantity * -1, total)

        return True, f"Successfully sold {quantity} {symbol}"

    def save_transaction(self, user_id, tran_type, symbol, quantity, price):
        sql = """
        INSERT INTO transactions 
            (tran_type, user_id, symbol, quantity, price) 
        VALUES 
            (?, ?, ?, ?, ?)
        """

        self._db.execute(sql, tran_type, user_id, symbol, quantity, price)

    def get_transactions(self, user_id):
        sql = """
        SELECT *
        FROM transactions
        WHERE user_id = ? 
        """

        return self._db.execute(sql, user_id)
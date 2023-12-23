import os
import logging 

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
from portfolio import Portfolio 

# Configure application
app = Flask(__name__)

# reference logger
logger = logging.getLogger("werkzeug")

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# create an instance of Portfolio for accessing DB
portfolioDb = Portfolio(db)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    portfolio = portfolioDb.get_portfolio(session["user_id"])
    cash = portfolioDb.get_cash(session["user_id"])
    
    total_assets = cash 

    # add the current values to total assets
    for symbol in portfolio:
        total_assets += symbol["value"]

    return render_template(
        "index.html", portfolio=portfolio, cash=cash, total_assets=total_assets
    )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")

        result, message = portfolioDb.buy(session["user_id"], symbol, shares)

        if not result:
            return apology(message)
        else:
            flash(message)
            return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    stocks = portfolioDb.get_portfolio(session["user_id"])
    
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")

        result, message = portfolioDb.sell(session["user_id"], symbol, shares)

        if not result:
            return apology(message)
        else:
            flash(message)
            return redirect("/")

    else:
        return render_template("sell.html", stocks=stocks)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = portfolioDb.get_transactions(session["user_id"])
    return render_template("transactions.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        quote = lookup(symbol)
        if not quote:
            return apology("Stock symbol does not exist", 400)
        else:
            return render_template("quote.html", quote=quote)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure username was submitted
        if not username:
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not password:
            return apology("must provide password", 403)

        # Ensure confirmation was submitted
        elif not confirmation:
            return apology("must provide confirmation", 403)

        # Ensure that password and confirmation are equal
        elif password != confirmation:
            return apology("password and confirmation must match", 403)
        else:
            # does the user already exist?
            rows = db.execute(
                "SELECT * FROM users WHERE username = ?", request.form.get("username")
            )

            if len(rows) > 0:
                return apology(f"{username} is already taken", 403)
            
            # finally in a place to insert the user. it seems like we could refactor
            # to move the validation but not important here
            hash = generate_password_hash(password)

            try:
                ...
                db.execute(
                    "INSERT INTO users (username, hash) values (?,?)", username, hash
                )
                # this flash message doesn't seem to work ...
                flash(f"Welcome, {username}. Please login!")
                return redirect("/login")
            except:
                return apology(f"a system error prevented your registration", 403)

    else:
        return render_template("register.html")

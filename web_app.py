from flask import Flask, render_template, request, redirect, url_for
from models import db, Trade

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


# ========================
# HOME ROUTE (READ)
# ========================
@app.route("/")
def home():
    trades = Trade.query.all()
    return render_template("index.html", trades=trades)


# ========================
# ADD ROUTE (CREATE)
# ========================
@app.route("/add", methods=["GET", "POST"])
def add_trade():
    if request.method == "POST":
        trade = Trade(
            representative=request.form.get("representative", "").strip(),
            trade_date=request.form.get("trade_date", "").strip(),
            disclosure_date=request.form.get("disclosure_date", "").strip(),
            ticker=request.form.get("ticker", "").strip(),
            asset_type=request.form.get("asset_type", "").strip(),
            transaction_type=request.form.get("transaction_type", "").strip(),
            amount_min=request.form.get("amount_min", "").strip(),
            amount_max=request.form.get("amount_max", "").strip(),
            source=request.form.get("source", "").strip(),
        )

        db.session.add(trade)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("add_trade.html")


# ========================
# EDIT ROUTE (UPDATE)
# ========================
@app.route("/edit/<int:item_id>", methods=["GET", "POST"])
def edit_trade(item_id):
    trade = Trade.query.get_or_404(item_id)

    if request.method == "POST":
        trade.representative = request.form.get("representative", "").strip()
        trade.trade_date = request.form.get("trade_date", "").strip()
        trade.disclosure_date = request.form.get("disclosure_date", "").strip()
        trade.ticker = request.form.get("ticker", "").strip()
        trade.asset_type = request.form.get("asset_type", "").strip()
        trade.transaction_type = request.form.get("transaction_type", "").strip()
        trade.amount_min = request.form.get("amount_min", "").strip()
        trade.amount_max = request.form.get("amount_max", "").strip()
        trade.source = request.form.get("source", "").strip()

        db.session.commit()

        return redirect(url_for("home"))

    return render_template("edit_trade.html", trade=trade)


# ========================
# DELETE ROUTE (DELETE)
# ========================
@app.route("/delete/<int:item_id>")
def delete_trade(item_id):
    trade = Trade.query.get_or_404(item_id)

    db.session.delete(trade)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
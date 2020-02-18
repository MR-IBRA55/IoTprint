from app import app, db, ma


@app.before_first_request
def init_app():
    db.init_app(app)
    ma.init_app(app)


if __name__ == "__main__":
    app.run(debug=True)

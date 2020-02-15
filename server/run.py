from app import app, db

db.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)

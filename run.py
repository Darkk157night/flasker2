from market import app

if __name__ == "__main__":
    app.app_context().push()
    app.run(debug=False,host='0.0.0.0')
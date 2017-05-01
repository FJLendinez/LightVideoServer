from run_it import app as application



if __name__ == "__main__":
    application.config.from_pyfile("./instance/local.py")
    application.run()
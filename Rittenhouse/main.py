import flaskr
import config

app = flaskr.create_app(config)

if __name__ == '__main__':
    app.run()
from flask import current_app, Flask, redirect, url_for

def create_app(config):
    """Creates Flask app from conifg file. Returns crud create function.

    :param config: config file
    :type config:
    :return app: Flask app
    :rtype Flask:
    """
    app = Flask(__name__)
    app.config.from_object(config)

    from .crud import crud
    app.register_blueprint(crud)

    @app.route("/")
    def index():
        return redirect(url_for('crud.create'))

    @app.errorhandler(500)
    def server_error(e):
        return """
           An internal error occurred: <pre>{}</pre>
           See logs for full stacktrace.
           """.format(e), 500

    return app


# config file specifies db
def get_model():
    """Returns backend model dependent on config file

    :return model: either mysql or mssql
    :rtype:
    """
    model_backend = current_app.config['DATA_BACKEND']
    if model_backend == 'mssql':
        from . import model_mssql
        model = model_mssql
    elif model_backend == 'mysql':
        from . import model_mysql
        model = model_mysql
    else:
        raise ValueError(
            "No appropriate databackend configured. "
            "Please specify mssql, mysql")

    return model

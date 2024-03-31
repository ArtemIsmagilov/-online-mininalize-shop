def create_app():
    from flask import Flask

    from .handlers import show_home
    from .settings import Conf, csrf

    app = Flask(__name__)
    app.config.from_object(Conf)

    @app.route("/")
    def home():
        return show_home()

    from .sql_app import cli_commands

    cli_commands.init_app(app)

    from .inventories_app import inventories_bp

    app.register_blueprint(inventories_bp.bp)

    csrf.init_app(app)

    return app

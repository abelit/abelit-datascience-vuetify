from flask.logging import default_handler
from flask import request
import os
import logging
from logging.handlers import RotatingFileHandler


basedir = os.path.abspath(os.path.dirname(__file__))


class RequestFormatter(logging.Formatter):
    def format(self, record):
        record.url = request.url
        record.remote_addr = request.remote_addr
        return super().format(record)


class InfoFilter(logging.Filter):
    def filter(self, record):
        """only use INFO
        筛选, 只需要 INFO 级别的log
        :param record:
        :return:
        """
        if logging.INFO <= record.levelno < logging.ERROR:
            # 已经是INFO级别了
            # 然后利用父类, 返回 1
            return super().filter(record)
        else:
            return 0


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    # 使用docker环境时把127.0.0.1改为db的容器名称
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost/dataforum"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置日志信息
    LOG_PATH = os.path.join(basedir, 'logs')
    LOG_PATH_ERROR = os.path.join(LOG_PATH, 'error.log')
    LOG_PATH_INFO = os.path.join(LOG_PATH, 'info.log')

    # 配置邮件信息
    MAIL_USERNAME = 'ychenid@163.com'
    MAIL_PASSWORD = 'Chen15285649896.'
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    CIRCULATE_MAIL_SENDER = 'ychenid@163.com'
    CIRCULATE_ADMIN = '948640709@qq.com'
    CIRCULATE_MAIL_SUBJECT_PREFIX = 'App Error '

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    DEBUG = False

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # email errors to the administrators
        import logging
        from logging.handlers import RotatingFileHandler
        # Formatter
        # formatter = logging.Formatter(
        #     '%(asctime)s %(levelname)s %(process)d %(thread)d'
        #     '%(module)s %(lineno)s %(message)s')

        formatter = RequestFormatter(
            '[%(asctime)s] %(remote_addr)s requested %(url)s'
            ' --- %(levelname)s in %(module)s: %(message)s'
        )

        # FileHandler Info
        file_handler_info = RotatingFileHandler(filename=cls.LOG_PATH_INFO)
        file_handler_info.setFormatter(formatter)
        file_handler_info.setLevel(logging.INFO)
        info_filter = InfoFilter()
        file_handler_info.addFilter(info_filter)
        app.logger.addHandler(file_handler_info)

        # FileHandler Error
        file_handler_error = RotatingFileHandler(filename=cls.LOG_PATH_ERROR)
        file_handler_error.setFormatter(formatter)
        file_handler_error.setLevel(logging.ERROR)
        app.logger.addHandler(file_handler_error)

        # email errors to the administrators
        import logging
        from logging.handlers import SMTPHandler
        credentials = None
        secure = None
        if getattr(cls, 'MAIL_USERNAME', None) is not None:
            credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
            if getattr(cls, 'MAIL_USE_TLS', None):
                secure = ()
        mail_handler = SMTPHandler(
            mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
            fromaddr=cls.CIRCULATE_MAIL_SENDER,
            toaddrs=[cls.CIRCULATE_ADMIN],
            subject=cls.CIRCULATE_MAIL_SUBJECT_PREFIX + ' Application Error',
            credentials=credentials,
            secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_ECHO = True

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # email errors to the administrators
        import logging
        from logging.handlers import RotatingFileHandler
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s %(levelname)s %(process)d %(thread)d'
            ' in %(module)s %(lineno)s %(message)s')
        # formatter = RequestFormatter(
        #     '[%(asctime)s] %(remote_addr)s requested %(url)s'
        #     ' --- %(levelname)s in %(module)s: %(message)s'
        # )

        # FileHandler Info
        file_handler_info = RotatingFileHandler(filename=cls.LOG_PATH_INFO)
        file_handler_info.setFormatter(formatter)
        file_handler_info.setLevel(logging.INFO)
        info_filter = InfoFilter()
        file_handler_info.addFilter(info_filter)
        app.logger.addHandler(file_handler_info)

        stream_handler = logging.StreamHandler()
        # stream_handler.setFormatter(Formatter)
        stream_handler.setLevel(logging.DEBUG)
        app.logger.addHandler(stream_handler)

        loginfo = logging.getLogger('werkzeug')
        loginfo.setLevel(logging.INFO)
        loginfo.addHandler(file_handler_info)
        loginfo.addHandler(stream_handler)

        # FileHandler Error
        file_handler_error = RotatingFileHandler(filename=cls.LOG_PATH_ERROR)
        file_handler_error.setFormatter(formatter)
        file_handler_error.setLevel(logging.ERROR)
        app.logger.addHandler(file_handler_error)

        # email errors to the administrators
        # import logging
        # from logging.handlers import SMTPHandler
        # credentials = None
        # secure = None
        # if getattr(cls, 'MAIL_USERNAME', None) is not None:
        #     credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
        #     if getattr(cls, 'MAIL_USE_TLS', None):
        #         secure = ()
        # mail_handler = SMTPHandler(
        #     mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
        #     fromaddr=cls.CIRCULATE_MAIL_SENDER,
        #     toaddrs=[cls.CIRCULATE_ADMIN],
        #     subject=cls.CIRCULATE_MAIL_SUBJECT_PREFIX + ' Application Error',
        #     credentials=credentials,
        #     secure=secure)
        # mail_handler.setLevel(logging.ERROR)
        # app.logger.addHandler(mail_handler)


class TestingConfig(Config):
    TESTING = True

"""
Криптография

ПРАКТИЧЕСКИЙ ПРИМЕР — ПРОБЛЕМЫ БЕЗОПАСНОСТИ ПРИ РАЗВЕРТЫВАНИИ МОДЕЛИ МО

"""

print('\n1 -- Предотвращение атаки MITM')
from xmlrpc.client import SafeTransport, ServerProxy
import ssl


class CertVerify(SafeTransport):
    def __init__(self, cafile, certfile=None, keyfile=None):
        SafeTransport.__init__(self)
        self._ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        self._ssl_context.load_verify_locations(cafile)
        if cert:
            self._ssl_context.load_cert_chain(certfile, keyfile)
        self._ssl_context.verify_mode = ssl.CERT_REQUIRED

    def make_connection(self, host):
        s = super().make_connection((host, {'context': self._ssl_context}))
        return s


# Создаем клиентский прокси-сервер
s = ServerProxy('https://cloudanum.com:15000',
                # transport=VerifyCertSafeTransport('server_cert.pem'), allow_none=True)
                transport=CertVerify('server_cert.pem'), allow_none=True)

print('\n2 -- ')

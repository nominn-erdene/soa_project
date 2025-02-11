from spyne import Application, rpc, ServiceBase, Unicode, Double
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class TemperatureService(ServiceBase):

    @rpc(Double, Unicode, _returns=Double)
    def convert_temperature(ctx, value, unit):
        if unit == "CtoF":
            return (value * 9/5) + 32
        elif unit == "FtoC":
            return (value - 32) * 5/9

app = Application([TemperatureService], 
                  tns="http://example.com/",
                  in_protocol=Soap11(validator='lxml'), 
                  out_protocol=Soap11())

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    server = make_server('127.0.0.1', 8000, WsgiApplication(app))
    print("Success http://127.0.0.1:8000")
    server.serve_forever()


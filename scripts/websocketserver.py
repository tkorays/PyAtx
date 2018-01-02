from autobahn.asyncio.websocket import WebSocketServerProtocol, WebSocketServerFactory
import asyncio


class WsServer(WebSocketServerProtocol):
    def onOpen(self):
        print("websocket server open")

    def onMessage(self, payload, isBinary):
        print("recv: ", payload)
        self.sendMessage(payload)

print("start....")
loop = asyncio.get_event_loop()

factory = WebSocketServerFactory()
factory.protocol = WsServer

coro = loop.create_server(factory, '127.0.0.1', 9988)
loop.run_until_complete(coro)
loop.run_forever()


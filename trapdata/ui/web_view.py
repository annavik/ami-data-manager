from time import time

import webview
from webview import Window


class TrapDataWebView:
    title = "AMI Trap Data Companion"
    url = "http://localhost:3000"
    window: Window = None

    def on_start(self):
        self.window.evaluate_js('alert("Hello from Phyton app!")')

    def run(self):
        api = TrapDataWebViewApi()
        self.window = webview.create_window(self.title, self.url, js_api=api)
        api.window = self.window
        webview.start(self.on_start)


class TrapDataWebViewApi:
    window: Window = None

    def send_message(self, content):
        print(content)
        self.window.evaluate_js(
            'window.pywebview.state.setMessage("PONG (%d)")' % time()
        )

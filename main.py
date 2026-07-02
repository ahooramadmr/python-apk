from kivy.app import App
from kivy.uix.button import Button
from jnius import autoclass
from android.runnable import run_on_ui_thread

PythonActivity = autoclass("org.kivy.android.PythonActivity")
WebView = autoclass("android.webkit.WebView")
WebViewClient = autoclass("android.webkit.WebViewClient")


class MyApp(App):

    def build(self):
        btn = Button(text="باز کردن سایت")
        btn.bind(on_press=self.open_site)
        return btn

    @run_on_ui_thread
    def open_site(self, *args):
        activity = PythonActivity.mActivity

        web = WebView(activity)
        web.getSettings().setJavaScriptEnabled(True)
        web.getSettings().setDomStorageEnabled(True)
        web.setWebViewClient(WebViewClient())

        web.loadUrl("https://ahooramadmr.github.io")

        activity.setContentView(web)


MyApp().run()

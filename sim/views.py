import os

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class CaptureView(View):
    def post(self, request, *args, **kwargs) -> HttpResponse:
        url = request.POST.get('url')
        print(f'{url = }')
        if url:
            return self.capture_website(url)
        else:
            return HttpResponse('No url provided', status=400)

    def capture_website(self, url: str) -> HttpResponse:
        """
        Visits the url to take a screenshot.
        """
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        print(f'Getting image for {url = }')
        driver.set_window_size(1920, 1080)

        # Create a path for our screenshot file.
        static_dir = os.path.join('sim', 'static', 'sim')
        os.makedirs(static_dir, exist_ok=True)
        screenshot_path = os.path.join(static_dir, 'screenshot.png')

        driver.save_screenshot(screenshot_path)
        driver.quit()

        return render(self.request, 'preview.html')


def capture_page(request) -> HttpResponse:
    """
    Renders the initial page.
    """
    return render(request, 'capture.html')


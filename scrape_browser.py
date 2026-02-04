# import async playwright
from playwright.async_api import async_playwright
import asyncio

# navigate to url
url = "https://www.amazon.com/"

# enter "potato" into search bar xpath is //*[@id="twotabsearchtextbox"]
search_term = "potato"
search_box_xpath = '//*[@id="twotabsearchtextbox"]'
search_button_xpath = '//*[@id="nav-search-submit-button"]'

# search for "potato"

async def main():
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Navigate to URL
        await page.goto(url)

        # Enter "potato" into search bar
        await page.fill(search_box_xpath, search_term)

        # Press search button
        await page.click(search_button_xpath)

        # Wait a bit to see results
        await page.wait_for_timeout(3000)

        # Close browser
        await browser.close()

# Run the async function
if __name__ == "__main__":
    asyncio.run(main())

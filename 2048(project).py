from playwright.sync_api import sync_playwright
playwright=sync_playwright().start()
browser=playwright.firefox.launch(headless=False,slow_mo=90)
page=browser.new_page()
URL="https://play2048.co/"
page.goto(URL)
page.locator("button.rounded-full").click()
element=page.locator("canvas.absolute.touch-none.object-contain").click()

cycle=[]
while True:
    
    page.keyboard.press("ArrowLeft")
    page.keyboard.press("ArrowUp")
    cycle_end=page.locator("span.shrink-1.truncate").nth(0).text_content()
    cycle.append(cycle_end)
    if len(set(cycle[-5:]))==1:
        page.keyboard.press("ArrowRight")
        if(len(set(cycle[-6:]))==1):
            page.keyboard.press("ArrowDown")
        
    if page.locator("div.absolute.left-0.right-0.bottom-0").nth(1).evaluate("el => getComputedStyle(el).opacity")=="1":
        
        print("Game Over")
        print("Thank You for playing!")
        break

browser.close()
playwright.stop()





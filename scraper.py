import time
import re
import csv
import os
import concurrent.futures
from videogame import VideoGame
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime

#TODO support TROUBLE_CONSOLES_MARIONETTE and TROUBLE_CONSOLES_KILL
#TODO add support for browsers other than firefox in scrollBottom()
#TODO add compression for csv file, convert the three doubles into one value

# console names as they appear in pricecharting.com URLs
CONSOLES = "playstation"

GAMES = ["007-racing"]

NEWGAMES = "007-racing" 

GAME_ATTRIBUTES = ["Genre","Release Date","ESRB Rating","Publisher","Developer","Model Number","Disc Count","Player Count","Also Compatible On","UPC","Description"]

# produce exception "Failed to decode response from marionette" in main()
TROUBLE_CONSOLES_MARIONETTE = ["psp", "nintendo-3ds", "atari-7800", "jaguar"]

# produce exception "invalid argument: can't kill an exited process" in main()
TROUBLE_CONSOLES_KILL = ["sega-cd", "gameboy-color", "playstation-vita", "atari-lynx"]

def gameCsv(games):
    """Creates csv file to store our scraped data

    Args:
        games: (list of videogame objects) videogame data scraped in our program
    """
    dt = datetime.now().strftime("%d.%m.%Y_%H.%M.%S")
    fn = "game_prices.csv"
    fieldnames = ['game', 'console', 'loose_val', 'complete_val', 'new_val', 'Genre', 'Release Date', 'ESRB Rating', 'Publisher', 'Developer', 'Model Number', 'Disc Count', 'Player Count', 'Also Compatible On', 'UPC', 'Description', 'date(D/M/Y)']
    if not os.path.exists(dt):
        os.mkdir(dt)
    with open(os.path.join(dt, fn), 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for g in games:
            writer.writerow({'console': g.getConsole(), 'game': g.getTitle(), 'loose_val': g.getLoosePrice(), 'complete_val': g.getCompletePrice(), 'new_val': g.getNewPrice(), 'Genre': g.getGenre(), 'Release Date': g.getReleaseDate(), 'ESRB Rating': g.getESRBRating(), 'Publisher': g.getPublisher(), 'Developer': g.getDeveloper(), 'Model Number': g.getModelNumber(), 'Disc Count': g.getDiscCount(), 'Player Count': g.getPlayerCount(), 'Also Compatible On': g.getAlsoCompatibleOn(), 'UPC': g.getUPC(), 'Description': g.getDescription(), 'date(D/M/Y)': dt.split('_')[0].replace('.', '/')})


def scrollBottom(console):
    """Scrolls to the bottom of webpage. pricecharting.com/console/<console-name> loads x number of videogames at a time, this loads all
        videogames for our console before we scrape values

    Args:
        console: (string) game system name as it appears in the pricecharting URL

    Returns:
        (browser) html for webpage with all values loaded
    """
    SCROLL_PAUSE_TIME = 1
    browser = webdriver.Firefox()
    if GAMES != [""]:
        browser.get('https://www.pricecharting.com/game/'+ CONSOLES +'/' + NEWGAMES)
    else :
        browser.get('https://www.pricecharting.com/console/' + console)
    prevHeight = browser.execute_script("return document.body.scrollHeight")
    atBottom = False # occasionally selenium lags, this ensures that we are truly at the bottom
    while True:
        time.sleep(SCROLL_PAUSE_TIME)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        currHeight = browser.execute_script("return document.body.scrollHeight")
        if prevHeight == currHeight:
            if atBottom:
                break
            atBottom = True
        else:
            atBottom = False
        prevHeight = currHeight

    return browser


def scrapeVals(console, browser):
    """Scrapes titles and values for each videogame in our webpage
    Args:
        console: (string) game system name as it appears in the pricecharting URL
        browser: (browser) html for webpage with all values loaded
    Returns:
        (list) videogame objects for our console
    """
    games = []
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    for EachPart in soup.select('div[id*="game-page"]'):
        title = str(re.findall(r'>(.*?)</a>', str(EachPart.select('h1[id="product_name"]'))))
        if title:
            print(title)
        loosePrice = re.findall("\d+\.\d+", str(EachPart.select('td[id="used_price"] > span[class="price js-price"]')))
        loosePrice = loosePrice[0] if len(loosePrice) > 0 else "N/A"
        completePrice = re.findall("\d+\.\d+", str(EachPart.select('td[id="complete_price"] > span[class="price js-price"]')))
        completePrice = completePrice[0] if len(completePrice) > 0 else "N/A"
        newPrice = re.findall("\d+\.\d+", str(EachPart.select('td[id="new_price"] > span[class="price js-price"]')))
        newPrice = newPrice[0] if len(newPrice) > 0 else "N/A"
        
        Genre = re.findall("\d+\.\d+", str(EachPart.select('table[id="attribute"] > td[class="details"]')))
        Genre = newPrice[0] if len(Genre) > 0 else "N/A"
        
        ReleaseDate = re.findall("\d+\.\d+", str(EachPart.select('table[id="attribute"] > td[class="details"]')))
        ReleaseDate = ReleaseDate[0] if len(ReleaseDate) > 0 else "N/A"
        
        ESRBRating = re.findall("\d+\.\d+", str(EachPart.select('table[id="attribute"] > td[class="details"]')))
        ESRBRating = ESRBRating[0] if len(ESRBRating) > 0 else "N/A"
        
        Publisher = re.findall("\d+\.\d+", str(EachPart.select('table[id="attribute"] > td[class="details"]')))
        Publisher = Publisher[0] if len(Publisher) > 0 else "N/A"
        
        Developer = re.findall("\d+\.\d+", str(EachPart.select('table[id="attribute"] > td[class="details"]')))
        Developer = Developer[0] if len(Developer) > 0 else "N/A"
        
        ModelNumber = re.findall("\d+\.\d+", str(EachPart.select('table[id="attribute"] > td[class="details"]')))
        ModelNumber = ModelNumber[0] if len(ModelNumber) > 0 else "N/A"
        
        DiscCount = re.findall("\d+\.\d+", str(EachPart.select('table[id="attribute"] > td[class="details"]')))
        DiscCount = DiscCount[0] if len(DiscCount) > 0 else "N/A"
        
        PlayerCount = re.findall("\d+\.\d+", str(EachPart.select('table[id="attribute"] > td[class="details"]')))
        PlayerCount = PlayerCount[0] if len(PlayerCount) > 0 else "N/A"
        
        AlsoCompatibleOn = re.findall("\d+\.\d+", str(EachPart.select('table[id="attribute"] > td[class="details"]')))
        AlsoCompatibleOn = AlsoCompatibleOn[0] if len(AlsoCompatibleOn) > 0 else "N/A"
        
        UPC = re.findall("\d+\.\d+", str(EachPart.select('table[id="attribute"] > td[class="details"]')))
        UPC = UPC[0] if len(UPC) > 0 else "N/A"
        
        Description = re.findall("\d+\.\d+", str(EachPart.select('table[id="new_price"] > td[class="details"]')))
        Description = Description[0] if len(Description) > 0 else "N/A"
        
        newGame = VideoGame(title, console, loosePrice, completePrice, newPrice, Genre, ReleaseDate, ESRBRating, Publisher, Developer, ModelNumber, DiscCount, PlayerCount, AlsoCompatibleOn, UPC, Description)
        games.append(newGame)
    return games


def pullVals(console):
    """Pulls values from pricecharting.com

    Args:
        console: (string) game system name as it appears in the pricecharting URL

    Returns:
        (list) videogame objects
    """
    print ('Pulling values for %s console\n' % (console))
    browser = scrollBottom(console)
    return scrapeVals(console, browser)


def main():
    """Orders execution of our program: scrape vals for each console then create CSV file
    """
    allGames = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        if GAMES != [""]:
            futureGames = {executor.submit(pullVals, games): games for games in GAMES}
            for future in concurrent.futures.as_completed(futureGames):
                scrapedConsole = futureGames[future]
                try:
                    consoleGames = future.result()
                    allGames = allGames + consoleGames
                    print ('%s games successfully scraped\n' % (scrapedConsole))
                except Exception as exc:
                    print ('%s generated an exception: %s' % (scrapedConsole, exc))
        else :    
            futureGames = {executor.submit(pullVals, console): console for console in CONSOLES}
            for future in concurrent.futures.as_completed(futureGames):
                scrapedConsole = futureGames[future]
                try:
                    consoleGames = future.result()
                    allGames = allGames + consoleGames
                    print ('%s console games successfully scraped\n' % (scrapedConsole))
                except Exception as exc:
                    print ('%s console generated an exception: %s' % (scrapedConsole, exc))
    gameCsv(allGames)


if __name__== "__main__":
    """Entry point for our program
    """
    print ('Scraping values from pricecharting.com\n')
    main()
    print ('Finished scraping values from pricecharting.com')

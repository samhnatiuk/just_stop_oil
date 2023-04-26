import requests
from bs4 import BeautifulSoup
import numpy as np
import datetime
import time
import snscrape.modules.twitter as sntwitter

# GETTING DATA FROM ARCHIVED SOCIALBLADE PAGES #

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 "
                  "Safari/537.36"}


def data_getter(url):
    """Given an archived socialblade url, extracts all relevant script for graphs posted on said page. Using this,
     we can copy and paste the relevant raw data from the function's output"""

    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.content, 'html.parser')
    script_divs = soup.find_all('script', {'type': 'text/javascript'})
    return script_divs


# TWITTER
twt_URL = "https://web.archive.org/web/20221106164741/https://socialblade.com/twitter/user/juststop_oil/monthly"
twt_script_divs = data_getter(twt_URL)
print(twt_script_divs)

# Getting appropriate data from output above:
twt_weekly_followers_gained = np.array([[1647489600000, 3558], [1647835200000, 578], [1648440000000, 1058],
                                        [1649044800000, 1808], [1649649600000, 3813], [1650254400000, 1338],
                                        [1650859200000, 892], [1651464000000, 690], [1652068800000, 847],
                                        [1652673600000, 360], [1653278400000, 326], [1653883200000, 680],
                                        [1654488000000, 196], [1655092800000, 453], [1655697600000, 233],
                                        [1656302400000, 621], [1656907200000, 2189], [1657512000000, 263],
                                        [1658116800000, 2126], [1658721600000, 858], [1659326400000, 761],
                                        [1659931200000, 426], [1660536000000, 265], [1661140800000, 1498],
                                        [1661745600000, 704], [1662350400000, 547], [1662955200000, 920],
                                        [1663560000000, 490], [1664164800000, 825], [1664769600000, 1892],
                                        [1665374400000, 11477], [1665979200000, 7513], [1666584000000, 16667]])

twt_weekly_followers = np.array(
    [[1667707200000, 84814], [1667102400000, 76515], [1666411200000, 58056], [1665720000000, 43483],
     [1665028800000, 35598], [1664337600000, 33677], [1663646400000, 33036], [1662955200000, 31913],
     [1662264000000, 31128], [1661572800000, 30165], [1660881600000, 28669], [1660104000000, 28174],
     [1659412800000, 27291], [1658721600000, 26227], [1657857600000, 23581], [1657166400000, 22878],
     [1656475200000, 19983], [1655784000000, 19657], [1655092800000, 19097], [1654401600000, 18792],
     [1653710400000, 18009]])

# FACEBOOK
fb_URL = "https://web.archive.org/web/20221105175159/https://socialblade.com/facebook/page/JustStopOil/monthly"
fb_script_divs = data_getter(fb_URL)
print(fb_script_divs)

# Getting appropriate data from output above:
fb_weekly_likes_gained = np.array(
    [[1647489600000, 564], [1647835200000, 74], [1648440000000, 170], [1649044800000, 223],
     [1649649600000, 563], [1650254400000, 188], [1650859200000, 102], [1651464000000, 79],
     [1652068800000, 65], [1652673600000, 57], [1653364800000, 37], [1653883200000, 31],
     [1654488000000, 36], [1655092800000, 66], [1655697600000, 38], [1656302400000, 61],
     [1656907200000, 238], [1657512000000, 80], [1658116800000, 231], [1658721600000, 93],
     [1659326400000, 170], [1659931200000, 67], [1660536000000, 112], [1661140800000, 124],
     [1661745600000, 86], [1662350400000, 64], [1662955200000, 188], [1663560000000, 239],
     [1664164800000, 300], [1664769600000, 162], [1665374400000, 459], [1665979200000, 406],
     [1666584000000, 283]])

fb_weekly_talking_gained = np.array(
    [[1647489600000, 5995], [1647835200000, -6504], [1648440000000, 987], [1649044800000, 3271],
     [1649649600000, 959], [1650254400000, -3220], [1650859200000, 1377], [1651464000000, -1095],
     [1652068800000, -240], [1652673600000, 2110], [1653364800000, -2321], [1653883200000, -391],
     [1654488000000, -441], [1655092800000, 262], [1655697600000, 505], [1656302400000, 742],
     [1656907200000, 2203], [1657512000000, -3647], [1658116800000, 2930],
     [1658721600000, -2539], [1659326400000, 853], [1659931200000, -945], [1660536000000, 455],
     [1661140800000, 2370], [1661745600000, -2352], [1662350400000, -231], [1662955200000, 5992],
     [1663560000000, 2624], [1664164800000, -3673], [1664769600000, -4543],
     [1665374400000, 6493], [1665979200000, 6930], [1666584000000, -15360]])

fb_weekly_likes = np.array([[1667620800000, 7863], [1667016000000, 7668], [1666324800000, 7286], [1665633600000, 6295],
                            [1664942400000, 6153], [1664251200000, 5746], [1663560000000, 5413], [1662868800000, 5189],
                            [1662091200000, 5095], [1661400000000, 4970], [1660708800000, 4773], [1660017600000, 4689],
                            [1659326400000, 4491], [1658635200000, 4358], [1657944000000, 4095], [1657252800000, 3998],
                            [1656561600000, 3699], [1655870400000, 3642], [1655179200000, 3570], [1654488000000, 3516],
                            [1653796800000, 3469]])

fb_weekly_talking = np.array(
    [[1667620800000, 10325], [1667016000000, 9184], [1666324800000, 26502], [1665633600000, 4764],
     [1664942400000, 11390], [1664251200000, 10906], [1663560000000, 8037], [1662868800000, 1746],
     [1662091200000, 2009], [1661400000000, 4025], [1660708800000, 1253], [1660017600000, 2138],
     [1659326400000, 1912], [1658635200000, 4324], [1657944000000, 1320], [1657252800000, 7026],
     [1656561600000, 1295], [1655870400000, 961], [1655179200000, 1001], [1654488000000, 1275],
     [1653796800000, 3041]])


def data_cleaner(arr, gain=True):
    """Takes the 2d numpy array [[date(i), value(i)]] and splits it into two 1d arrays [date(i)], [value(i)], which
    makes recombining easier. Dates are converted from integers to datetime objects using time"""

    if not gain:
        arr = arr[::-1]
    arr1, arr2 = np.split(arr, 2, axis=1)
    dates, values = arr1.flatten(), arr2.flatten()
    dates = [int(i / 1000) for i in dates]
    dates = [time.strftime('%Y-%m-%d', time.localtime(j)) for j in dates]
    return dates, values


def data_combiner_1():
    """Combining cleaned change in twt followers/fb likes/fb "talking about" data for exporting as a csv"""

    dates, twt_fol = data_cleaner(twt_weekly_followers_gained)
    dates, fb_likes = data_cleaner(fb_weekly_likes_gained)
    dates, fb_talking = data_cleaner(fb_weekly_talking_gained)
    titles = np.asarray(
        [['Date Range', 'Twitter Followers Gained', 'Facebook Likes Gained', 'Facebook "Talking About" Gained']])
    values = np.asarray([[dates[i], twt_fol[i], fb_likes[i], fb_talking[i]] for i in range(len(dates))])
    values = values[1:]  # Cutting first value so each datapoint is separated by 7 days
    return np.concatenate((titles, values), axis=0)


def data_combiner_2():
    """Combining cleaned net twt followers/fb likes/fb "talking about" data for exporting as a csv"""

    dates, fb_likes = data_cleaner(fb_weekly_likes, gain=False)
    dates, fb_talking = data_cleaner(fb_weekly_talking, gain=False)
    dates, twt_fol = data_cleaner(twt_weekly_followers, gain=False)
    titles = np.asarray([['Date Range', 'Facebook Likes', 'Facebook "Talking About"', 'Twitter Followers']])
    values = np.asarray([[dates[i], fb_likes[i], fb_talking[i], twt_fol[i]] for i in range(len(dates))])
    return np.concatenate((titles, values), axis=0)


# noinspection PyTypeChecker
'''np.savetxt("weekly_combined_change_new.csv", data_combiner_1(), delimiter=',', fmt='%s')'''
# noinspection PyTypeChecker
'''np.savetxt('weekly_combined.csv, data_combiner_2(), delimiter=',', fmt='%s')'''


# SCRAPING RAW DATA FROM TWITTER #

def twitter_scraper(search_term, start_date, end_date):
    """Returns the amount of tweets with geotags in the UK for a given search term per day, for each day in between
    two input dates"""

    start, end = datetime.datetime.strptime(start_date, "%Y-%m-%d"), datetime.datetime.strptime(end_date, "%Y-%m-%d")
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days + 1)]
    date_list = [date.strftime("%Y-%m-%d") for date in date_generated]

    # Scraping
    nums = []
    for k in range(len(date_list) - 1):
        count = 0

        # Fetching results (we are only interested in j: number of results)
        for j, s in enumerate(sntwitter.TwitterSearchScraper(search_term + ' since:' + date_list[k] +
                                                             ' until:' + date_list[
                                                                 k + 1] + ' near:"United Kingdom"').get_items()):
            if j > 10000:  # Twitter API limit
                break
            count = j

        if count != 0:
            count += 1
        nums.append(count)

    return date_list, np.array(nums)


def data_combiner_3(start_date, end_date):
    """Combines the results of twitter_scraper into one numpy array, for various search terms."""
    date_list, fossil_fuels = twitter_scraper('"fossil fuels" "just stop oil"', start_date, end_date)
    date_list, just_stop_oil = twitter_scraper('"just stop oil"', start_date, end_date)
    date_list, climate_change = twitter_scraper('"climate change" "just stop oil"', start_date, end_date)
    date_list, net_zero = twitter_scraper('"net zero" "just stop oil"', start_date, end_date)
    titles = np.asarray([['Date', 'Just Stop Oil', 'Climate Change + Just Stop Oil', 'Fossil Fuels + Just Stop Oil',
                          'Net Zero + Just Stop Oil']])
    values = np.asarray([[date_list[i], just_stop_oil[i], climate_change[i], fossil_fuels[i], net_zero[i]] for i
                         in range(len(date_list) - 1)])
    return np.concatenate((titles, values), axis=0)


# noinspection PyTypeChecker
'''np.savetxt("twitter_analytics_all.csv, combiner_3("2022-03-01", "2022-11-06"), delimiter=",", fmt='%s')'''


# SCRAPING RAW DATA FROM GOOGLE

def google_scraper(search_term, start_date, end_date):
    """Returns the amount of google search results for a given search term per week, for each week between
    two given dates"""

    # Creates list of date ranges
    start, end = datetime.datetime.strptime(start_date, "%Y-%m-%d"), datetime.datetime.strptime(end_date,
                                                                                                  "%Y-%m-%d")
    date_generated = [start + datetime.timedelta(days=7 * x) for x in range(0, int(1 / 7 * (end - start).days) + 1)]
    date_list, date_list_ranges = [date.strftime("%Y-%m-%d") for date in date_generated], []
    for s in range(len(date_list) - 1):
        date_list_ranges.append(date_list[s] + '--' + date_list[s + 1])

    # Scraping
    values = []
    for j in range(len(date_list) - 1):
        URL = "https://www.google.co.uk/search?q=allintitle:" + search_term + " after:" + date_list[j] + \
              " before:" + date_list[j + 1]

        result = requests.get(URL, headers=headers)
        soup = BeautifulSoup(result.content, 'html.parser')

        # Fetching number of results
        total_results_text = soup.find("div", {"id": "result-stats"}).find(text=True, recursive=False)

        results_num = ''.join([num for num in total_results_text if num.isdigit()])
        ls.append(results_num)

        time.sleep(2)

    return np.flip(np.rot90(np.asarray([date_list_ranges, values])))


'''np.savetxt("jso_google_search.csv", a, delimiter=",", fmt='%s')'''


from DrissionPage import ChromiumPage
from colorama import Fore, Style
from time import sleep
from sys import argv
from json import dump


red = f"{Fore.RED}"
l_red = f"{Fore.LIGHTRED_EX}"
l_green = f"{Fore.LIGHTGREEN_EX}"
l_blue = f"{Fore.LIGHTBLUE_EX}"
cyan = f"{Fore.LIGHTCYAN_EX}"
magenta = f"{Fore.MAGENTA}"

def parsing(url="https://render-state.to/wp-json/wp/v2/posts?page=1",timeout=5):
    page = ChromiumPage()
    page.clear_cache()
    try:
        page.get(url)
        sleep(timeout)
        i = page.get_frame('@src^https://challenges.cloudflare.com/cdn-cgi')
        e = i('.mark')
        e.click()
        
        sleep(5)
        check_logo = page.ele('')
    except Exception as ex:
        print("Error:", ex)
    finally:
        file_name = url[url.index("=")+1:]
        with open(f'{file_name}.json', 'w') as f:
            dump(page.json, f, indent=4)
            print("\n",Fore.LIGHTYELLOW_EX+f"Json сформирован и сохранен как ' {file_name} '")
            page.close()
            exit()


if __name__=="__main__":
    try:
        timeout = argv[2]
        page_count = argv[1]
        url = f"https://render-state.to/wp-json/wp/v2/posts?page={page_count}"
        parsing(url,timeout)
    except Exception as ex:
        pass
        print()
        print(red+"!!! Аргументы не заданы !!!"+Style.RESET_ALL)
        print()
        print(magenta+"Правильный синтаксис скрипта:"+Style.RESET_ALL)
        print(magenta+"python main.py 'номер_страницы' 'время ожидания прохождения капчи в секундах'"+Style.RESET_ALL)
        print()
        print(l_green+"Образец:",Style.RESET_ALL)
        print(l_green+"python main.py 100 5"+Style.RESET_ALL)
        print()



## 介紹
<br>
1. 這個爬蟲是使用 Selenium 套件完成
2. 提供一次性[防汛網站](https://www.wra.gov.tw/)大量圖片下載 
3. 下載的圖片可以依鄉鎮縣市歸納在資料夾，可以依照檔案內的標示指引，調整不同日期的事件
   - new_event = True 時, 預設為下載最新事件
   - new_event = False 時, 可以在隔一行的 up = number 指定回朔多少次事件

## __專案安裝步驟__

1. 在本地端建立資料夾
```bash
打開終端機 ex. Git Bash 或 命令提示字元
mkdir waterResourcesAgency
cd waterResourcesAgency
```

2. 下載專案
```bash
git clone https://github.com/softtoday72/waterResourcesAgency.git
```

3. 下載套件
```bash
pip install beautifulsoup4 
pip install selenium == 3.141.0
```
下載 [chrome Driver](https://chromedriver.chromium.org/downloads)
版本需選擇當前瀏覽器使用的版本，這邊使用chrome做例子

4. 在 cmd or bash 執行
```
python3 crawler.py
```
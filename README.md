# NetEaseMusicCrawler
Crawling the number of all comments of songs in NetEase Music (an music app famous for its comments).
Surely, the structure can be used in other crawler projects.
![](https://img.shields.io/badge/Python-3.5.2-blue.svg)

The basic structure (demand analysis) is down below: (layer by layer)
1. Crawling all artists info ([artists.py](musicCrawler/artists.py));
2. Based on the artists info we get, continue crawling the albums ([album_by _artist.py](musicCrawler/album_by_artist.py))
3. Based on the albums, crawling songs on each album ([music_by _album.py](musicCrawler/music_by_album.py));
4. Crawling comments for each song ([comments_by _music.py](musicCrawler/comments_by_music.py));
5. Note: All syntax related to database ([sql.py](musicCrawler/sql.py)).


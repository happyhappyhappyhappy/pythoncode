from pytube import YouTube
import my_module
import byte2si
import url_get
import os
import glob
import time
import sys
import youtube_dl

VIDEO_DIR = os.path.join(os.getcwd(), "DL_videos")
OPTS = {
    "outtmpl": "{VIDEO_DIR}/%(title)s.mp4".format(VIDEO_DIR=VIDEO_DIR),
    'ignoreerrors': True
}


def download(url):
    """
    Download video from YouTube.

    Parameters
    ----------
    url : str
        YouTube video URL

    Returns
    ----------
    info : dict
        Downloaded video info.
    """
    print("Downloading {url} start..".format(url=url))
    with youtube_dl.YoutubeDL(OPTS) as y:
        info = y.extract_info(url, download=True)
        print("Downloading {url} finish!".format(url=url))
    return info

def rename(info):
    """
    Rename downloaded video filename as camelcase.

    Parameters
    ----------
    info : dict
        Downloaded video info.
    """
    title = info["title"]
    pattern = '{VIDEO_DIR}/{title}.mp4'.format(VIDEO_DIR=VIDEO_DIR, title=title)
    for v in glob.glob(pattern, recursive=True):
        print("{title}.mp4 found! Renaming start..".format(title=title))
        file_path = os.path.join(VIDEO_DIR, v)
        new_file_path = file_path.replace(' ', '_')
        os.rename(file_path, new_file_path)
        print("Renaming finish!".format(title))


def absfpath(path):
    # ”Download”ディレクトリ下のファイルを取得する
    flist = glob.glob(path + '/*')
    if flist:
        # “Download”ディレクトリ下の1つしかない動画ファイルを取得する
        fpath = os.path.abspath(flist[0])
         # “Download”ディレクトリ下にある動画ファイルの絶対パスを返す
        return fpath
    else:
        raise OSError('The file does not exist.')


def main():
    #プログレスバー
    print('Now executing...')

    # YouTubeアプリからurlを取得
    url = url_get.yturl()
    if not url:
        raise ('Not YouTube')

    print(url)
    info = download(url)
    rename(info)
    abspath = absfpath(VIDEO_DIR)


if __name__ == '__main__':
    # 開始時間を取得
    start = time.time()
    main()
    # 終了時間を少数第3位まで取得
    finish = round(time.time() - start, 3)
    # 実行所要時間を表示
    print('Execute Time:', finish)
    # 終了
    print('Done')
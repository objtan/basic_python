from os import link


class Video:
    def __init__(self, title, link):
        self.title = title
        self.link = link

def read_video():
    title = input('Enter title: ')
    link = input('Enter link: ')
    video = Video(title, link)
    return video

def print_video(video):
    print('Video title: ', video.title)
    print('Video link: ', video.link)

def main():
    vid = read_video()
    print_video(vid)
main()
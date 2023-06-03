import video_processor


class Controller:
    def __init__(self):
        self.controller = video_processor.VideoProcessor()
        self.controller.run()


if __name__ == "__main__":
    start = Controller()

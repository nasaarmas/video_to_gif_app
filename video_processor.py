from model import FileHandler
from model import GifCreation
import view


class VideoProcessor:
    def __init__(self):
        self.view = view.UIController(self)

    def create_gif(self):
        """Function gets the path of video file checks if it has good extension and loops through
        file using frames to write them to output file, this function is invoked in separate thread """
        source_video = FileHandler.video_path  # Get path of video and check if it opened/is video
        if not source_video:
            self.view.show_error("You must specify input file first")
            return

        if not FileHandler.is_video_file(source_video):
            self.view.show_error("Specified file has wrong format")
            return

        output_gif_path = FileHandler.save_filepath
        if not output_gif_path:
            self.view.show_error("You must choose output file", 0)
            return
        model = GifCreation(self.view)
        model.create_gif(source_video, output_gif_path)

    def run(self):
        """function to run main loop"""
        self.view.run()

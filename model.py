import mimetypes
import cv2
import imageio


class FileHandler:
    video_path = ""
    save_filepath = ""

    @staticmethod
    def is_video_file(filepath):
        """Function that checks if input file is a video"""
        extension_checker = mimetypes.guess_type(filepath)[0]
        if extension_checker is not None:
            extension_checker = extension_checker.split('/')[0]
            if extension_checker in ['video']:
                return True
        return False


class GifCreation:
    def __init__(self, view_ui):
        self.output_gif_path = None
        self.source_video = None
        self.view = view_ui

    def create_gif(self, source_vid, gif_output_path):
        self.source_video = source_vid
        self.output_gif_path = gif_output_path
        try:
            just_vid = cv2.VideoCapture(self.source_video)
            fps = just_vid.get(cv2.CAP_PROP_FPS)
            number_frames = int(just_vid.get(cv2.CAP_PROP_FRAME_COUNT))
            try:
                with imageio.get_writer(self.output_gif_path, mode='I', duration=(1000 / fps),
                                        loop=0) as output_gif:  # Creating output gif
                    while just_vid.isOpened():  # Loop through every frame, every loop updates the progress bar
                        ret, frame = just_vid.read()
                        if not ret:
                            break
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        output_gif.append_data(frame)  # Writing current frame to our output file
                        self.view.update_progress(100 / (number_frames * 1.5))  # Update the progress bar

            except Exception as e:
                self.view.show_error(f"Problem with creating output GIF - {str(e)}")
                return
        except Exception as e:
            self.view.show_error(f"Error while opening video file - {str(e)}")
        finally:
            # Closing opened files for clean exit
            just_vid.release()
            self.view.update_progress(100)  # Update the progress bar

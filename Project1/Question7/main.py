from fer import Video
from fer import FER
from matplotlib import pyplot as plt
import pandas as pd


def findHumanEmotion(vid):
    face_detector = FER(mtcnn=True)
    input_video = Video(vid)
    processing_data = input_video.analyze(face_detector, display=False)
    vid_df = input_video.to_pandas(processing_data)
    vid_df = input_video.get_first_face(vid_df)
    vid_df = input_video.get_emotions(vid_df)

    vid_df.plot(figsize=(20, 8), fontsize=16).get_figure()
    plt.show()

    angry = sum(vid_df.angry)
    disgust = sum(vid_df.disgust)
    fear = sum(vid_df.fear)
    happy = sum(vid_df.happy)
    sad = sum(vid_df.sad)
    surprise = sum(vid_df.surprise)
    neutral = sum(vid_df.neutral)

    emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
    emotions_values = [angry, disgust, fear, happy, sad, surprise, neutral]

    score_comparisons = pd.DataFrame(emotions, columns=['Human Emotions'])
    score_comparisons['Emotion Value from the Video'] = emotions_values

    plt.show()




# Put in the location of the video file that has to be processed
location_videofile = "C:/Users/maxwe/OneDrive/Desktop/Homework/CS-5510/Project1/Question7/content/Video_One.mp4"
location_videofile_2 = "C:/Users/maxwe/OneDrive/Desktop/Homework/CS-5510/Project1/Question7/content/Video_Two.mp4"
findHumanEmotion(location_videofile)
findHumanEmotion(location_videofile_2)
# But the Face detection detector
# Input the video for processing
# The Analyze() function will run analysis on every frame of the input video.
# It will create a rectangular box around every image and show the emotion values next to that.
# Finally, the method will publish a new video that will have a box around the face of the human with live emotion values.
# We will now convert the analysed information into a dataframe.
# This will help us import the data as a .CSV file to perform analysis over it later

# Plotting the emotions against time in the video


# We will conclude the project by experimenting the code on another video


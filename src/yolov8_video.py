import cv2
from ultralytics import YOLO


model = YOLO('src/models/updated_model.pt')

# Open the video file
video_path = "dark_bg_videos/video5.avi"
cap = cv2.VideoCapture(video_path)


frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create a VideoWriter object to save the output video
output_path = "dark_bg_videos/video5_with_detections.avi"
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # You can also use 'MJPG', 'X264', etc.
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        out.write(annotated_frame)

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

cap.release()
out.release()
cv2.destroyAllWindows()

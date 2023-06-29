import audio
import head_pose
import detection
import threading as th


if __name__ == "__main__":
    # Create separate threads for each module
    head_pose_thread = th.Thread(target=head_pose.pose)
    audio_thread = th.Thread(target=audio.sound)
    detection_thread = th.Thread(target=detection.run_detection)

    # Start the threads
    head_pose_thread.start()
    audio_thread.start()
    detection_thread.start()

    # Wait for all threads to complete
    head_pose_thread.join()
    audio_thread.join()
    detection_thread.join()

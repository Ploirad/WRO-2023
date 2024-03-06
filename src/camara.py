import picamera

def record_video():
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.framerate = 30
        camera.start_preview()
        # Allow camera warm-up time
        camera.wait_recording(2)

        # Record for 30 seconds
        camera.start_recording('video.h264')
        camera.wait_recording(30)
        camera.stop_recording()

if __name__ == '__main__':
    record_video()

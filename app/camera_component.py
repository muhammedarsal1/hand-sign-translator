import streamlit.components.v1 as components

def camera_input():
    camera_html = """
    <script>
        let video = document.createElement('video');
        video.setAttribute('autoplay', '');
        video.setAttribute('playsinline', '');
        video.style.width = '100%';
        video.style.height = 'auto';

        navigator.mediaDevices.getUserMedia({ video: true })
            .then(stream => {
                video.srcObject = stream;
            })
            .catch(error => {
                console.error("Camera not accessible:", error);
                document.getElementById("camera-container").innerText = "🚨 Camera not accessible. Please enable camera permissions.";
            });

        document.getElementById("camera-container").appendChild(video);
    </script>
    <div id="camera-container"></div>
    """

    components.html(camera_html, height=300)

    return None  # Streamlit does not support direct webcam capture in pure Python

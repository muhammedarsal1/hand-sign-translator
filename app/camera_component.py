import streamlit.components.v1 as components

def camera_input():
    camera_html = """
    <script>
        let video = document.createElement('video');
        let canvas = document.createElement('canvas');
        let context = canvas.getContext('2d');
        let captureButton = document.createElement('button');
        let capturedImage = document.createElement('img');

        video.setAttribute('autoplay', '');
        video.setAttribute('playsinline', '');
        video.style.width = '100%';
        video.style.height = 'auto';

        captureButton.innerText = 'Capture Image';
        captureButton.onclick = function() {
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            context.drawImage(video, 0, 0, canvas.width, canvas.height);
            let imageData = canvas.toDataURL('image/png');

            // Send image data to Streamlit
            window.parent.postMessage(imageData, "*");

            // Show captured image
            capturedImage.src = imageData;
            document.getElementById('captured-container').innerHTML = '';
            document.getElementById('captured-container').appendChild(capturedImage);
        };

        navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } })
            .then(stream => {
                video.srcObject = stream;
                document.getElementById('camera-container').appendChild(video);
                document.getElementById('camera-container').appendChild(captureButton);
            })
            .catch(error => {
                console.error("Camera not accessible:", error);
                document.getElementById("camera-container").innerText = "🚨 Camera not accessible. Please enable camera permissions.";
            });

        document.body.appendChild(capturedImage);
    </script>
    <div id="camera-container"></div>
    <div id="captured-container"></div>
    """
    return components.html(camera_html, height=400)

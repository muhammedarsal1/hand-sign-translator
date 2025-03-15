import streamlit.components.v1 as components

def camera_input():
    camera_html = """
    <script>
        let video = document.createElement('video');
        let canvas = document.createElement('canvas');
        let context = canvas.getContext('2d');
        let captureButton = document.createElement('button');
        let translateButton = document.createElement('button');
        let capturedImage = document.createElement('img');
        let recordedChunks = [];
        let mediaRecorder;

        video.setAttribute('autoplay', '');
        video.setAttribute('playsinline', '');
        video.style.width = '100%';
        video.style.height = 'auto';

        captureButton.innerText = 'Capture Image';
        translateButton.innerText = 'Translate';
        translateButton.style.display = 'none';

        captureButton.onclick = function() {
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            context.drawImage(video, 0, 0, canvas.width, canvas.height);
            capturedImage.src = canvas.toDataURL('image/png');
            document.getElementById('captured-container').innerHTML = '';
            document.getElementById('captured-container').appendChild(capturedImage);
            translateButton.style.display = 'block';
        };

        translateButton.onclick = function() {
            let imageData = capturedImage.src;
            fetch('/predict', {
                method: 'POST',
                body: JSON.stringify({ image: imageData }),
                headers: { 'Content-Type': 'application/json' }
            })
            .then(response => response.json())
            .then(data => {
                alert('Predicted Sign: ' + data.prediction);
            })
            .catch(error => console.error('Error:', error));
        };

        navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } })
            .then(stream => {
                video.srcObject = stream;
                document.getElementById('camera-container').appendChild(video);
                document.getElementById('camera-container').appendChild(captureButton);
                document.getElementById('camera-container').appendChild(translateButton);
            })
            .catch(error => {
                console.error("Camera not accessible:", error);
                document.getElementById("camera-container").innerText = "🚨 Camera not accessible. Please enable camera permissions.";
            });
    </script>
    <div id="camera-container"></div>
    <div id="captured-container"></div>
    """
    components.html(camera_html, height=500)

    return None

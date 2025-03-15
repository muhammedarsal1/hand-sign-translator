import streamlit.components.v1 as components

def camera_input():
    """Camera input component using JavaScript to send images to Streamlit"""
    camera_html = """
    <script>
        let video = document.createElement('video');
        let canvas = document.createElement('canvas');
        let context = canvas.getContext('2d');
        let captureButton = document.createElement('button');
        let translateButton = document.createElement('button');
        let capturedImage = document.createElement('img');
        let hiddenInput = document.createElement('input');

        video.setAttribute('autoplay', '');
        video.setAttribute('playsinline', '');
        video.style.width = '100%';
        video.style.height = 'auto';

        captureButton.innerText = '📸 Capture Image';
        translateButton.innerText = '🔠 Translate Sign';

        captureButton.onclick = function() {
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            context.drawImage(video, 0, 0, canvas.width, canvas.height);
            let imageData = canvas.toDataURL('image/png');

            // ✅ Store image in hidden input
            hiddenInput.value = imageData;

            // ✅ Send image data to Streamlit
            window.parent.postMessage(imageData, "*");

            // ✅ Display captured image
            capturedImage.src = imageData;
            document.getElementById('captured-container').innerHTML = '';
            document.getElementById('captured-container').appendChild(capturedImage);
        };

        translateButton.onclick = function() {
            window.parent.postMessage(hiddenInput.value, "*");
        };

        navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } })
            .then(stream => {
                video.srcObject = stream;
                document.getElementById('camera-container').appendChild(video);
                document.getElementById('camera-container').appendChild(captureButton);
                document.getElementById('camera-container').appendChild(translateButton);
            })
            .catch(error => {
                console.error("🚨 Camera not accessible:", error);
                document.getElementById("camera-container").innerText = "🚨 Camera not accessible. Please enable camera permissions.";
            });
    </script>
    <div id="camera-container"></div>
    <div id="captured-container"></div>
    """
    return components.html(camera_html, height=500)

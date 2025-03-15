import streamlit.components.v1 as components

def camera_input():
    camera_html = """
    <script>
        let video = document.createElement('video');
        let canvas = document.createElement('canvas');
        let context = canvas.getContext('2d');
        let captureButton = document.createElement('button');
        let hiddenInput = document.createElement('input');

        video.setAttribute('autoplay', '');
        video.setAttribute('playsinline', '');
        video.style.width = '100%';
        video.style.height = 'auto';

        captureButton.innerText = 'Capture Image';
        hiddenInput.type = 'text';
        hiddenInput.id = 'capturedImageData';
        hiddenInput.style.display = 'none';

        captureButton.onclick = function() {
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            context.drawImage(video, 0, 0, canvas.width, canvas.height);
            let imageData = canvas.toDataURL('image/png');
            hiddenInput.value = imageData;
            window.parent.postMessage(imageData, "*");
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

        document.body.appendChild(hiddenInput);
    </script>
    <div id="camera-container"></div>
    """
    return components.html(camera_html, height=400)

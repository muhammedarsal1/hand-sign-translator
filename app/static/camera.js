const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

// Start the camera
function startCamera() {
    navigator.mediaDevices.getUserMedia({ video: true })
        .then((stream) => {
            video.srcObject = stream;
        })
        .catch((error) => {
            console.error("🚨 Camera not accessible: ", error);
            alert("🚨 Camera not accessible. Please enable camera permissions.");
        });
}

// Capture frame and send to Python
function captureFrame() {
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    const imageData = canvas.toDataURL("image/jpeg"); // Convert to base64

    fetch("/upload_frame", {
        method: "POST",
        body: JSON.stringify({ image: imageData }),
        headers: { "Content-Type": "application/json" }
    }).then(response => response.json())
      .then(data => console.log("✅ Frame sent:", data))
      .catch(error => console.error("🚨 Error sending frame:", error));
}

// Start the camera when the page loads
document.addEventListener("DOMContentLoaded", startCamera);

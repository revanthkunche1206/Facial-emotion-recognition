const video = document.getElementById('video');
const emotionText = document.getElementById('emotion');

navigator.mediaDevices.getUserMedia({ video: true })
  .then((stream) => {
    video.srcObject = stream;
  });

function captureAndSendFrame() {
  const canvas = document.createElement('canvas');
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  const ctx = canvas.getContext('2d');
  ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

  canvas.toBlob((blob) => {
    const formData = new FormData();
    formData.append('frame', blob, 'frame.jpg');

    fetch('/detect_emotion/', {
      method: 'POST',
      body: formData,
    })
    .then((res) => res.json())
    .then((data) => {
      emotionText.textContent = data.emotion;
    });
  }, 'image/jpeg');
}

setInterval(captureAndSendFrame, 2000);

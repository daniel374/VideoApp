function openModal(videoId) {
    document.getElementById(videoId).style.display = 'flex';
}

function closeModal(videoId) {
    var modal = document.getElementById(videoId);
    modal.style.display = 'none';
    var video = modal.querySelector('video');
    video.pause();
    video.currentTime = 0;
}

function likeVideo(id) {
    alert("Has dado 'Me gusta' al Video " + id);
}
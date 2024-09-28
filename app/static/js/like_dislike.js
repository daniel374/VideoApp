const id_vd = 1;
const isLike = 1;
const url = `/videos/${id_vd}/like`;

function sendLike(isLike, id_vd) {
    fetch(`/videos/${id_vd}/like`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
          id_video_lk: id_vd,
          isLike: isLike
      }), // 1 es el id del video
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // actualiza el número de likes/dislikes en el frontend
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
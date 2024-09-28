function sendLike(isLike, id_vd) {
    fetch('/videos/${id_vd}/like', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
          like: isLike,
          user_id: 1,
          id_vd: id_vd
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
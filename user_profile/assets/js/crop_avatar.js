
const image = document.getElementById("image");
const cropper = new Cropper(image, {
  viewMode: 1,
  zoomable: false,
  aspectRatio: 1 / 1,
  crop(event) {
    document.getElementById("id_x").value = event.detail.x;
    document.getElementById("id_y").value = event.detail.y;
    document.getElementById("id_w").value = event.detail.width;
    document.getElementById("id_h").value = event.detail.height;
  },
});

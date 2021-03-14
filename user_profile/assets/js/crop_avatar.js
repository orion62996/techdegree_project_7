const image = document.getElementById("image");
const cropper = new Cropper(image, {
  viewMode: 2,
  zoomable: false,
  aspectRatio: 1 / 1,
  background: false,
  crop(event) {
    document.getElementById("id_x").value = event.detail.x;
    document.getElementById("id_y").value = event.detail.y;
    document.getElementById("id_width").value = event.detail.width;
    document.getElementById("id_height").value = event.detail.height;
    document.getElementById("id_rotate").value = event.detail.rotate;
    document.getElementById("id_flip").value = event.detail.scaleX;
  },
});

const toggle = document.querySelector('[aria-pressed]');
const flipToggle = document.getElementById("flipToggle");

toggle.addEventListener('click', (e) => {
  if (toggle.ariaPressed === 'true') {
    toggle.ariaPressed = 'false'
    toggle.setAttribute('class', "btn btn-secondary");
    cropper.scaleX(1);
  } else {
    toggle.ariaPressed = 'true'
    toggle.setAttribute('class', "btn btn-primary");
    cropper.scaleX(-1);
  }
});

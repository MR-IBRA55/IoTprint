const myForm = document.getElementById('myForm');
myForm.addEventListener('submit', uploadFile);

var displayName = document.getElementById('displayName')
var fileInput = document.getElementById('gcodeFile')

// function uploadFile(e) {
//   e.preventDefault();
  
//   var formData = new FormData();
//   formData.append("display_name", displayName.value);
//   formData.append("file", fileInput.files[0], "/D:/NEW/USB/Sketches/box.gcode");
  
//   var requestOptions = {
//     method: 'POST',
//     body: formData,
//     redirect: 'follow'
//   };
  
//   fetch("http://127.0.0.1:5000/api/upload", requestOptions)
//     .then(response => response.text())
//     .then(result => console.log(result))
//     .catch(error => console.log('error', error));

// }

function uploadFile(e) {
  e.preventDefault();

  var xhr = new XMLHttpRequest();

  var formData = new FormData();
  formData.append("display_name", displayName.value);
  formData.append("file", fileInput.files[0], "/D:/NEW/USB/Sketches/box.gcode");
  
  xhr.open('POST', 'http://restapi:5000/api/upload', true);

  xhr.onload = function () {
    console.log(JSON.parse(this.response));
  }

  xhr.onerror = function () {
    console.log(JSON.parse(this.response));
  }

  xhr.send(formData);

}
const myForm = document.getElementById('myForm');
myForm.addEventListener('submit', uploadFile);

var displayName = document.getElementById('displayName')
var fileInput = document.getElementById('gcodeFile')


function uploadFile(e) {
  e.preventDefault();

  var xhr = new XMLHttpRequest();

  var formData = new FormData();
  formData.append("display_name", displayName.value);
  formData.append("file", fileInput.files[0]);

  xhr.open('POST', `${document.URL}api/upload`, true);

  xhr.onload = function () {
    console.log(JSON.parse(this.response));
  }

  xhr.send(formData);

}

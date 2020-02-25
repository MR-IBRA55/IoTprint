function displayForm() {
  const btnUploadPage = document.getElementById('btnUploadPage');
  btnUploadPage.addEventListener('click', function () {
    const asideDynamic = document.getElementById('asideDynamic');
    asideDynamic.innerHTML =
      `<form id="uploadForm">
          <label>Display name</label><br>
          <input type="text" id="inpDisplayName" name="displayName" placeholder="ex: 20mmbox"><br>
        
          <label for="myfile">Select a file</label><br>
          <input type="file" id="inpFile" name="file"><br>
          
          <button type="submit">Upload</button>
        </form>
      `
    sendFormData()
  })
}

function sendFormData() {
  const uploadForm = document.getElementById('uploadForm')
  uploadForm.addEventListener('submit', function (e) {
    e.preventDefault()
    var inpDisplayName = document.getElementById('inpDisplayName')
    var inpFile = document.getElementById('inpFile')

    var formData = new FormData();
    formData.append("display_name", inpDisplayName.value);
    formData.append("file", inpFile.files[0]);

    var xhr = new XMLHttpRequest();
    xhr.open('POST', `http://${document.domain}/api/upload`, true);
    xhr.onload = function () {
      alert(JSON.parse(this.response).msg)
    }
    xhr.send(formData);
  })
}

displayForm();

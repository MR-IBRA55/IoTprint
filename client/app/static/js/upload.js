const btnUploadPage = document.getElementById('btnUploadPage');

const uploadForm = document.getElementById('uploadForm');

btnUploadPage.addEventListener('click', function () {
  const asideDynamic = document.getElementById('asideDynamic');
  asideDynamic.innerHTML =
  ` <form id="uploadForm">
      <label>Display name</label><br>
      <input type="text" id="inpDisplayName" name="displayName" placeholder="ex: 20mmbox"><br>
    
      <label for="myfile">Select a file</label><br>
      <input type="file" id="inpFile" name="file">
    </form>
  `
})

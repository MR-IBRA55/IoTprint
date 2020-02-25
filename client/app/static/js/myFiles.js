class MyFiles {
  constructor(endPoint) {
    this.endPoint = endPoint
  }

  fetchData() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', `http://${document.domain}/api/${this.endPoint}`, true);

    xhr.onload = function () {
      if (this.status == 200) {
        var sketches = JSON.parse(this.responseText)
        var output = '';
        for (var sketch in sketches) {
          output +=
            `
            <table class="myFilesTable">
              <tr>
                <th>${sketches[sketch].display_name}</th>
                <td><button class="btnOrderNow" type="button">Order</button></td>
              </tr>
            </table>
          `
          const asideDynamic = document.getElementById('asideDynamic');
          asideDynamic.innerHTML = output
        }
      }
    }
    xhr.send();
  }
}

const btnFilesPage = document.getElementById('btnFilesPage');
const myFiles = new MyFiles('sketches')

btnFilesPage.addEventListener('click', function () {
  myFiles.fetchData()
})

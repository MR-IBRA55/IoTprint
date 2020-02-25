function fetchSketches() {
  const btnFilesPage = document.getElementById('btnFilesPage');
  btnFilesPage.addEventListener('click', function () {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', `http://${document.domain}/api/sketches`, true);

    xhr.onload = function () {
      if (this.status == 200) {
        var sketches = JSON.parse(this.responseText)
        var output = '';
        for (var sketch in sketches) {
          output +=
            `
              <table id=${sketches[sketch]._id} class="myFilesTable">
                <tr>
                  <th>${sketches[sketch].display_name}</th>
                  <td><button class="btnOrderNow" type="button">Order</button></td>
                </tr>
              </table>
            `
          const asideDynamic = document.getElementById('asideDynamic');
          asideDynamic.innerHTML = output
        }
      } else {
        alert(JSON.parse(this.response).msg)
      }
    }
    xhr.send();
    orderNow();
  })

}

function orderNow() {

}


fetchSketches();


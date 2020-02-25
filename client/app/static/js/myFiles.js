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
              <table class="myFilesTable">
                <tr>
                  <th>${sketches[sketch].display_name}</th>
                  <td><button id=${sketches[sketch]._id} class="BtnsOrder" type="button">Order</button></td>
                </tr>
              </table>
            `
          const asideDynamic = document.getElementById('asideDynamic');
          asideDynamic.innerHTML = output
        }
        orderNow();
      } else {
        alert(JSON.parse(this.response).msg)
      }
    }
    xhr.send();
  })

}

function orderNow() {
  var btnsOrder = document.getElementsByClassName("BtnsOrder");
  for (var i = 0; i < btnsOrder.length; i++) {
    btnsOrder[i].addEventListener('click', function (e) {
      var data = JSON.stringify({ "sketch": e.target.id })
      var xhr = new XMLHttpRequest();
      xhr.withCredentials = true;
      xhr.open('POST', `http://${document.domain}/api/order`, true);

      xhr.setRequestHeader("Content-Type", "application/json");
      xhr.setRequestHeader("User", "5e54ed3692d6474676eb19a0");

      xhr.onload = function () {
        alert(JSON.parse(this.response).msg)
      }

      xhr.send(data);
    })
  }
}


fetchSketches();

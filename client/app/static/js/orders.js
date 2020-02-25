
function tableHead() {
  const asideDynamic = document.getElementById('asideDynamic');
  asideDynamic.innerHTML = `<table class="OrdersTable">
                              <thead>
                                <tr>
                                  <th>Filename</th>
                                  <th>Date</th>
                                  <th>Status</th>
                                </tr>
                              </thead>
                              <tbody>
                                
                              </tbody> 
                            </table> 
                            `
}


function fetchOrders() {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', `http://${document.domain}/api/orders`, true);

  xhr.onload = function () {
    if (this.status == 200) {
      var orders = JSON.parse(this.responseText)
      var output = '';
      
      for (var order in orders) {
        output += `
                  <tr>
                    <td>${orders[order].sketch.display_name}</td>
                    <td>${orders[order].date}</td>
                    <td>${orders[order].status}</td>
                  </tr>
                  `
        var ordersTable = document.querySelector('.OrdersTable tbody');
        ordersTable.innerHTML = output
      }
    } else {
      alert(JSON.parse(this.response).msg)
    }
  }
  xhr.send();
}


const btnOrdersPage = document.getElementById('btnOrdersPage');
btnOrdersPage.addEventListener('click', function () {
  tableHead()
  fetchOrders()
})

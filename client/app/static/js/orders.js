class Orders {
  constructor(endPoint) {
    this.endPoint = endPoint
  }

  fetchData() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', `http://${document.domain}/api/${this.endPoint}`, true);
    
    xhr.onload = function () {
      if (this.status == 200) {
        var orders = JSON.parse(this.responseText)
        var output = '';
        for (var order in orders) {
          output +=
        `<table class="ordersTable">
            <tr>
              <th>Filename</th>
              <th>Date</th>
              <th>Status</th>
            </tr>
            <tr>
              <td>${orders[order].sketch.display_name}</td>
              <td>${orders[order].date}</td>
              <td>${orders[order].status}</td>
            </tr>
         </table> 
        `
          const asideDynamic = document.getElementById('asideDynamic');
          asideDynamic.innerHTML = output
        }
      } else if (this.status == 404) {
        console.log(this.responseText)
      }
    }
    xhr.send();
  }
}

const btnOrdersPage = document.getElementById('btnOrdersPage');
const orders = new Orders('orders')

btnOrdersPage.addEventListener('click', function () {
  orders.fetchData()
})


// const btnOrdersPage = document.getElementById('btnOrdersPage');
// btnOrdersPage.addEventListener('click', function () {
//   const asideDynamic = document.getElementById('asideDynamic');
//   asideDynamic.innerHTML =
//   `<table class="ordersTable">
//       <tr>
//         <th>Filename</th>
//         <th>Date</th>
//         <th>Status</th>
//       </tr>
//       <tr>
//         <td>Box</td>
//         <td>24-2-2020 20:00</td>
//         <td>Standby</td>
//       </tr>
//     </table>
//   `
// })

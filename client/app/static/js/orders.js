const btnOrdersPage = document.getElementById('btnOrdersPage');


btnOrdersPage.addEventListener('click', function () {
  const asideDynamic = document.getElementById('asideDynamic');
  asideDynamic.innerHTML =
    `<table id="ordersTable">
      <tr>
        <th>Filename</th>
        <th>Date</th>
        <th>Status</th>
      </tr>
      <tr>
        <td>Box</td>
        <td>24-2-2020 20:00</td>
        <td>Standby</td>
      </tr>
    </table>
  `
})

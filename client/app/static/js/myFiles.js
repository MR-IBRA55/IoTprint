const btnFilesPage = document.getElementById('btnFilesPage');


btnFilesPage.addEventListener('click', function () {
  const asideDynamic = document.getElementById('asideDynamic');
  asideDynamic.innerHTML = 
  `<table id="myFilesTable">
    <tr>
      <th>Filename</th>
      <td><button class="btnOrderNow" type="button">Order</button></td>
    </tr>
   </table>
  `
})
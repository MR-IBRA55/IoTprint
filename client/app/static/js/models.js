const btnModelsPage = document.getElementById('btnModelsPage');


btnModelsPage.addEventListener('click', function () {
  const asideDynamic = document.getElementById('asideDynamic');
  asideDynamic.innerHTML =
  ` <table class="modelsTable">
      <tr>
        <th><img src="../static/img/cube.jpg" alt=""></th>
        <td class="textModels">XYZ Cube</td>
        <td><button class="btnOrderNow" type="button">Order</button></td>
      </tr>
    </table>
  `
})

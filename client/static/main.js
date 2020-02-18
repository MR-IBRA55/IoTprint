const upload = document.getElementById('btnSketch')
console.log(upload)

  const url = 'http://localhost:5000/api/sketches';

upload.addEventListener("click", function(){
  fetch(url, {
    method: 'GET',
  })
  
    .then(data => data.json())
    .then((json) => {
        alert(JSON.stringify(json));
  })  
}); 

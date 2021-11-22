 
function recogerBio(){
    fetch('https://superheroapi.com/api/1080594549377442/70/')
    .then(response => {
        if (response.ok) {
            return response.json();
        } 
        else {
            console.log(response.statusCode)
            return Promise.reject('Error en la respuesta del server')
        }
    })
    .then(data => {
        //Aqui se recoge toda la informacion correspondiente
        console.log(data);
        let p = document.getElementById("boton");
        let titulo = document.createElement("h2");
        titulo.textContent=data.name;
        p.after(titulo);
    })
    .catch(error => console.log('Error: ', error));
}




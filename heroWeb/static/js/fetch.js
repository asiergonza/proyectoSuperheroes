 
function recogerBio(id){
    let boton= document.getElementById('boton');
    boton.className="disappear";
    let boton1 = document.getElementById("boton1");
    boton1.classList.remove("disappear");
    let element = document.getElementById('cuerpo');
    if(typeof(element) != 'undefined' && element != null){

    }else{
        fetch('https://superheroapi.com/api/1080594549377442/'+id+'/')
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
            let contenido = document.createElement('div');
            contenido.setAttribute("id","cuerpo");
            boton.after(contenido);
            //Cargaremos la informacion recogida de la API
            const lista= `<p>`+data.name+` mas conocido como `+data.biography["full-name"]+` es un superheroe perteneciente al editor `+data.biography["publisher"]+` nacido en `+data.biography["place-of-birth"]+`.Ha tenido los siguientes trabajos; `+data.work["occupation"]+` y tiene las siguientes bases; `+data.work["base"]+`.Tiene las siguientes caracteristicas:</p>
            <ul>
                <li>Sexo: `+data.appearance["gender"]+` </li>
                <li>Raza: `+data.appearance["race"]+`  </li>
                <li>Altura: `+data.appearance["height"]+`  </li>
                <li>Peso: `+data.appearance["weight"]+`  </li>
                <li>Color de ojos: `+data.appearance["eye-color"]+`  </li>
                <li>Color de pelo: `+data.appearance["hair-color"]+`  </li>
            </ul>
            <p>Este superheroe tiene los siguientes grupos afiliados: `+data.connections["group-affiliation"]+`. En cuanto a sus powerstats, podemos observar las siguientes:</p>
            <ul>
                <li>Inteligenicia: `+data.powerstats["intelligence"]+` </li>
                <li>Fuerza: `+data.powerstats["strength"]+`  </li>
                <li>Rapidez: `+data.powerstats["speed"]+`  </li>
                <li>Dureza: `+data.powerstats["durability"]+`  </li>
                <li>Poder: `+data.powerstats["power"]+`  </li>
                <li>Combate: `+data.powerstats["combat"]+`  </li>
            </ul>`;
            contenido.innerHTML=lista;
            
        })
        .catch(error => console.log('Error: ', error));
        }
    
}
function borrar(){
    let contenido = document.getElementById("cuerpo");
    contenido.remove();
    let boton = document.getElementById("boton");
    boton.classList.remove("disappear");
    let boton1 = document.getElementById("boton1");
    boton1.className="disappear";
}




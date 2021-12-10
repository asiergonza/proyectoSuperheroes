 
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
            
            let contenido = document.createElement('div');
            contenido.setAttribute("id","cuerpo");
            boton.after(contenido);
            //Cargaremos la informacion recogida de la API
            console.log(data);
            let powerstats= [];
            
            for(let i in data.powerstats){
                if(data.powerstats[i]!= 'null'){
                    powerstats.push(data.powerstats[i]);
                }else{
                    powerstats.push('No hay info');
                }
                
            }
            
            let lista=`<p>`+data.name+` mas conocido como `+data.biography["full-name"]+` es un superheroe perteneciente al editor `+data.biography["publisher"];
           
            if(data.biography["place-of-birth"]!='-'){
                lista= lista+` nacido en `+data.biography["place-of-birth"]+`.`;
            }else{
                lista=lista+`.`;
            }
            if(data.work["occupation"]!='-'){
                lista= lista+` Ha tenido los siguientes trabajos; `+data.work["occupation"];
                if(data.work["base"]!='-'){
                    lista= lista +` y tiene las siguientes bases; `+data.work["base"];
                }
            }else{
                if(data.work["base"]!='-'){
                    lista= lista +` Tiene las siguientes bases; `+data.work["base"];
                }
            }
            lista= lista+`. Tiene las siguientes caracteristicas:</p>`;
            
            
            
            
            const info1=
            `<ul>
                <li>Sexo: `+data.appearance["gender"]+` </li>
                <li>Raza: `+data.appearance["race"]+`  </li>
                <li>Altura: `+data.appearance["height"]+`  </li>
                <li>Peso: `+data.appearance["weight"]+`  </li>
                <li>Color de ojos: `+data.appearance["eye-color"]+`  </li>
                <li>Color de pelo: `+data.appearance["hair-color"]+`  </li>
            </ul>`;
            const info2=`<p>Este superheroe tiene los siguientes grupos afiliados: `+data.connections["group-affiliation"]+`. En cuanto a sus powerstats, podemos observar las siguientes:</p>
            `;
            const estadisticas=`<ul>
                <li>Inteligenicia: `+powerstats[0]+` </li>
                <li>Fuerza: `+powerstats[1]+`  </li>
                <li>Rapidez: `+powerstats[2]+`  </li>
                <li>Dureza: `+powerstats[3]+`  </li>
                <li>Poder: `+powerstats[4]+`  </li>
                <li>Combate: `+powerstats[5]+`  </li>
            </ul>`;
            contenido.innerHTML=lista+info1+info2+estadisticas;
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




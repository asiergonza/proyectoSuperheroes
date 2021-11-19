function recogerBio(){
    fetch('https://superheroapi.com/api/1080594549377442/70')
    .then(response => {
        if (response.ok) {
            return response.json()
        } 
        else {
            console.log(response.statusCode)
            return Promise.reject('Error en la respuesta del server')
        }
    })
    .then(data => console.log(data))
    .catch(error => console.log('Error: ', error));
}




function poll_event_classical(eventKey){

    if (eventKey in keys_classical){
        cannons_positions = [0, 0, 0, 0, 0, 0, 0, 0]
        cannons_positions[keys_classical[eventKey]] = 1
    }
}

function poll_event_quantum(keyList){
    
        fetch("http://127.0.0.1:8000/quantum", 
        {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
                'Accept': 'application/json'
            },
            body:JSON.stringify({keyList})}).then(res=>{
                if(res.ok){
                    return res.json()
                }else{
                    alert("Error en el envío de datos")
                }
            }).then(Response=> foreach_position(Response))
            .catch((err) => console.error(err));
}

var bag = []
function key_bag(eventKey){

    if (eventKey in keys_quantum){
        const index = bag.indexOf(eventKey)
        if (index === -1) {
            bag.push(eventKey);
          } else {
            bag.splice(index, 1);
          }
    }
    poll_event_quantum(bag)
}
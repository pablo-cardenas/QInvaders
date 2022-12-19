function foreach_position(data){
    for(i in player_to_gates){
        if(data.matrix == `[${String(player_to_gates[i])}]`){
            cannons_positions = player_to_gates[i]
        }
    }
    // console.log(data.matrix)
    for(i in quantum_gates){
        if(data.draw == `[${String(quantum_gates[i])}]`){
            cannons_draw = quantum_gates[i]
        }
    }

    // for(i in Object.keys(nuevoArray)){
    //     if(String(cannons_positions) == `${String(Object.keys(nuevoArray)[i])}`){
    //         let clave = Object.keys(nuevoArray)[i]

    //         for (i in quantum_gates){
    //             if (nuevoArray[clave] == `${String(quantum_gates[i])}`){
    //                 cannons_draw = quantum_gates[i]
    //             }
    //         }
    //     }
    // }
    console.log(data.draw)
}

var quantum_activate = false
function switchTF(){
    quantum_activate = !quantum_activate
}
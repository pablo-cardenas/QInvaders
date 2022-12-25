function foreach_position(data){
    for(i in player_to_gates){
        if(data.matrix == `[${String(player_to_gates[i])}]`){
            cannons_positions = player_to_gates[i]
        }
    }
    for(i in quantum_gates){
        if(data.draw == `[${String(quantum_gates[i])}]`){
            cannons_draw = quantum_gates[i]
        }
    }
}

var quantum_activate = false
function switchTF(){
    quantum_activate = !quantum_activate
}
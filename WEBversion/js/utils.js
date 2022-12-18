function foreach_position(position){
    for(i in player_to_gates){
        if(position == `[${String(player_to_gates[i])}]`){
            cannons_positions = player_to_gates[i]
        }
    }
}

var quantum_activate = false
function switchTF(){
    quantum_activate = !quantum_activate
}
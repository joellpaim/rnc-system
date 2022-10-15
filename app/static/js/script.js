
// 2.5 Mostra campo qual padrão após check em Sim
document.getElementById("ha_padrao-0").onclick = function(){
    document.getElementById("qual-padrao-1").style.display = "block";
    document.getElementById("qual-padrao-2").style.display = "block";
    document.getElementById("pergunta-seguido").style.display = "block";
    document.getElementById("e-seguido").style.display = "block";
}
document.getElementById("ha_padrao-1").onclick = function(){
    document.getElementById("qual-padrao-1").style.display = "none";
    document.getElementById("qual-padrao-2").style.display = "none";
    document.getElementById("pergunta-seguido").style.display = "none";
    document.getElementById("e-seguido").style.display = "none";
    const campo = document.getElementById("qual_padrao");

    if (campo.value != ''){
        campo.value = '';
    }
}

// 2.6 Reclamação do procedente - seleciona campo após radio check
document.getElementById("reclamacao_procedente-0").onclick = function(){
    document.getElementById("reclama-sim").style.display = "block";
    document.getElementById("reclama-nao").style.display = "none";
 }

document.getElementById("reclamacao_procedente-1").onclick = function(){
    document.getElementById("reclama-nao").style.display = "block";
    document.getElementById("reclama-sim").style.display = "none";
}

// 2.8 - campos para upload de fotos

let photo1 = document.getElementById('imgPhoto-1');
let file_pos = document.getElementById('imagem_pos');

photo1.addEventListener('click', () => {
    file_pos.click();
})
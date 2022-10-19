
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

let photo2 = document.getElementById('imgPhoto-2');
let file_neg = document.getElementById('imagem_neg');

let photo3 = document.getElementById('imgPhoto-3');
let file_anexo = document.getElementById('anexo_2');

photo1.addEventListener('click', () => {
    file_pos.click();
})

photo2.addEventListener('click', () => {
    file_neg.click();
})

photo3.addEventListener('click', () => {
    file_anexo.click();
})
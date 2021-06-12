
const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')
const url=window.location.href

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click',()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const nombre = modalBtn.getAttribute('data-examen')
    const numero_preguntas = modalBtn.getAttribute('data-preguntas')
    const aprobar = modalBtn.getAttribute('data-pasar')
    const tiempo = modalBtn.getAttribute('data-tiempo')
    console.log(modalBody)
    console.log(pk)
    console.log(nombre)
    console.log(numero_preguntas)
    console.log(aprobar)
    console.log(tiempo)

    modalBody.innerHTML = `
    <div class="h5 mb-3">¿ Esta seguro de que quiere empezar "<b>${nombre}</b>"?</div>
    <div class="text-muted">
        <ul>
            <li>Título: <b>${nombre}</li>
            <li>Número de preguntas: <b>${numero_preguntas}</li>
            <li>Puntuación para pasar: <b>${aprobar}</li>
            <li>Tiempo límite: <b>${tiempo}</li>
        </ul>
    </div>
    `
    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk
    })
}))



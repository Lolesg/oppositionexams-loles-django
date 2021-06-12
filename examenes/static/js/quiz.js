const url = window.location.href

const examenBox = document.getElementById('quiz-box')
const puntuacionBox = document.getElementById('scorebox')
const resultadoBox = document.getElementById('resultbox')
const tiempoBox = document.getElementById('restante')

let timeLimit = document.getElementById('restante');
let tiempo_string = timeLimit.innerHTML;
console.log(tiempo_string);
let tiempo = parseInt(tiempo_string);
console.log(tiempo);
var conteo = new Date(tiempo*60000);

function inicializar(){
    let variable = conteo.getMinutes()+":"+conteo.getSeconds();
    console.log(variable);
    timeLimit.innerHTML = variable;
}

function cuenta(){
    intervaloRegresivo = setInterval("regresiva()",1000);
}

function regresiva(){
    if(conteo.getTime()>0){
        conteo.setTime(conteo.getTime()-1000);
    }
    else{
        clearInterval(intervaloRegresivo);
        alert("El tiempo máximo para realizar el examen ha terminado");
        sendData();
    }
    let variable = conteo.getMinutes()+":"+conteo.getSeconds();
    console.log(variable);
    timeLimit.innerHTML = variable;
}

function detenerContador(){
    clearInterval(intervaloRegresivo);
}
onload = inicializar;
cuenta();


/*
let inicial = document.getElementById('restante')
let tiem = inicial.innerText;
let tiempo = parseInt(tiem);
console.log(tiempo);
let timeInterval = 0;
let p = tiempo*60000;

function actualizar(){
    tiempo--;
    if(tiempo <=0){
        clearInterval(intervalo);
        alert("Tiempo finalizado");
        sendData();

    }
    else{
        document.getElementById('restante').innerHTML=tiempo;
    }
    
}

function Contador(){
    intervalo = setInterval(actualizar,60000);
}

function detenerContador(){
    clearInterval(intervalo)
}

Contador();
*/

$.ajax({
    type: 'GET',
    url:`${url}/data`,
    success: function(response){
        const dato = response.data
        dato.forEach(el => {
            for(const [pregunta,respuestas] of Object.entries(el)){
                examenBox.innerHTML += `
                
                <div class="mb-2">
                    <b>${pregunta}</b>
                </div>
                `
                respuestas.forEach(respuesta => {
                    examenBox. innerHTML += `
                    <div class="diseno">
                        <input type="radio" class="ans" id="${pregunta}-${respuesta}" name="${pregunta}" value="${respuesta}">
                        <label for="${pregunta}">${respuesta}</label>
                    </div>
                    `
                })
            }
        });
        
    },
    error: function(error){
        console.log(error)
    }
    
})
/*
timeInterval= setInterval( ()=> {
    tiempo--
    if(tiempo>0){
        alert("El tiempo se ha terminado");
        clearInterval(timeInterval);
    }
    else{
        console.log(tiempo);
        document.getElementsByClassName('restante').innerHTML=tiempo;
    }
},p)
*/




const quizBox = document.getElementById('quiz-box')
const scoreBox = document.getElementById('scorebox')
const resultBox = document.getElementById('resultbox')



const quizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')


const sendData = () => {
    const elements =[...document.getElementsByClassName('ans')]
    const data = {}
    document.getElementById('restante').innerHTML=`Examen finalizado`;
    data['csrfmiddlewaretoken'] = csrf[0].value 
    elements.forEach(el=>{
        if(el.checked){
            data[el.name] = el.value
        }
        else {
            if(!data[el.name]){
                data[el.name] = null
            }
        }
    })
    $.ajax({
        type:'POST',
        url:`${url}/save/`,
        data: data,
        success: function(response){
            console.log(response)
            const results = response.resultados
            console.log(results)
            quizForm.classList.add('not-visible')

            scoreBox.innerHTML += `Tu resultado es: ${response.nota}`
            console.log(scoreBox)

            results.forEach(res=>{
                const resDiv = document.createElement("div")
                for(const [question,resp] of Object.entries(res)){
                    resDiv.innerHTML += question
                    const cls = ['container','p-3','text-light','h3']
                    resDiv.classList.add(...cls)

                    if(resp=='No respondida'){
                        resDiv.innerHTML += '- no respondida'
                        resDiv.classList.add('bg-danger')
                    }
                    else{
                        const answer = resp['respuesta']
                        const correct = resp['Respuesta_correcta']


                        if(answer == correct){
                            resDiv.classList.add('bg-success')
                            resDiv.innerHTML += ` Tu respuesta: ${answer}`
                        }
                        else{
                            resDiv.classList.add('bg-danger')
                            resDiv.innerHTML += ` | La respuesta válida es: ${correct}`
                            resDiv.innerHTML += ` | Tu respuesta: ${answer}`
                        }
                    }

                }

                const finalizar = document.getElementById('finalizar')
                finalizar.append(resDiv)
            })
            const boton = document.getElementById('boton')
            boton.classList.add("btn")
            boton.classList.add("btn-primary")
            boton.classList.add("mt-3")
            boton.classList.remove("not-visible")

        },
        error: function(error){
            console.log(error)
        }
    })
}

quizForm.addEventListener('submit', e=> {
    e.preventDefault()

    sendData()
})




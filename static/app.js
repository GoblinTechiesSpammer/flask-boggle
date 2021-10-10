// Event handler for word guess form.
const $wordGuess = $("#word-guess");
$wordGuess.submit(wordGuessForm);

async function wordGuessForm(event){
    event.preventDefault();

    const $guess = $("#guess");
    let word = $guess.val();
    let response = await axios.get("/guess", {params: {word: word}});
    console.log(response.data.result);

    //Update guess feedback on page.
    updateGuess(response.data.result);

    //Update score on page.
    updateScore(response.data.score);
}

function updateGuess(result){
    $(".guess-result").empty();
    $(".guess-result").append(`<p>${result}</p>`);
}

function updateScore(score){
    $(".score").empty();
    $(".score").append(`<p>${score}</p>`);
}


// Timer for stopping game after 60 seconds.
const $timer = $(".timer");
var startTime = 0;

// How would I disable more submissions?
var time = setInterval(tickTock, 1000);

function tickTock(){
    if (startTime >= 60){
        $wordGuess.remove();
        clearInterval(time);
    }
    else{
        startTime += 1;
        $timer.text(startTime);
    }
}
const $wordGuess = $("#word-guess");

$wordGuess.submit(async function(event){
    event.preventDefault();

    const $guess = $("#guess");
    let word = $guess.val();
    let response = await axios.get("/guess", {params: {word: word}});
    console.log(response.data.result);
    $(".guess-result").empty();
    $(".guess-result").append(`<p>${response.data.result}</p>`);

    // Score
    $(".score").empty();
    $(".score").append(`<p>${response.data.score}</p>`);
});
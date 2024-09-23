let score = 0;
let workers = 0;
let workerCost = 10;

// Function to play sound
function playSound(src) {
    let audio = new Audio(src);
    audio.play();
}

document.getElementById('cookie').addEventListener('click', function() {
    score += 1;
    document.getElementById('score').textContent = `Points: ${score}`;
    playSound('images/click.mp3'); // Play click sound
});

document.getElementById('buyWorker').addEventListener('click', function() {
    if (score >= workerCost) {
        score -= workerCost;
        workers += 1;
        workerCost = Math.floor(workerCost * 1.5); // Increase cost for next worker
        document.getElementById('score').textContent = `Points: ${score}`;
        document.getElementById('workers').textContent = `Workers: ${workers}`;
        document.getElementById('buyWorker').textContent = `Buy Worker (Cost: ${workerCost})`;
    }
});

// Add passive income from workers
setInterval(function() {
    score += workers;
    document.getElementById('score').textContent = `Points: ${score}`;
}, 1000); // Update every second

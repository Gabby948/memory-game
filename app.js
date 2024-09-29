// Lógica del Juego de Memoria en formato SPA
(function () {
    const app = document.getElementById('app');
  
    // Cartas y variables globales
    const cardsArray = ['🍎', '🍌', '🍓', '🍍', '🍇', '🍉', '🥝', '🍒'];
    let shuffledCards = [...cardsArray, ...cardsArray].sort(() => 0.5 - Math.random());
    console.log(shuffledCards);
    let firstCard = null;
    let secondCard = null;
    let matchedPairs = 0;
    let timeLeft = 60;
    let timerInterval;
  
    // Función para renderizar la estructura principal de la SPA
    function render() {
      app.innerHTML = `
        <h1>Juego de Memoria</h1>
        <div id="game-board"></div>
        <div class="info">
          <p>Tiempo restante: <span id="timer">${timeLeft}</span> segundos</p>
          <button id="reset-button">Reiniciar</button>
        </div>
      `;
      createBoard();
      document.getElementById('reset-button').addEventListener('click', resetGame);
      startTimer();
    }
  
    // Crear las cartas en el tablero
    function createBoard() {
      const gameBoard = document.getElementById('game-board');
      gameBoard.innerHTML = '';
      shuffledCards.forEach((emoji) => {
        const card = document.createElement('div');
        card.classList.add('card');
        card.dataset.emoji = emoji;
        card.addEventListener('click', flipCard);
        gameBoard.appendChild(card);
      });
    }
  
    // Función para voltear las cartas
    function flipCard(event) {
      const selectedCard = event.target;
      if (selectedCard === firstCard || selectedCard.classList.contains('matched')) return;
  
      selectedCard.textContent = selectedCard.dataset.emoji;
  
      if (!firstCard) {
        firstCard = selectedCard;
      } else {
        secondCard = selectedCard;
        checkMatch();
      }
    }
  
    // Verificar si las cartas coinciden
    function checkMatch() {
      if (firstCard.dataset.emoji === secondCard.dataset.emoji) {
        firstCard.classList.add('matched');
        secondCard.classList.add('matched');
        matchedPairs++;
        resetSelections();
        checkWin();
      } else {
        setTimeout(() => {
          firstCard.textContent = '';
          secondCard.textContent = '';
          resetSelections();
        }, 1000);
      }
    }
  
    // Reiniciar selección de cartas
    function resetSelections() {
      firstCard = null;
      secondCard = null;
    }
  
    // Verificar si se ha ganado el juego
    function checkWin() {
      if (matchedPairs === cardsArray.length) {
        clearInterval(timerInterval);
        alert('¡Ganaste! Felicidades 🎉');
      }
    }
  
    // Iniciar el temporizador
    function startTimer() {
      timerInterval = setInterval(() => {
        timeLeft--;
        document.getElementById('timer').textContent = timeLeft;
        if (timeLeft === 0) {
          clearInterval(timerInterval);
          alert('¡Se acabó el tiempo! Intenta de nuevo.');
          resetGame();
        }
      }, 1000);
    }
  
    // Reiniciar el juego
    function resetGame() {
      matchedPairs = 0;
      timeLeft = 60;
      shuffledCards = [...cardsArray, ...cardsArray].sort(() => 0.5 - Math.random());
      clearInterval(timerInterval);
      render();
    }
  
    // Renderizar la SPA
    render();
  })();
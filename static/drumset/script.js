function playSound(e) {
    // Get information about key press.
    const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`);
    const key = document.querySelector(`.key[data-key="${e.keyCode}"]`);

    //stop the function if there is no audio associated with key.
    if (!audio) return;

    //rewind to start to allow for multiple quick key presses.
    audio.currentTime = 0;

    // play sound.
    audio.play();

    // add playing to class list for transition effect.
    key.classList.add('playing');
}

function removeTransition(e) {
    if (e.propertyName !== 'transform') return;
    this.classList.remove('playing');
}

const keys = document.querySelectorAll('.key');
keys.forEach(key => key.addEventListener('transitionend', removeTransition));

// Attach event listener for key down presses.
window.addEventListener('keydown', playSound);

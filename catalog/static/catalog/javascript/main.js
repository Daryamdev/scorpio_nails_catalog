document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('stars-container');
    if (!container) return;

    const starCount = 300;

    for (let i = 0; i < starCount; i++) {
        const star = document.createElement('div');
        star.classList.add('star');

        const top = Math.random() * 100;
        const left = Math.random() * 100;
        const size = Math.random() * 2.5 + 0.8;
        const duration = Math.random() * 3 + 1.5;
        const delay = Math.random() * 5;

        star.style.top = `${top}%`;
        star.style.left = `${left}%`;
        star.style.width = `${size}px`;
        star.style.height = `${size}px`;
        star.style.setProperty('--duration', `${duration}s`);
        star.style.setProperty('--delay', `${delay}s`);

        if (i % 6 === 0) {
            star.classList.add('bright');
        }

        container.appendChild(star);
    }
});
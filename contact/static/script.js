const menuBtn = document.getElementById('menu-btn');
const dropdown = document.getElementById('dropdown');

menuBtn.addEventListener('click', () => {
    dropdown.classList.toggle('open');
    menuBtn.classList.toggle('open');
});
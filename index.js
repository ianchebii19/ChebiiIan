function handleMenuIconClick() {
  const menuIcon = document.querySelector('.menuIcon');
  const sidebar = document.querySelector('.sidebar');
  const bxa = document.querySelector('#bxa');
  const far = document.querySelector('#far');
  
  menuIcon.addEventListener('click', function() {
    sidebar.style.display = 'block';
    bxa.style.display = 'block';
    far.style.display = 'none';
  });
}

function handleBxaClick() {
  const menuIcon = document.querySelector('.menuIcon');
  const bxa = document.querySelector('#bxa');
  const far = document.querySelector('#far');
  const sidebar = document.querySelector('.sidebar');
  const bxaa = document.querySelector('.bxaa');
  
  bxa.addEventListener('click', function() {
    far.style.display = 'block';
    sidebar.style.display = 'none';
    bxa.style.display = 'none';

  });
}
handleMenuIconClick();
  handleBxaClick();



function toggleContent(id) {
  var contents = document.getElementsByClassName("content");
  for (var i = 0; i < contents.length; i++) {
      if (contents[i].id !== id) { // Only add 'active' class to the clicked content
          contents[i].classList.remove("active");
      }
  }
  document.getElementById(id).classList.add("active");
}

document.addEventListener('DOMContentLoaded', function() {
  const words = document.querySelectorAll('.word');
  let index = 0;

  function rotateWords() {
      const currentWord = words[index];
      const nextWord = words[(index + 1) % words.length];

      currentWord.style.transform = 'rotateX(90deg)';
      nextWord.style.transform = 'rotateX(0deg)';

      index = (index + 1) % words.length;
  }

  setInterval(rotateWords, 2000); // Adjust the interval as needed
});

function showAbout() {
  var aboutSection = document.getElementById('about');
  aboutSection.style.display = (aboutSection.style.display === 'none' || aboutSection.style.display === '') ? 'block' : 'none';
};




document.addEventListener('DOMContentLoaded', () => {
  const textArray = ["Future YouTuber", "Programmer", "Tech Enthusiast"];
  const typingDelay = 100;
  const erasingDelay = 50;
  const newTextDelay = 2000; // Delay between current and next text
  let textArrayIndex = 0;
  let charIndex = 0;

  const typewriterElement = document.getElementById("typewriter");

  function type() {
    if (charIndex < textArray[textArrayIndex].length) {
      typewriterElement.textContent += textArray[textArrayIndex].charAt(charIndex);
      charIndex++;
      setTimeout(type, typingDelay);
    } else {
      setTimeout(erase, newTextDelay);
    }
  }

  function erase() {
    if (charIndex > 0) {
      typewriterElement.textContent = textArray[textArrayIndex].substring(0, charIndex - 1);
      charIndex--;
      setTimeout(erase, erasingDelay);
    } else {
      textArrayIndex++;
      if (textArrayIndex >= textArray.length) textArrayIndex = 0;
      setTimeout(type, typingDelay + 1100);
    }
  }

  // Initiate typing effect
  if (textArray.length) setTimeout(type, newTextDelay + 250);
});
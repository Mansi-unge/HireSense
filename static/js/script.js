// Count words in job description textarea
function countWords() {
  const textarea = document.querySelector('textarea');
  if (!textarea) return;
  const text = textarea.value.trim();
  document.getElementById("wordCount").innerText =
    text ? text.split(/\s+/).length : 0;
}

// Show loading overlay when form is submitted
function showLoader(event) {
  const form = document.querySelector('form');
  if (!form) return;
  document.getElementById("loading").style.display = "flex";
}

// Attach event listeners after DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  const textarea = document.querySelector('textarea');
  if (textarea) {
    textarea.addEventListener('input', countWords);
  }

  const form = document.querySelector('form');
  if (form) {
    form.addEventListener('submit', showLoader);
  }
});

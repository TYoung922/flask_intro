setTimeout(() => {
  const flashContainer = document.getElementById("flash-message");
  if (flashContainer) {
    flashContainer.style.display = "none";
  }
}, 5000);

function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

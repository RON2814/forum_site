document
  .getElementById("dropdownButton")
  .addEventListener("click", function () {
    var menu = document.getElementById("dropdownMenu");
    menu.classList.toggle("hidden");
  });

// Close dropdown when clicking outside
window.addEventListener("click", function (e) {
  var dropdown = document.getElementById("dropdownMenu");
  var button = document.getElementById("dropdownButton");
  if (!button.contains(e.target)) {
    dropdown.classList.add("hidden");
  }
});

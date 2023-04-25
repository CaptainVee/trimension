// get all panel elements and count their number
var panels = document.querySelectorAll(".panel");
var numPanels = panels.length;

// if a panel is open, lower its z-idx
// otherwise, set zIdx back to original
function checkZ(aPanel) {
  if (aPanel.classList.contains("open")) {
    aPanel.style.zIndex = "1";
  } else {
    // set z-index back to original stored in data
    var zIdx = aPanel.dataset.zIdx;
    aPanel.style.zIndex = zIdx;
  }
}

// loop through all panels and reverse sort via zIdx
for (var i = 0; i < numPanels; i++) {
  var zIdx = numPanels - i;
  panels[i].style.zIndex = zIdx;
  panels[i].dataset.zIdx = zIdx;
}

// when clicking the front panel add class 'open' to panel
// if clicking back panel, remove 'open' from panel
for (var i = 0; i < numPanels; i++) {
  panels[i].addEventListener("click", function (event) {
    if (
      event.target.classList.contains("front") ||
      event.target.classList.contains("back")
    ) {
      this.classList.toggle("open");
      checkZ(this);
    }
  });
}

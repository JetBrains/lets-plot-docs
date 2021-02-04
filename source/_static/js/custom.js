document.addEventListener("DOMContentLoaded", function () {
  addLinkToPyPI();
  addLinkToGitHub();
});

function addLinkToPyPI() {
  const versionElem = document.querySelector("#navbar .navbar-version b");
  const versionParentElem = versionElem.parentElement;
  const linkElem = document.createElement("a");
  linkElem.href = "https://pypi.org/project/lets-plot";
  linkElem.target = "_blank";
  linkElem.appendChild(versionElem);
  versionParentElem.appendChild(linkElem);
}

function addLinkToGitHub() {
<<<<<<< HEAD
  const logoSize = document.getElementsByClassName('navbar-version')[0].clientHeight;
  const logoElem = document.createElement("div");
  logoElem.classList.add("github-logo");
  logoElem.style.display = "block";
  logoElem.style.width = logoSize + "px";
  logoElem.style.height = logoSize + "px";
=======
  const imgElem = document.createElement("img");
  imgElem.alt = "GitHub Logomark";
  imgElem.src = "_static/images/GitHub-Mark-Light-120px-plus.png";
>>>>>>> 8caf5005f6bc0c522a640b2be26a34e0f4fc14e2
  const linkElem = document.createElement("a");
  linkElem.href = "https://github.com/JetBrains/lets-plot";
  linkElem.classList.add("navbar-brand");
  linkElem.target = "_blank";
<<<<<<< HEAD
  linkElem.appendChild(logoElem);
=======
  linkElem.appendChild(imgElem);
>>>>>>> 8caf5005f6bc0c522a640b2be26a34e0f4fc14e2
  document.querySelector("#navbar .navbar-header").appendChild(linkElem);
}
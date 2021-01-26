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
  const imgElem = document.createElement("img");
  imgElem.alt = "GitHub Logomark";
  imgElem.src = "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png";
  const linkElem = document.createElement("a");
  linkElem.href = "https://github.com/JetBrains/lets-plot";
  linkElem.classList.add("navbar-brand");
  linkElem.target = "_blank";
  linkElem.appendChild(imgElem);
  document.querySelector("#navbar .navbar-header").appendChild(linkElem);
}
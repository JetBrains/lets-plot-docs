document.addEventListener("DOMContentLoaded", function () {
  const versionElem = document.querySelector("#navbar .navbar-version b");
  const versionParentElem = versionElem.parentElement;
  const linkElem = document.createElement("a");
  linkElem.href = "https://pypi.org/project/lets-plot/" + versionElem.textContent;
  linkElem.target = "_blank";
  linkElem.appendChild(versionElem);
  versionParentElem.appendChild(linkElem);
});
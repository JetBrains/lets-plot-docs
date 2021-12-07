document.addEventListener("DOMContentLoaded", function () {
  addLinkToPyPI();
  addLinkToGitHub();
  fixPanels();
  addTargetToExternalReferences();
  handlePreviewGallery();
});

function addLinkToPyPI() {
  const versionElem = document.querySelector("#navbar .navbar-version b");
  const versionParentElem = versionElem.parentElement;
  const linkElem = document.createElement("a");
  linkElem.href = "https://pypi.org/project/lets-plot";
  linkElem.classList.add("reference", "external");
  linkElem.appendChild(versionElem);
  versionParentElem.appendChild(linkElem);
}

function addLinkToGitHub() {
  const logoSize = document.getElementsByClassName('navbar-version')[0].clientHeight;
  const logoElem = document.createElement("div");
  logoElem.classList.add("github-logo");
  logoElem.style.display = "block";
  logoElem.style.width = logoSize + "px";
  logoElem.style.height = logoSize + "px";
  const linkElem = document.createElement("a");
  linkElem.href = "https://github.com/JetBrains/lets-plot";
  linkElem.classList.add("navbar-brand", "reference", "external");
  linkElem.appendChild(logoElem);
  document.querySelector("#navbar .navbar-header").appendChild(linkElem);
}

function fixPanels() {
  const cards = document.getElementsByClassName('card docutils');
  for (let i = 0; i < cards.length; i++)
    cards[i].classList.remove('shadow');
}

function addTargetToExternalReferences() {
  const links = document.getElementsByClassName("reference external");
  for (let i = 0; i < links.length; i++)
    links[i].setAttribute('target', '_blank');
}

function handlePreviewGallery() {
  if (document.getElementsByClassName('preview-gallery').length == 0) return;
  const previewsPerRow = 4;
  const previews = document.getElementsByClassName('preview-gallery')[0].getElementsByClassName('d-flex');
  const updatePreviewGallery = function (currentHiddenRowId) {
    for (let i = 0; i < previews.length; i++)
      if (i < currentHiddenRowId * previewsPerRow) {
        previews[i].classList.remove('hidden');
        previews[i].style.height = String(previews[i].offsetWidth) + 'px';
      } else
        previews[i].classList.add('hidden');
  }
  const thereIsMorePreviews = function () {
    return !![...previews].find(elem => elem.classList.contains('hidden'));
  }
  let hiddenRowId = 1;
  const loadMoreOnClick = function (event) {
    if (thereIsMorePreviews()) {
      event.preventDefault();
      hiddenRowId++;
      updatePreviewGallery(hiddenRowId);
      if (thereIsMorePreviews()) return;
      event.target.classList.add("hidden");
    }
  }
  updatePreviewGallery(hiddenRowId);
  document.getElementById('preview-gallery-more').getElementsByTagName('a')[0].onclick = loadMoreOnClick;
}
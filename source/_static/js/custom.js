document.addEventListener("DOMContentLoaded", function () {
  fixNavLinks();
  removeCardShadows();
  addTargetToExternalReferences();
  handlePreviewGallery();
});

function fixNavLinks() {
  const navItems = document.getElementsByClassName("navbar-nav")[0].getElementsByClassName("nav-item");
  for (let i = 0; i < navItems.length; i++) {
    const navLink = navItems[i].getElementsByClassName("nav-link")[0];
    navLink.classList.remove("nav-external");
    navLink.classList.add("nav-internal");
  }
}

function removeCardShadows() {
  const cards = document.getElementsByClassName('sd-card docutils');
  for (let i = 0; i < cards.length; i++)
    cards[i].classList.remove('sd-shadow-sm');
}

function addTargetToExternalReferences() {
  const links = document.getElementsByClassName("reference external");
  for (let i = 0; i < links.length; i++)
    links[i].setAttribute('target', '_blank');
}

function handlePreviewGallery() {
  if (document.getElementsByClassName('preview-gallery').length == 0) return;
  const gridElementClass = "sd-d-flex-row";
  const previewsPerRow = 4;
  const previews = document.getElementsByClassName('preview-gallery')[0].getElementsByClassName(gridElementClass);
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
      event.target.classList.add('hidden');
    }
  }
  updatePreviewGallery(hiddenRowId);
  document.getElementById('preview-gallery-more').getElementsByTagName('a')[0].onclick = loadMoreOnClick;
}
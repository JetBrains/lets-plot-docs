document.addEventListener("DOMContentLoaded", function () {
  fixNavLinks();
  fixNavLinksOnLandingPage();
  removeCardShadows();
  addTargetToExternalReferences();
  handlePreviewGallery();
});

function fixNavLinks() {
  const navItems = document.getElementsByClassName("navbar-nav")[0].getElementsByClassName("nav-item");
  for (let i = 0; i < navItems.length; i++) {
    const navLink = getNavLinkOrNull(navItems[i]);
    if (navLink === null) continue;
    navLink.classList.remove("nav-external");
    navLink.classList.add("nav-internal");
  }
}

function fixNavLinksOnLandingPage() {
  const excludedNavLinks = ["github", "pypi"];
  if (!isLandingPage()) return;
  const navItems = document.getElementsByClassName("bd-header")[0].getElementsByClassName("nav-item");
  for (let i = 0; i < navItems.length; i++) {
    const navItem = navItems[i];
    const navLink = getNavLinkOrNull(navItem);
    if (navLink === null) continue;
    for (let j = 0; j < excludedNavLinks.length; j++) {
      if (navLink.href.indexOf(excludedNavLinks[j]) != -1)
        navItem.classList.add("hidden");
    }
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

function isLandingPage() {
  return document.getElementsByClassName("bd-breadcrumbs").length == 0;
}

function getNavLinkOrNull(navItem) {
  const navLinks = navItem.getElementsByClassName("nav-link");
  return navLinks.length != 0 ? navLinks[0] : null;
}
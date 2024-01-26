document.addEventListener("DOMContentLoaded", function () {
  fixNavLinks();
  removeEmptySecondarySidebar();
  removeCardShadows();
  addTargetToExternalReferences();
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

function removeEmptySecondarySidebar() {
  const sidebarElements = document.getElementsByClassName("bd-sidebar-secondary bd-toc");
  for (let i = 0; i < sidebarElements.length; i++) {
    const sidebarElement = sidebarElements[i];
    if (sidebarElement.hasChildNodes()) continue;
    sidebarElement.style.display = "none";
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

function isLandingPage() {
  return document.getElementsByClassName("bd-breadcrumbs").length == 0;
}

function getNavLinkOrNull(navItem) {
  const navLinks = navItem.getElementsByClassName("nav-link");
  return navLinks.length != 0 ? navLinks[0] : null;
}
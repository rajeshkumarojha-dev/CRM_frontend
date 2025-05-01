


// side bar
document.addEventListener('DOMContentLoaded', function () {
    const html = document.documentElement;
    const toggleBtn = document.getElementById('toggle-btn');

    toggleBtn.addEventListener('click', function () {
        html.classList.toggle('sidebar-collapsed');
        localStorage.setItem('sidebarCollapsed', html.classList.contains('sidebar-collapsed'));
    });
});


document.addEventListener('DOMContentLoaded', function () {
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    tooltipTriggerList.forEach(function (tooltipTriggerEl) {
        new bootstrap.Tooltip(tooltipTriggerEl);
    });
});

// darkmode
// Toggle dark mode
// This script toggles between light and dark mode based on user preference
const themeBtn = document.querySelector(".toggle-theme");
const root = document.documentElement;

// Load theme from localStorage
const savedTheme = localStorage.getItem("theme");
if (savedTheme === "dark") {
    root.classList.add("dark-mode");
    themeBtn.classList.remove("fa-moon");
    themeBtn.classList.add("fa-sun");
}

if (themeBtn) {
    themeBtn.addEventListener("click", function (e) {
        e.preventDefault();
        root.classList.toggle("dark-mode");

        const isDark = root.classList.contains("dark-mode");
        localStorage.setItem("theme", isDark ? "dark" : "light");

        // Toggle icon class
        if (isDark) {
            themeBtn.classList.remove("fa-moon");
            themeBtn.classList.add("fa-sun");
        } else {
            themeBtn.classList.remove("fa-sun");
            themeBtn.classList.add("fa-moon");
        }
    });
}
// Sidebar in responsive view

let menu = document.querySelector(".nav-icon");
let sidebar = document.querySelector(".sidebar");

menu.addEventListener("click", (event) => {
    sidebar.classList.toggle("sidebar-active");
    event.stopPropagation();
});

window.addEventListener("click", () => {
    sidebar.classList.remove("sidebar-active");
});

// Prevent sidebar from closing when clicking inside it
sidebar.addEventListener("click", (event) => {
    event.stopPropagation();
});

function closeModal() {
    document.querySelector('.modal-custom').style.display = 'none';
}


let menuIcon = document.querySelector('.bars');
let menuContainer = document.querySelector('.header-icons');

menuIcon.addEventListener('click', function (e) {
    e.stopPropagation(); // Prevent event from bubbling to document
    menuIcon.classList.toggle('fa-xmark');
    menuContainer.classList.toggle('active');
});

// Close menu if clicked outside
document.addEventListener('click', function (e) {
    if (!menuContainer.contains(e.target) && !menuIcon.contains(e.target)) {
        menuIcon.classList.remove('fa-xmark');
        menuContainer.classList.remove('active');
    }
});



// detaills-sidebar script //user deatils

let detailSidebar = document.querySelector('.details-sidebar');
let detailsMenu = document.querySelector('.detail-menubar');
let detailsClose = document.querySelector('.details-close');

if (detailsMenu) {
    detailsMenu.addEventListener('click', function (event) {
        detailSidebar.classList.add('active');
        detailsClose.classList.remove("active");

        event.stopPropagation();
    });
}

if (detailsClose) {
    detailsClose.addEventListener('click', function () {
        detailSidebar.classList.remove('active');

    })
}

// Close sidebar when clicking outside
if(detailSidebar){
    window.addEventListener('click', function (event) {
        if (!detailSidebar.contains(event.target) && !detailsMenu.contains(event.target)) {
            detailSidebar.classList.remove('active');
        }
    });
}


// Prevent sidebar clicks from closing it
if (detailSidebar) {
    detailSidebar.addEventListener('click', function (event) {
        event.stopPropagation();
    });
}



// <!-- DataTables Script -->

$(document).ready(function () {
    $('#myTable').DataTable({
        scrollY: '45vh',
        scrollX: true,
        scrollCollapse: true,
        paging: true,
        responsive: true
    });
});

$(document).ready(function () {
    $('#companyTable').DataTable({
        scrollX: true,
        scrollY: '45vh',
        scrollCollapse: true,
        paging: true,
        searching: true,
        ordering: true,
        responsive: false
    });
});


$(document).ready(function () {
    $('#contactactivity').DataTable({
      scrollX: true,
      scrollY: '45vh',
      scrollCollapse: true,
      paging: true,
      searching: true,
      ordering: true,
      responsive: false
    });
  });

  $(document).ready(function () {
    $('#groupTable').DataTable({
        scrollX: true,
        scrollY: '45vh',
        responsive: true,
        pageLength: 10
    });
});

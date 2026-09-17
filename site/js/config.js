// docs/js/config.js
// Usa las credenciales públicas (OK para el frontend)
window.SUPABASE_URL = "https://gcxjphckdxmymqmduabn.supabase.co";
window.SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdjeGpwaGNrZHhteW1xbWR1YWJuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTc1MTc5NDQsImV4cCI6MjA3MzA5Mzk0NH0.wOUm-g3EXGMIq3xrNvigCHK2q017h06jx5cLHoLJro0";

document.addEventListener("click", (event) => {
	const link = event.target.closest(".md-sidebar--primary .md-nav__link");
	const page = event.target.closest(".md-main, .md-overlay");
	const drawer = document.getElementById("__drawer");

	if ((link || page) && drawer) {
		drawer.checked = false;
	}
});

document.addEventListener("keydown", (event) => {
	const drawer = document.getElementById("__drawer");

	if (event.key === "Escape" && drawer) {
		drawer.checked = false;
	}
});
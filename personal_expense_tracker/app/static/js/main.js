// Scroll-triggered animations using Intersection Observer
(function () {
	if (!('IntersectionObserver' in window)) return;
	const animateEls = document.querySelectorAll('.card, .hero, .animate-in, .animate-slide-up');
	const io = new IntersectionObserver((entries) => {
		for (const e of entries) {
			if (e.isIntersecting) {
				e.target.classList.add('animate-in', 'animate-slide-up');
				io.unobserve(e.target);
			}
		}
	}, { threshold: 0.08 });
	animateEls.forEach(el => io.observe(el));
})();

// Simple toast API
window.showToast = function (message, type = 'success', timeout = 3000) {
	const container = document.getElementById('toast-container');
	if (!container) return;
	const item = document.createElement('div');
	item.className = `toast-item ${type}`;
	item.setAttribute('role', 'status');
	item.textContent = message;
	container.appendChild(item);
	setTimeout(() => { item.remove(); }, timeout);
}

